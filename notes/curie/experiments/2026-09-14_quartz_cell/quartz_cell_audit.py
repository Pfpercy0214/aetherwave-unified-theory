#!/usr/bin/env python3
"""Quartz starting-point audit, 2026-09-14. Requires Python 3.10+ and NumPy.

Run: python quartz_cell_audit.py --out results

Three explicitly separated calculations:
  A. Periodic nine-atom geometry and field-direction projections.
  B. Infinitesimal rigid-tetrahedron compatibility, not an atomistic force model.
  C. Homogeneous linear piezoelectric energy control using supplied tensors.

No resonance, channel-mobility, lifetime, or damage data are used. Part C does
not derive its coefficients from part A/B. Their signed crystallographic
convention crosswalk remains to be completed before combining them atomically.
"""
from __future__ import annotations
import argparse
import csv
import hashlib
import itertools
import json
from pathlib import Path
import numpy as np

SOURCES = {
    'geometry': 'https://doi.org/10.1107/S1600576722005945',
    'geometry_html': 'https://journals.iucr.org/j/issues/2022/04/00/te5094/',
    'atomic_motion': 'https://doi.org/10.1063/1.4935591',
    'author_account': 'https://www.intechopen.com/chapters/83792',
    'tensor_control': 'https://ansyshelp.ansys.com/public/Views/Secured/corp/v261/en/ans_cou/Hlp_G_COU3_piezo.html',
    'conventions': 'https://doc.comsol.com/6.4/doc/com.comsol.help.sme/sme_ug_modeling.05.108.html',
    'atomic_response_method': 'https://docs.abinit.org/tutorial/elastic/',
}


def strain_matrix(s: np.ndarray) -> np.ndarray:
    """Engineering Voigt order xx,yy,zz,yz,xz,xy; shear entries are 2*S_ij."""
    s = np.asarray(s, dtype=float)
    return np.array([[s[0], s[5]/2, s[4]/2],
                     [s[5]/2, s[1], s[3]/2],
                     [s[4]/2, s[3]/2, s[2]]])


def strain_vector(a: np.ndarray) -> np.ndarray:
    return np.array([a[0,0], a[1,1], a[2,2], 2*a[1,2], 2*a[0,2], 2*a[0,1]])


def structure() -> tuple[np.ndarray, np.ndarray, list[str]]:
    # IUCr Table 4: dextro P3221, z(+) setting, right-handed Cartesian axes.
    # Lattice vectors are rows; fractional row vector f maps as f @ lattice.
    a, c = 4.9137, 5.4047  # angstrom, reported 298 K lattice parameters
    u, x, y, z = 0.4697, 0.4133, 0.2672, 0.1188
    lattice = np.array([[a,0,0], [-a/2,np.sqrt(3)*a/2,0], [0,0,c]])
    frac = np.array([[u,0,0], [0,u,2/3], [-u,-u,1/3],
                     [x,y,z], [-y,x-y,z+2/3], [y-x,-x,z+1/3],
                     [x-y,-y,-z], [-x,y-x,-z+1/3], [y,x,-z+2/3]]) % 1.0
    labels = ['Si1','Si2','Si3','O1','O2','O3','O4','O5','O6']
    return lattice, frac, labels


SHIFTS = [np.asarray(t, float) for t in itertools.product((-1,0,1), repeat=3)]


def neighbors(i: int, candidates: range, lattice: np.ndarray,
              frac: np.ndarray, cutoff: float = 1.8) -> list[tuple]:
    out = []
    for j in candidates:
        for shift in SHIFTS:
            b = (frac[j]+shift-frac[i]) @ lattice
            distance = float(np.linalg.norm(b))
            if 1e-8 < distance < cutoff:
                out.append((distance, j, shift.copy(), b))
    return sorted(out, key=lambda item: (item[0],item[1],tuple(item[2])))


def geometric_audit(lattice: np.ndarray, frac: np.ndarray) -> tuple[dict,list[dict]]:
    angle = np.deg2rad(35.25)
    direction = np.array([0,np.cos(angle),np.sin(angle)])
    normals, rows = [], []
    for i in range(3,9):
        nb = neighbors(i,range(3),lattice,frac)
        if len(nb) != 2:
            raise ValueError('Each oxygen must have exactly two Si neighbors.')
        b1,b2 = nb[0][3],nb[1][3]
        normal = np.cross(b1,b2); normal /= np.linalg.norm(normal)
        normals.append(normal)
        bridge_angle = np.rad2deg(np.arccos(np.clip(np.dot(b1,b2)/np.linalg.norm(b1)/np.linalg.norm(b2),-1,1)))
        projection = float(normal@direction)
        rows.append(dict(site=f'O{i-2}',bond_short_A=nb[0][0],bond_long_A=nb[1][0],
                         Si_O_Si_deg=float(bridge_angle),
                         field_plane_angle_deg=float(np.rad2deg(np.arcsin(abs(projection)))),
                         signed_projection=projection,projection_squared=projection**2))
    total = sum(r['projection_squared'] for r in rows)
    for row in rows: row['normalized_geometric_score'] = row['projection_squared']/total
    ns=np.asarray(normals)
    rotations={}
    for deg in (0,35,35.25,90,-35.25):
        n=np.array([0,np.cos(np.deg2rad(deg)),np.sin(np.deg2rad(deg))])
        p=ns@n
        rotations[str(deg)]={'field_plane_angles_deg':np.rad2deg(np.arcsin(np.clip(abs(p),0,1))).tolist(),
                            'projection_scores':(p*p/np.dot(p,p)).tolist()}
    coordination={str(cutoff):[len(neighbors(i,range(3,9),lattice,frac,cutoff)) for i in range(3)] for cutoff in (1.7,1.8,1.9)}
    return {'convention':'IUCr dextro z(+), X parallel a, Z parallel c',
            'field_direction':direction.tolist(), 'tilt_deg':35.25,
            'Si_coordination_cutoff_check':coordination,
            'strongest_pair_projection_score':sum(sorted(r['normalized_geometric_score'] for r in rows)[-2:]),
            'rotation_checks':rotations,
            'status':'Geometry-only squared projection, NOT current, occupancy, energy fraction, or measured displacement.'},rows


def compatibility_audit(lattice: np.ndarray, frac: np.ndarray) -> dict:
    a=float(lattice[0,0]); strain_basis=[strain_matrix(e) for e in np.eye(6)]
    edges=[]
    for i in range(3):
        nb=neighbors(i,range(3,9),lattice,frac)
        if len(nb)!=4:raise ValueError('Incorrect Si coordination')
        for _,j,q,_ in nb:edges.append((i,j,np.zeros(3),q))
        for nb1,nb2 in itertools.combinations(nb,2):
            edges.append((nb1[1],nb2[1],nb1[2],nb2[2]))
    rows=[]
    for i,j,qi,qj in edges:
        d=(frac[j]+qj-frac[i]-qi)@lattice/a
        n=d/np.linalg.norm(d)
        row=np.zeros(33);row[3*i:3*i+3]-=n;row[3*j:3*j+3]+=n
        row[27:]=[n@B@d for B in strain_basis]
        rows.append(row)
    J=np.asarray(rows)
    translations=np.zeros((3,33))
    for k in range(3):translations[k,k:27:3]=1/3
    A=np.vstack([J,translations])
    _,singular,Vh=np.linalg.svd(A,full_matrices=True)
    rank=int(np.sum(singular>1e-10*singular[0]))
    null=Vh[rank:].T
    ranks={str(t):int(np.sum(singular>t*singular[0])) for t in (1e-8,1e-10,1e-12)}
    # Central finite-difference check of the entire bond-length Jacobian.
    def lengths(q):
        displacements=q[:27].reshape(9,3)
        F=np.eye(3)+strain_matrix(q[27:])
        return np.array([np.linalg.norm(F@((frac[j]+qj-frac[i]-qi)@lattice/a)+displacements[j]-displacements[i])
                         for i,j,qi,qj in edges])
    step=1e-6
    fd=np.column_stack([(lengths(step*e)-lengths(-step*e))/(2*step) for e in np.eye(33)])
    fixed=np.vstack([A,np.column_stack([np.zeros((6,27)),np.eye(6)])])
    fixed_rank=int(np.linalg.matrix_rank(fixed,tol=1e-9))
    residual=float(np.linalg.norm(A@null,ord=np.inf))
    if rank!=30 or residual>1e-12:raise AssertionError('Unexpected compatibility rank/residual')
    return {'degrees_of_freedom':33,'internal_Cartesian_displacements':27,'symmetric_cell_strains':6,
            'bond_length_constraints':30,'translation_gauge_constraints':3,
            'combined_rank':rank,'compatible_infinitesimal_modes':33-rank,
            'ranks_by_relative_threshold':ranks,'fixed_cell_modes':33-fixed_rank,
            'max_Jacobian_finite_difference_error':float(np.max(abs(fd-J))),
            'nullspace_residual_infinity_norm':residual,
            'singular_values':singular.tolist(),
            'status':'Periodic zero-wavevector infinitesimal rigid-SiO4 approximation; NOT frequencies, nonlinear accessibility, or quantum state counts.'}


def material_tensors() -> tuple[np.ndarray,np.ndarray,np.ndarray]:
    # ANSYS 2.3.7 coefficients and matrix layout, engineering Voigt notation.
    # c66 is obtained from trigonal symmetry, matching its tuning-fork listing.
    c11,c12,c13,c14,c33,c44=86.74,6.99,11.91,-17.91,107.2,57.94
    C=1e9*np.array([[c11,c12,c13,c14,0,0], [c12,c11,c13,-c14,0,0],
                   [c13,c13,c33,0,0,0], [c14,-c14,0,c44,0,0],
                   [0,0,0,0,c44,c14], [0,0,0,0,c14,(c11-c12)/2]])
    e11,e14=.171,-.0406
    e=np.array([[e11,-e11,0,e14,0,0],[0,0,0,0,-e14,-e11],[0,0,0,0,0,0]])
    eps=np.diag([39.21,39.21,41.03])*1e-12
    return C,e,eps


def energy_audit(volume_A3: float) -> dict:
    C,e,eps=material_tensors()
    E0=1e5*np.array([0,np.cos(np.deg2rad(35.25)),np.sin(np.deg2rad(35.25))])
    def solve(E):
        strain=np.linalg.solve(C,e.T@E)
        D=e@strain+eps@E
        elastic=float(strain@C@strain/2)
        dielectric=float(E@eps@E/2)
        # Recover internal energy through a Legendre transform: U=H+E.D.
        H=float(elastic-E@e@strain-dielectric)
        U=H+float(E@D)
        return strain,D,elastic,dielectric,U
    s,D,Us,Ue,U=solve(E0)
    mechanical_relative=float(np.linalg.norm(C@s-e.T@E0)/np.linalg.norm(e.T@E0))
    ramp=np.linspace(0.,1.,1001)
    Er=ramp[:,None]*E0;Dr=ramp[:,None]*D
    work=float(np.sum((Er[:-1]+Er[1:])/2*(Dr[1:]-Dr[:-1])))
    loop=np.r_[ramp,ramp[-2::-1]]
    El=loop[:,None]*E0;Dl=loop[:,None]*D
    loop_work=float(np.sum((El[:-1]+El[1:])/2*(Dl[1:]-Dl[:-1])))
    sweep=[]
    for scale in (0,.1,1,2,10,-1):
        ss,dd,es,ee,uu=solve(scale*E0)
        sweep.append({'field_scale':scale,'strain':ss.tolist(),'D_C_m2':dd.tolist(),
                      'elastic_J_m3':es,'dielectric_J_m3':ee,'total_J_m3':uu})
    # Coordinate-covariance guard: rotate all tensors, not just the E vector.
    angle=.417
    Q=np.array([[np.cos(angle),-np.sin(angle),0],[np.sin(angle),np.cos(angle),0],[0,0,1]])
    T=np.column_stack([strain_vector(Q@strain_matrix(b)@Q.T) for b in np.eye(6)])
    Ti=np.linalg.inv(T)
    Cr=Ti.T@C@Ti;er=Q@e@Ti;epsr=Q@eps@Q.T
    sr=np.linalg.solve(Cr,er.T@(Q@E0));Dr2=er@sr+epsr@(Q@E0)
    covariance_error=float(np.linalg.norm(sr-T@s)/np.linalg.norm(s))
    field_covariance_error=float(np.linalg.norm(Dr2-Q@D)/np.linalg.norm(D))
    dielectric_relaxed=eps+e@np.linalg.solve(C,e.T)
    eig=np.linalg.eigvalsh(C)
    checks={'stiffness_positive_definite':bool(eig.min()>0),
            'mechanical_balance_relative_error':mechanical_relative,
            'source_work_relative_error':abs(work-U)/U,
            'closed_reversible_cycle_work_J_m3':loop_work,
            'field_reversal_strain_error':float(np.max(abs(solve(-E0)[0]+s))),
            'double_drive_strain_error':float(np.max(abs(solve(2*E0)[0]-2*s))),
            'Z_directed_piezo_strain_norm':float(np.linalg.norm(solve(np.array([0.,0.,1e5]))[0])),
            'coordinate_covariance_relative_error':covariance_error,
            'D_coordinate_covariance_relative_error':field_covariance_error}
    if max(mechanical_relative,covariance_error,field_covariance_error,abs(work-U)/U)>1e-12:
        raise AssertionError('Energy or covariance check failed')
    return {'model':'Independent homogeneous zero-stress linear piezoelectric control; not an atomically resolved field solution.',
            'tensor_convention':'The ANSYS supplied signs/layout are retained; not yet registered to the IUCr atomic basis.',
            'E_V_m':E0.tolist(),'E_magnitude_V_m':float(np.linalg.norm(E0)),
            'strain_order':['xx','yy','zz','2yz','2xz','2xy'],
            'strain':s.tolist(),'D_C_m2':D.tolist(),
            'elastic_energy_J_m3':Us,'dielectric_energy_J_m3':Ue,'stored_energy_J_m3':U,
            'quasistatic_source_work_J_m3':work,'cell_energy_J':U*volume_A3*1e-30,
            'free_vs_clamped_effective_permittivity_ratio':float((E0@dielectric_relaxed@E0)/(E0@eps@E0)),
            'C_Pa':C.tolist(),'e_C_m2':e.tolist(),'epsilon_constant_strain_F_m':eps.tolist(),
            'd_m_V':np.linalg.solve(C,e.T).tolist(),
            'C_eigenvalues_GPa':(eig/1e9).tolist(),'checks':checks,'drive_sweep':sweep}


def dump_csv(path: Path, rows: list[dict]) -> None:
    with path.open('w',newline='',encoding='utf-8') as handle:
        writer=csv.DictWriter(handle,fieldnames=list(rows[0]));writer.writeheader();writer.writerows(rows)


def main() -> None:
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--out',type=Path,default=Path('results'))
    args=parser.parse_args();args.out.mkdir(parents=True,exist_ok=True)
    lattice,frac,labels=structure();volume=float(np.linalg.det(lattice))
    geometry,bridges=geometric_audit(lattice,frac)
    report={'research_date':'2026-09-14','status':'Target-informed construction and consistency checks; NOT ARK validation.',
            'sources':SOURCES,'numpy_version':np.__version__,
            'code_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
            'cell':{'lattice_vectors_A':lattice.tolist(),'volume_A3':volume,
                    'fractional_positions':frac.tolist(),'labels':labels},
            'geometry':geometry,'bridge_rows':bridges,
            'compatibility':compatibility_audit(lattice,frac),
            'energy':energy_audit(volume)}
    (args.out/'results.json').write_text(json.dumps(report,indent=2,allow_nan=False)+'\n',encoding='utf-8')
    dump_csv(args.out/'bridge_geometry.csv',bridges)
    dump_csv(args.out/'atomic_positions.csv',[dict(site=label,fx=p[0],fy=p[1],fz=p[2]) for label,p in zip(labels,frac)])
    print(json.dumps({'volume_A3':volume,'bridges':bridges,'compatibility':report['compatibility'],
                      'energy':{k:v for k,v in report['energy'].items() if k not in ('drive_sweep','C_Pa','e_C_m2','epsilon_constant_strain_F_m','d_m_V')}},indent=2))

if __name__=='__main__':main()
