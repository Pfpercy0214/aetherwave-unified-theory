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

C      = 299_792_458.0      # [DERIVED:physical const] speed of light, m/s
KPC    = 3.08567758e19      # [GEOMETRIC] kpc -> m
HBAR   = 1.054571817e-34    # [DERIVED:physical const] J s  (for aetheron-scale check only)
SQRT2  = np.sqrt(2.0)       # [DERIVED:XXV virial/unit-audit bridge tau=v*sqrt2/c]
EPS    = 1e-300
ROT    = Path('sparc')

# ----------------------------------------------------------------------------
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

# ----------------------------------------------------------------------------
def reconstruct(r_kpc, vobs_kms):
    """
    Reconstruct theta_c, tau_c, kappa_c from V_obs ONLY.
    Returns fields on the OBSERVED radial grid (no outward tail).
    """
    r = r_kpc*KPC; v = vobs_kms*1e3; N=len(r)
    # [MEASURED->DERIVED] kinematic acceleration g_obs = v^2/r  (XXV 10.1)
    g_obs = v**2/np.maximum(r, r[0])

    # theta_c from the gravitational potential (XXV 10.2 / A.1: theta^2 = 2 phi/c^2).
    # phi reconstructed by integrating g_obs. BOUNDARY TREATMENT below is the one
    # place a choice lives -- handled in solve() via three audited variants.
    return dict(r=r, N=N, v=v, g_obs=g_obs)

def theta_from_phi(r, g_obs, boundary):
    """
    theta_c(r) from integrating g_obs.  'boundary' selects how phi is anchored
    beyond the last observed point -- the audited choice.
      'edge_zero'  : [ASSUMPTION:flag] phi(r_last)=0. Physically false (potential
                     does not vanish at data edge) and causes theta->0, kappa->inf
                     at the edge. Included ONLY to show the artifact. DO NOT USE.
      'edge_slope' : [ASSUMPTION:flag] continue g_obs past r_last using the
                     MEASURED local log-slope of g_obs (data-derived, not imposed
                     1/r^2). Mild extrapolation; flagged.
      'flat_v'     : [DERIVED:XXV 10.6] outer curve is flat (v->const), the
                     framework's OWN prediction; continue with v=const => g~1/r,
                     integrate the tail analytically. This is the blade-safe one
                     because the continuation is what the theory predicts, not a
                     free choice.
    """
    N=len(r); r_last=r[-1]
    if boundary=='edge_zero':
        cum=cumulative_trapezoid(g_obs,r,initial=0.0); phi=cum[-1]-cum
    elif boundary=='edge_slope':
        # measured local slope of log g_obs over last few points
        k=max(3,N//8); lg=np.log(np.maximum(g_obs[-k:],EPS)); lr=np.log(r[-k:])
        slope=np.polyfit(lr,lg,1)[0]                      # [MEASURED] data falloff exponent
        r_ext=np.linspace(r_last*1.001, r_last*50, 2000)
        g_ext=g_obs[-1]*(r_ext/r_last)**slope
        R=np.concatenate([r,r_ext]); G=np.concatenate([g_obs,g_ext])
        cum=cumulative_trapezoid(G,R,initial=0.0); phi_full=cum[-1]-cum; phi=phi_full[:N]
    elif boundary=='flat_v':
        # [DERIVED:XXV 10.6] flat rotation => v=v_last const => g_obs = v_last^2/r
        # tail integral_{r_last}^inf v^2/r' dr' diverges (log) so anchor at large R*
        # with the SAME flat law; the framework predicts flatness, so this is its
        # own statement, not an inserted tail shape.
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
    """
    Recursive balance solve.  With Lambda=0 (use_U=False):
        Pi(r) = -div(kappa_c grad theta_c)          [DERIVED:XXV E.3 / Curie 'solve Pi directly']
    Then recover entropy pressure and viscosity:
        dS_t  = Pi / chi_c                            [DERIVED:XXIV linear conjugate]
        eta_c = tau_c / dS_t                          [DERIVED:XIX  eta=tau/dS]
    chi_c is the PDE-normalization scaling. Curie: linear, fixed by units. We use
    the PDE's own entropy-term normalization chi_c = (tau_c/kappa_c) so that Pi maps
    back through the SAME coefficient the governing equation assigns to the entropy
    term [DERIVED:XXV D.1 RHS (tau_c/kappa_c) d(dS_t)/dt]. This is NOT a free constant;
    it is read off the reconstructed tau_c,kappa_c. Flagged for audit anyway.
    """
    rec=reconstruct(g['r'], g['vobs']); r=rec['r']; N=rec['N']; v=rec['v']
    theta=theta_from_phi(r, rec['g_obs'], boundary)
    tau  = v*SQRT2/C                                  # [DERIVED:XXV bridge]  RAW
    kappa= tau/np.maximum(theta,EPS)                  # [DERIVED:XXV kappa=tau/theta]

    # spatial operator div(kappa grad theta) in SPHERICAL measure
    # [GEOMETRIC] (disk vs sphere audited separately; start spherical = isotropic substrat)
    dtheta=np.gradient(theta,r)
    flux  = r**2 * kappa * dtheta                     # [GEOMETRIC] r^2 weighting
    div   = np.gradient(flux,r)/np.maximum(r**2,EPS)  # div(kappa grad theta)

    U_term=np.zeros(N)
    if use_U:
        # [ASSUMPTION:flag] minimal nonlinear U forced by XXV E.3 constraints
        # (bounded, admits localized minima, restoring near equilibrium). The
        # SIMPLEST such form with NO extra shape freedom is U = (1/2) m(theta-theta0)^2
        # with theta0 the local equilibrium -> dU/dtheta = m(theta-theta0). But m and
        # theta0 are not pinned by velocity alone => this branch CARRIES FREEDOM and is
        # reported separately, never as the primary result.
        U_term=np.zeros(N)  # placeholder; only run if Lambda=0 fails

    Pi = U_term - div                                 # [DERIVED:XXV E.3] with Lambda=0 -> Pi=-div

    # map Pi -> dS_t -> eta_c
    chi = tau/np.maximum(kappa,EPS)                   # [DERIVED:XXV D.1 normalization] flagged
    dSt = Pi/np.maximum(chi,EPS)                      # entropy pressure (quasi-static stored form)
    eta = tau/np.maximum(np.abs(dSt),EPS)             # [DERIVED:XIX] substrat viscosity

    # aetheron coherence length as CONSISTENCY CHECK only (not used in decomposition)
    d_aeth = HBAR/np.maximum(eta*C,EPS)               # [DERIVED:XIX d~hbar/(eta c)]

    return dict(name=g['name'], r=r, N=N, theta=theta, tau=tau, kappa=kappa,
                div=div, Pi=Pi, chi=chi, dSt=dSt, eta=eta, d_aeth=d_aeth,
                g_obs=rec['g_obs'], boundary=boundary)

# ----------------------------------------------------------------------------
def describe_eta(s, edge_trim=2):
    """
    Read the bunched/stretched decomposition off the SHAPE of eta_c(r).
    No chosen scale: we report plateau / transition / monotonicity as MEASURED
    features. edge_trim drops the last/first points where finite-diff + any
    boundary residual is least reliable [ASSUMPTION:flag small].
    """
    r=s['r']/KPC; eta=s['eta']; N=s['N']
    a=edge_trim; b=N-edge_trim
    if b-a<4: a,b=0,N
    rr=r[a:b]; ee=eta[a:b]
    le=np.log(np.maximum(ee,EPS))
    # local log-slope of eta vs r: where it changes character
    slope=np.gradient(le,rr)
    # transition radius = where |d(log eta)/dr| is maximal (sharpest change) [MEASURED]
    itr=int(np.argmax(np.abs(slope)))
    # plateau detection: longest run where |slope| < 0.3 * max|slope| [ASSUMPTION:flag thresh]
    thr=0.3*np.max(np.abs(slope))
    flat=np.abs(slope)<thr
    return dict(r_trans=rr[itr], eta_min=ee.min(), eta_max=ee.max(),
                eta_med=float(np.median(ee)), frac_flat=float(flat.mean()),
                slope_max=float(np.max(np.abs(slope))), rr=rr, ee=ee, slope=slope)

# ----------------------------------------------------------------------------
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
    # boundary-artifact guard: check last-point kappa isn't exploding
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
