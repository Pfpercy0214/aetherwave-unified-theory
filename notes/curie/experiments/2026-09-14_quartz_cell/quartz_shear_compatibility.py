#!/usr/bin/env python3
"""Quartz compatibility-first audit (2026-09-14), Python 3.10+ and NumPy.

Place beside the frozen quartz_cell_audit.py. Run:
    python quartz_shear_compatibility.py --out compatibility_results

NO coefficients, coordinates, orientation, or channel thresholds are fitted.
The target is the prior conventional zero-stress static piezoelectric control,
not a measured atomic trajectory or a resonator mode. Least-squares projections
are diagnostics, NOT predictions of physical atomic response.
"""
from __future__ import annotations
import argparse
import csv
import hashlib
import itertools
import json
from pathlib import Path
import numpy as np
import quartz_cell_audit as base

BASE_SHA256='593b2f441a3f6c0c8e71e06b81138a50be8687f1538bbde66466393cc39d44f5'
MIRROR=np.diag([1.,1.,-1.])
# Engineering s=(Sxx,Syy,Szz,2Syz,2Sxz,2Sxy); ||W s|| is tensor Frobenius norm.
W=np.diag([1.,1.,1.,1/np.sqrt(2),1/np.sqrt(2),1/np.sqrt(2)])
SOURCES={
 'atomic_basis_and_setting': 'https://journals.iucr.org/j/issues/2022/04/00/te5094/',
 'convention_sign_table': 'https://doc.comsol.com/6.4/doc/com.comsol.help.sme/sme_ug_modeling.05.108.html',
 'unaltered_material_constants': 'https://ansyshelp.ansys.com/public/Views/Secured/corp/v261/en/ans_cou/Hlp_G_COU3_piezo.html',
 'experimental_motivation': 'https://www.intechopen.com/chapters/83792',
}


def dextro_basis(u=.4697,x=.4133,y=.2672,z=.1188):
    return np.asarray([[u,0,0],[0,u,2/3],[-u,-u,1/3],
        [x,y,z],[-y,x-y,z+2/3],[y-x,-x,z+1/3],
        [x-y,-y,-z],[-x,y-x,-z+1/3],[y,x,-z+2/3]])%1


def laevo_reverse_basis(u=.5303,x=.5867,y=.7328,z=.8812):
    # IUCr Table 5, with Table 3 complementary coordinates.
    return np.asarray([[u,0,0],[0,u,1/3],[-u,-u,2/3],
        [x,y,z],[-y,x-y,z+1/3],[y-x,-x,z+2/3],
        [x-y,-y,-z],[-x,y-x,-z+2/3],[y,x,-z+1/3]])%1


def nullspace(A,rtol=1e-10):
    _,sv,vh=np.linalg.svd(A,full_matrices=True)
    rank=int(np.sum(sv>rtol*sv[0])) if len(sv) and sv[0] else 0
    return vh[rank:].T,rank,sv


def orthogonal_span(B,rtol=1e-10):
    u,sv,_=np.linalg.svd(B,full_matrices=False)
    rank=int(np.sum(sv>rtol*sv[0])) if len(sv) and sv[0] else 0
    return u[:,:rank],rank


def strain_transform(Q):
    return np.column_stack([base.strain_vector(Q@base.strain_matrix(s)@Q.T) for s in np.eye(6)])


def transform_material(C,e,eps,Q):
    # Passive frame or active material transformation used consistently for all tensors.
    T=strain_transform(Q);Ti=np.linalg.inv(T)
    return Ti.T@C@Ti,Q@e@Ti,Q@eps@Q.T


def constraints(lattice,frac,cutoff=1.8):
    a=float(np.linalg.norm(lattice[0]));edges=[]
    for i in range(3):
        nb=base.neighbors(i,range(3,9),lattice,frac,cutoff)
        if len(nb)!=4:raise ValueError(f'Si{i+1} coordination {len(nb)} != 4')
        for _,j,q,_ in nb:edges.append((i,j,np.zeros(3),q,'SiO'))
        for n1,n2 in itertools.combinations(nb,2):edges.append((n1[1],n2[1],n1[2],n2[2],'OO'))
    rows=[];lengths=[]
    for i,j,qi,qj,_ in edges:
        b=(frac[j]+qj-frac[i]-qi)@lattice/a;n=b/np.linalg.norm(b)
        row=np.zeros(33);row[3*i:3*i+3]-=n;row[3*j:3*j+3]+=n
        row[27:]=[n@base.strain_matrix(s)@b for s in np.eye(6)]
        rows.append(row);lengths.append(float(np.linalg.norm(b)))
    J=np.asarray(rows);gauge=np.zeros((3,33))
    for k in range(3):gauge[k,k:27:3]=1/3
    mask=np.array([edge[-1]=='SiO' for edge in edges])
    return J,gauge,mask,np.asarray(lengths),edges


def construct_space(J,gauge,mask=None):
    rows=J if mask is None else J[mask]
    A=np.vstack([rows,gauge]);N,rank,sv=nullspace(A);B=N[27:]
    Q,srank=orthogonal_span(W@B)
    return dict(A=A,N=N,B=B,projector=Q@Q.T,rank=rank,srank=srank,singular=sv)


def projection(space,s):
    coef=np.linalg.lstsq(W@space['B'],W@s,rcond=1e-10)[0]
    q=space['N']@coef;sp=q[27:];ws=W@s
    nr=float(np.linalg.norm(W@(s-sp)));den=float(np.linalg.norm(ws))
    return dict(strain_target=s.tolist(),nearest_compatible_strain=sp.tolist(),
        residual_strain=(s-sp).tolist(),target_Frobenius_norm=den,
        relative_Frobenius_residual=None if den<1e-25 else nr/den,
        angular_mismatch_degrees=None if den<1e-25 else float(np.rad2deg(np.arcsin(np.clip(nr/den,0,1)))),
        relative_constraint_residual=None if den<1e-25 else float(np.linalg.norm(space['A']@q)/den))


def finite_shape_diagnostic(J,gauge,mask,lengths,lattice,frac,s):
    # Hold each SiO length exactly at first order; select one representative by
    # minimum sum of squared fractional OO distance changes. This is NOT a force law.
    A=np.vstack([J[mask,:27],gauge[:,:27]]);b=np.r_[-J[mask,27:]@s,np.zeros(3)]
    u0=np.linalg.lstsq(A,b,rcond=1e-10)[0];Nu,rank,_=nullspace(A)
    O=J[~mask,:27]/lengths[~mask,None];Os=J[~mask,27:]/lengths[~mask,None]
    z=np.linalg.lstsq(O@Nu,-(O@u0+Os@s),rcond=1e-10)[0];u=u0+Nu@z
    frac_changes=(J[:,:27]@u+J[:,27:]@s)/lengths
    a=np.linalg.norm(lattice[0]);disp=u.reshape(9,3)*a;angles=[]
    for i in range(3):
        nb=base.neighbors(i,range(3,9),lattice,frac)
        for n1,n2 in itertools.combinations(nb,2):
            b1,b2=n1[3],n2[3];db1=base.strain_matrix(s)@b1+disp[n1[1]]-disp[i]
            db2=base.strain_matrix(s)@b2+disp[n2[1]]-disp[i]
            l1,l2=np.linalg.norm(b1),np.linalg.norm(b2);c=(b1@b2)/l1/l2
            dc=(db1@b2+b1@db2)/l1/l2-c*(b1@db1/l1**2+b2@db2/l2**2)
            angles.append(float(-dc/np.sqrt(1-c*c)*180/np.pi))
    return dict(status='Target-conditioned geometric feasibility example, NOT predicted atomic motion.',
        selector='Minimum squared fractional OO changes, exact first-order SiO lengths, zero-translation gauge.',
        unconstrained_internal_modes_at_fixed_strain=27-rank,
        maximum_fractional_SiO_change=float(np.max(abs(frac_changes[mask]))),
        rms_fractional_OO_change=float(np.sqrt(np.mean(frac_changes[~mask]**2))),
        maximum_fractional_OO_change=float(np.max(abs(frac_changes[~mask]))),
        maximum_abs_OSiO_angle_change_degrees=float(np.max(abs(np.asarray(angles)))),
        non_affine_displacements_A=disp.tolist(),OSiO_angle_changes_degrees=angles,
        fractional_edge_changes=frac_changes.tolist())


def check(condition,message):
    if not condition:raise AssertionError(message)


def run():
    actual=hashlib.sha256(Path(base.__file__).read_bytes()).hexdigest()
    check(actual==BASE_SHA256,'Frozen source hash mismatch; review changed inputs before rerunning.')
    lattice,original,labels=base.structure();C,e,eps=base.material_tensors()
    # Operational registration: dextro z(+) -> laevo r(+), by inversion and
    # Rz(pi): net mirror z. This is an enantiomorph+setting conversion, NOT
    # a proper rotation of the same specimen. The old constants are unchanged.
    frac=(original@MIRROR)%1
    from_table=(laevo_reverse_basis()@np.diag([-1.,-1.,1.]))%1
    diff=frac-from_table;diff-=np.round(diff)
    map_error=float(np.max(abs(diff)));check(map_error<1e-14,'Enantiomorph/setting crosswalk failed')
    J,gauge,mask,lengths,edges=constraints(lattice,frac)
    space=construct_space(J,gauge);B=space['B']
    check(space['rank']==30 and space['srank']==3,'Unexpected rigid-unit dimension')
    r=float((B[5]@B[4])/(B[5]@B[5]))
    zratio=float(((B[0]+B[1])@B[2])/np.dot(B[0]+B[1],B[0]+B[1]))
    identity_rows=np.zeros((3,6));identity_rows[0,2]=1;identity_rows[0,:2]=-zratio
    identity_rows[1,3]=1;identity_rows[1,0]=-r;identity_rows[1,1]=r
    identity_rows[2,4]=1;identity_rows[2,5]=-r
    check(np.linalg.norm(identity_rows@B)<1e-12,'Compact strain relations not exact')
    EAT=1e5*np.array([0,np.cos(np.deg2rad(35.25)),np.sin(np.deg2rad(35.25))])
    vectors={'X':np.array([1e5,0,0]),'Y':np.array([0,1e5,0]),'Z':np.array([0,0,1e5]),'AT':EAT,'AT_reversed':-EAT,'AT_double':2*EAT}
    responses={};simple=[]
    for name,E in vectors.items():
        s=np.linalg.solve(C,e.T@E);p=projection(space,s);responses[name]={'E_V_m':E.tolist(),**p}
        simple.append(dict(case=name,residual_fraction=p['relative_Frobenius_residual'],
            angular_mismatch_deg=p['angular_mismatch_degrees'],**{f'target_{i}':float(s[i]) for i in range(6)}))
    target=np.asarray(responses['AT']['strain_target']);ref=responses['AT']['relative_Frobenius_residual']
    check(abs(ref-.413028873242529)<1e-10,'Unexpected principal mismatch')
    # Deliberately wrong direct combination, saved as a negative control.
    wrong=construct_space(*constraints(lattice,original)[:2])
    wrong_result=projection(wrong,target)
    # Recover equivalent description in original dextro geometry, mapping ALL
    # tensor objects and the loading by the same improper transformation.
    Cm,em,epsm=transform_material(C,e,eps,MIRROR)
    back=projection(wrong,np.linalg.solve(Cm,em.T@(MIRROR@EAT)))
    # Arbitrary proper rotation covariance: rebuild constraints from rotated bonds.
    rng=np.random.default_rng(9142026);rotation_errors=[]
    for _ in range(16):
        Q,_=np.linalg.qr(rng.normal(size=(3,3)))
        if np.linalg.det(Q)<0:Q[:,0]*=-1
        Jr,gr,*_=constraints(lattice@Q.T,frac)
        Cr,er,epsr=transform_material(C,e,eps,Q)
        sr=np.linalg.solve(Cr,er.T@(Q@EAT))
        pr=projection(construct_space(Jr,gr),sr)
        rotation_errors.append(abs(pr['relative_Frobenius_residual']-ref))
    # Order and gauge invariance.
    order=rng.permutation(30)
    order_res=projection(construct_space(J[order],gauge),target)['relative_Frobenius_residual']
    scaled_gauge_res=projection(construct_space(J,7*gauge),target)['relative_Frobenius_residual']
    relaxed=construct_space(J,gauge,mask)
    relaxed_res=projection(relaxed,target)
    check(relaxed['srank']==6 and relaxed['rank']==15,'Unexpected SiO-only rank')
    # Rounding sensitivity only: perturb four prototype numbers within +/- half
    # their last printed decimal place, preserving all crystallographic symmetries.
    rounding=[]
    for _ in range(100):
        params=np.array([.4697,.4133,.2672,.1188])+rng.uniform(-5e-5,5e-5,4)
        f=(dextro_basis(*params)@MIRROR)%1
        JJ,gg,*_=constraints(lattice,f);ss=construct_space(JJ,gg)
        rounding.append(projection(ss,target)['relative_Frobenius_residual'])
    cutoffs={}
    for cutoff in (1.7,1.8,1.9):
        j,g,*_=constraints(lattice,frac,cutoff)
        cutoffs[str(cutoff)]=projection(construct_space(j,g),target)['relative_Frobenius_residual']
    # Recheck local linearized distances by central finite differences.
    aa=np.linalg.norm(lattice[0])
    def lens(q):
        u=q[:27].reshape(9,3);F=np.eye(3)+base.strain_matrix(q[27:])
        return np.array([np.linalg.norm(F@((frac[j]+qj-frac[i]-qi)@lattice/aa)+u[j]-u[i]) for i,j,qi,qj,_ in edges])
    h=1e-6;fd=np.column_stack([(lens(h*x)-lens(-h*x))/(2*h) for x in np.eye(33)])
    fd_error=float(np.max(abs(fd-J)))
    checks={'table_5_to_registered_coordinates_max_error':map_error,
        'constraint_matrix_finite_difference_max_error':fd_error,
        'rigid_nullspace_residual':float(np.linalg.norm(space['A']@space['N'])),
        'mirror_equivalent_residual_difference':abs(ref-back['relative_Frobenius_residual']),
        'largest_proper_rotation_residual_difference':max(rotation_errors),
        'row_permutation_residual_difference':abs(ref-order_res),
        'gauge_scaling_residual_difference':abs(ref-scaled_gauge_res),
        'SiO_only_relative_Frobenius_residual':relaxed_res['relative_Frobenius_residual']}
    check(max(rotation_errors)<1e-12,'Frame-dependent projection metric')
    check(abs(ref-back['relative_Frobenius_residual'])<1e-12,'Mirror covariance failed')
    check(fd_error<1e-8,'Finite-difference Jacobian mismatch')
    finite=finite_shape_diagnostic(J,gauge,mask,lengths,lattice,frac,target)
    d=np.linalg.solve(C,e.T)
    return {'date':'2026-09-14','baseline_commit':'f3035c02d828cf568e2398fa0234b2cc78c642b5',
        'status':'Compatibility audit: exact rigid units fail the specified static piezoelectric control. Not an ARK validation or atomistic response prediction.',
        'sources':SOURCES,'numpy_version':np.__version__,'base_code_sha256':actual,
        'code_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        'registration':{'operation':'Original IUCr dextro z(+) -> inversion -> laevo z(-) -> Rz(pi) -> laevo r(+).',
            'net_cartesian_matrix':MIRROR.tolist(),'handedness_note':'An enantiomorph plus setting conversion, not a proper rotation of the same specimen.',
            'sign_table_inference':'Inherited c14<0,e11>0,e14<0 matches the IRE left/laevo sign family. Matrix index format alone does not identify crystallographic axes.',
            'registered_lattice_vectors_A':lattice.tolist(),'registered_fractional_positions':frac.tolist(),
            'atom_labels':labels,'direct_table_crosscheck_error':map_error,
            'specimen_limit':'No handedness or domain measurement is available for any particular resonator; this is a registered material-control comparison.'},
        'rigid':{'total_variables':33,'constraint_rank_including_translation_gauge':space['rank'],
            'admissible_dimension':space['N'].shape[1],'strain_subspace_rank':space['srank'],
            'strain_basis_engineering':B.tolist(),'nullspace':space['N'].tolist(),
            'projector_Mandel':space['projector'].tolist(),'compact_constraint_rows':identity_rows.tolist(),
            'strain_relations':{'s3_over_s1_plus_s2':zratio,'s4_over_s1_minus_s2_and_s5_over_s6':r},
            'singular_values':space['singular'].tolist()},
        'control':{'C_Pa':C.tolist(),'e_C_m2':e.tolist(),'d_m_V':d.tolist(),
            's5_over_s6_for_Y_field':float(d[4,1]/d[5,1]),'responses':responses},
        'wrong_direct_combination':wrong_result,'mirror_equivalent_comparison':back,
        'relaxed_SiO_only':{'constraint_rank':relaxed['rank'],'admissible_dimension':relaxed['N'].shape[1],
            'strain_subspace_rank':relaxed['srank'],'target_projection':relaxed_res},
        'finite_shape_diagnostic':finite,'checks':checks,
        'rounding_sensitivity':{'draws':100,'prototype_half_width':5e-5,'minimum_residual':min(rounding),
            'maximum_residual':max(rounding),'interpretation':'Printed-coordinate rounding sensitivity, NOT experimental uncertainty or probability.'},
        'cutoff_checks':cutoffs},simple


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--out',type=Path,default=Path('compatibility_results'))
    args=parser.parse_args();args.out.mkdir(parents=True,exist_ok=True)
    report,rows=run()
    (args.out/'results.json').write_text(json.dumps(report,indent=2,allow_nan=False)+'\n',encoding='utf-8')
    with (args.out/'comparison.csv').open('w',newline='',encoding='utf-8') as f:
        w=csv.DictWriter(f,fieldnames=rows[0]);w.writeheader();w.writerows(rows)
    print(json.dumps({'rigid_dimension':report['rigid']['admissible_dimension'],
        'strain_relations':report['rigid']['strain_relations'],
        'control_ratio':report['control']['s5_over_s6_for_Y_field'],
        'AT_response':report['control']['responses']['AT'],'checks':report['checks'],
        'rounding':report['rounding_sensitivity'],
        'relaxed_ranks':[report['relaxed_SiO_only']['constraint_rank'],report['relaxed_SiO_only']['strain_subspace_rank']],
        'finite_shape':{k:v for k,v in report['finite_shape_diagnostic'].items() if k not in ('non_affine_displacements_A','OSiO_angle_changes_degrees','fractional_edge_changes')}},indent=2))

if __name__=='__main__':main()
