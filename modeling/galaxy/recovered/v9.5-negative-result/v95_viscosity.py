#!/usr/bin/env python3
# ============================================================================
# ARK V9.5  —  Recursive Viscosity / Displacement-Flow Solver  (feasibility)
# ============================================================================
# CONCEPT (from the XXV / XXIV / XIX discussion, Paul + Curie + Theia):
#   A galaxy is modeled NOT as a static mass distribution but as a ROTATING
#   DISPLACEMENT FLOW.  V_obs(r) is the boundary condition.  The governing
#   balance PDE then determines every other scalar relative to it (recursive
#   fixed point): the entropy pressure Pi, hence dS_t, hence the substrat
#   viscosity eta_c = tau_c / dS_t falls out.  The bunched(DM-like) vs
#   stretched(DE-like) decomposition is read off the SHAPE of eta_c(r) with
#   no chosen scale.
#
# PROVENANCE TAGS (Paul's rule: anything not formally in the papers is flagged):
#   [MEASURED]            : taken directly from SPARC rotmod files
#   [DERIVED:src]         : forced by a relation stated in the named paper
#   [GEOMETRIC]           : pure math/geometry factor (pi, r^2, finite diff)
#   [ASSUMPTION:flag]     : NOT in the papers; a numerical/modeling choice.
#                           Must be justified or removed. Never shapes a claim
#                           silently.
#
# NO PHOTOMETRY enters the predictor. Vgas/Vdisk/Vbul/SBdisk are SEALED and
# used ONLY at the end as an independent answer-key comparison.
# NO FITTED CONSTANTS. Bridges used: tau=v*sqrt2/c, theta from observed g_obs.
# ============================================================================
import numpy as np
from pathlib import Path
from scipy.integrate import cumulative_trapezoid
import json

C      = 299_792_458.0
KPC    = 3.08567758e19
HBAR   = 1.054571817e-34
SQRT2  = np.sqrt(2.0)
EPS    = 1e-300
ROT    = Path('sparc')

def parse(name):
    """[MEASURED] read rotmod: r[kpc], Vobs, errV, Vgas, Vdisk, Vbul, SBdisk, SBbul"""
    fp = ROT / f'{name}_rotmod.dat'; dist=None; rows=[]
    for line in fp.read_text(errors='replace').splitlines():
        s=line.strip()
        if not s: continue
        if s.startswith('#'):
            if 'Distance' in s and '=' in s:
                try: dist=float(s.split('=',1)[1].split()[0])
                except: pass
            continue
        p=s.split()
        if len(p)>=6:
            try: v=[float(x) for x in p[:8]]
            except: continue
            while len(v)<8: v.append(0.0)
            rows.append(v)
    a=np.asarray(rows,float)
    return dict(name=name, dist=dist, r=a[:,0], vobs=a[:,1], errv=a[:,2],
                vgas=a[:,3], vdisk=a[:,4], vbul=a[:,5], sbdisk=a[:,6], sbbul=a[:,7])

def reconstruct(r_kpc, vobs_kms):
    r = r_kpc*KPC; v = vobs_kms*1e3; N=len(r)
    g_obs = v**2/np.maximum(r, r[0])
    return dict(r=r, N=N, v=v, g_obs=g_obs)

def theta_from_phi(r, g_obs, boundary):
    N=len(r); r_last=r[-1]
    if boundary=='edge_zero':
        cum=cumulative_trapezoid(g_obs,r,initial=0.0); phi=cum[-1]-cum
    elif boundary=='edge_slope':
        k=max(3,N//8); lg=np.log(np.maximum(g_obs[-k:],EPS)); lr=np.log(r[-k:])
        slope=np.polyfit(lr,lg,1)[0]
        r_ext=np.linspace(r_last*1.001, r_last*50, 2000)
        g_ext=g_obs[-1]*(r_ext/r_last)**slope
        R=np.concatenate([r,r_ext]); G=np.concatenate([g_obs,g_ext])
        cum=cumulative_trapezoid(G,R,initial=0.0); phi_full=cum[-1]-cum; phi=phi_full[:N]
    elif boundary=='flat_v':
        v_last2=g_obs[-1]*r_last
        r_ext=np.linspace(r_last*1.001, r_last*50, 2000)
        g_ext=v_last2/r_ext
        R=np.concatenate([r,r_ext]); G=np.concatenate([g_obs,g_ext])
        cum=cumulative_trapezoid(G,R,initial=0.0); phi_full=cum[-1]-cum; phi=phi_full[:N]
    else:
        raise ValueError(boundary)
    theta=np.sqrt(np.maximum(2*phi/C**2,0.0))
    return theta

def solve(g, boundary='flat_v', use_U=False):
    rec=reconstruct(g['r'], g['vobs']); r=rec['r']; N=rec['N']; v=rec['v']
    theta=theta_from_phi(r, rec['g_obs'], boundary)
    tau  = v*SQRT2/C
    kappa= tau/np.maximum(theta,EPS)
    dtheta=np.gradient(theta,r)
    flux  = r**2 * kappa * dtheta
    div   = np.gradient(flux,r)/np.maximum(r**2,EPS)
    U_term=np.zeros(N)
    if use_U:
        U_term=np.zeros(N)
    Pi = U_term - div
    chi = tau/np.maximum(kappa,EPS)
    dSt = Pi/np.maximum(chi,EPS)
    eta = tau/np.maximum(np.abs(dSt),EPS)
    d_aeth = HBAR/np.maximum(eta*C,EPS)
    return dict(name=g['name'], r=r, N=N, theta=theta, tau=tau, kappa=kappa,
                div=div, Pi=Pi, chi=chi, dSt=dSt, eta=eta, d_aeth=d_aeth,
                g_obs=rec['g_obs'], boundary=boundary)

def describe_eta(s, edge_trim=2):
    r=s['r']/KPC; eta=s['eta']; N=s['N']
    a=edge_trim; b=N-edge_trim
    if b-a<4: a,b=0,N
    rr=r[a:b]; ee=eta[a:b]
    le=np.log(np.maximum(ee,EPS))
    slope=np.gradient(le,rr)
    itr=int(np.argmax(np.abs(slope)))
    thr=0.3*np.max(np.abs(slope))
    flat=np.abs(slope)<thr
    return dict(r_trans=rr[itr], eta_min=ee.min(), eta_max=ee.max(),
                eta_med=float(np.median(ee)), frac_flat=float(flat.mean()),
                slope_max=float(np.max(np.abs(slope))), rr=rr, ee=ee, slope=slope)

def run(name, boundary='flat_v'):
    g=parse(name); s=solve(g, boundary=boundary, use_U=False)
    d=describe_eta(s)
    rkpc=s['r']/KPC
    print(f"\n{'='*70}\n{name}  [Lambda=0, boundary={boundary}]  D={g['dist']}Mpc  N={s['N']}")
    print(f"{'='*70}")
    print(f"  eta_c(r): min={d['eta_min']:.3e}  med={d['eta_med']:.3e}  max={d['eta_max']:.3e}")
    print(f"  sharpest eta transition at r = {d['r_trans']:.2f} kpc   frac_flat={d['frac_flat']:.2f}")
    print(f"  {'r[kpc]':>8} {'Vobs':>7} {'kappa':>9} {'Pi':>11} {'dS_t':>11} {'eta_c':>11} {'d_aeth[m]':>11}")
    step=max(1,s['N']//12)
    for i in range(0,s['N'],step):
        print(f"  {rkpc[i]:8.2f} {g['vobs'][i]:7.1f} {s['kappa'][i]:9.3f} "
              f"{s['Pi'][i]:11.3e} {s['dSt'][i]:11.3e} {s['eta'][i]:11.3e} {s['d_aeth'][i]:11.3e}")
    if s['kappa'][-1] > 50*np.median(s['kappa'][:-1]):
        print(f"  [WARN] kappa edge blow-up detected ({s['kappa'][-1]:.2e}) -> boundary artifact")
    return s,d

if __name__=='__main__':
    for nm in ['NGC3198','CamB']:
        for bnd in ['flat_v','edge_slope','edge_zero']:
            run(nm, boundary=bnd)
    print(f"\n{'#'*70}")
    print("READOUT: eta_c(r) shape is the decomposition. Stable plateau=coherent band;")
    print("sharp transition=condensed/bulk boundary (DATA-set, not chosen); the three")
    print("boundary variants show how much the result depends on the edge treatment.")
    print("flat_v is blade-safe (XXV 10.6 prediction); edge_zero shown only to expose")
    print("the artifact. If flat_v and edge_slope agree, the edge isn't driving it.")
    print(f"{'#'*70}")
