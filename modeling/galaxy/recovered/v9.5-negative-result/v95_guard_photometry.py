#!/usr/bin/env python3
# ============================================================================
# ARK V9.5 — Artifact Guard + Sealed Photometry Cross-Check
# ============================================================================
# Curie's protocol, exact order:
#   PART A (artifact guard): run the SAME eta-shape solver on synthetic toy
#     curves (flat, Keplerian, solid-body, exponential-disk). If eta_hat rises
#     ~10x outward even on featureless curves, Q3 is partly a math artifact.
#   PART B (sealed photometry): freeze eta-transition from V_obs ONLY, THEN
#     unseal SBdisk/Vdisk and test whether eta-transition predicts baryonic
#     concentration BETTER THAN a dumb radius-only null (fixed fraction of r_max).
#
# The question is NOT "does it look close" — it's "does eta-transition beat the
# null predictor." If not, Q3 doesn't know where the baryons are.
#
# Photometry (SBdisk/Vdisk/Vgas/Vbul) is touched ONLY in Part B, AFTER freeze.
# ============================================================================
import numpy as np
from pathlib import Path
from scipy.integrate import cumulative_trapezoid
from scipy import stats
import pickle

C=299_792_458.0; KPC=3.08567758e19; SQRT2=np.sqrt(2.0); EPS=1e-300
ROT=Path('sparc'); N_MIN=15

# ---------- the SAME reconstruction used in v95_relax (verbatim core) ----------
def theta_flatv(r,g_obs):
    r_last=r[-1]; v_last2=g_obs[-1]*r_last
    r_ext=np.linspace(r_last*1.001,r_last*50,2000); g_ext=v_last2/r_ext
    R=np.concatenate([r,r_ext]); G=np.concatenate([g_obs,g_ext])
    cum=cumulative_trapezoid(G,R,initial=0.0); phi=(cum[-1]-cum)[:len(r)]
    return np.sqrt(np.maximum(2*phi/C**2,0.0))

def eta_hat_from_v(r_kpc, vobs_kms):
    r=r_kpc*KPC; v=vobs_kms*1e3; N=len(r)
    g_obs=v**2/np.maximum(r,r[0])
    theta=theta_flatv(r,g_obs); tau=v*SQRT2/C
    kappa=tau/np.maximum(theta,EPS)
    dtheta=np.gradient(theta,r); flux=r**2*kappa*dtheta
    div=np.gradient(flux,r)/np.maximum(r**2,EPS)
    Pi=-div; chi=tau/np.maximum(kappa,EPS); dSt=Pi/np.maximum(chi,EPS)
    eta=tau/np.maximum(np.abs(dSt),EPS)
    return eta/np.maximum(np.median(eta),EPS)

def transition_and_ratio(r_kpc, eta_hat, trim=2):
    N=len(eta_hat); a,b=(trim,N-trim) if N-2*trim>=5 else (0,N)
    rr=r_kpc[a:b]; eh=eta_hat[a:b]
    leh=np.log(np.maximum(eh,EPS)); lrr=np.log(np.maximum(rr,EPS))
    slope=np.gradient(leh,lrr); itr=int(np.argmax(np.abs(slope)))
    ei=np.median(eh[:max(1,len(eh)//3)]); eo=np.median(eh[-max(1,len(eh)//3):])
    return rr[itr], eo/max(ei,EPS)

# ============================= PART A: ARTIFACT GUARD =========================
print("="*70); print("PART A — SYNTHETIC NULL CURVES (artifact guard)"); print("="*70)
r_syn=np.linspace(0.5,30,40)   # kpc, generic well-sampled grid
def make(kind, vflat=150.0, rs=3.0):
    if kind=='flat':         v=vflat*np.ones_like(r_syn)
    elif kind=='kepler':     v=vflat*np.sqrt(rs/np.maximum(r_syn,0.3))   # v~r^-1/2
    elif kind=='solid_then_flat':
        v=np.where(r_syn<rs, vflat*r_syn/rs, vflat)
    elif kind=='exp_disk':   # rises then gently declines, exponential-disk-ish
        v=vflat*np.sqrt(1-np.exp(-r_syn/rs))*(1+0.0*r_syn)
    return v
print(f"  {'curve':<18} {'eta_outer/inner':>16} {'r_trans[kpc]':>14}")
syn_ratios={}
for kind in ['flat','kepler','solid_then_flat','exp_disk']:
    v=make(kind); eh=eta_hat_from_v(r_syn,v)
    rt,ratio=transition_and_ratio(r_syn,eh)
    syn_ratios[kind]=ratio
    print(f"  {kind:<18} {ratio:>16.2f} {rt:>14.2f}")
print("  INTERPRETATION:")
print("   - if ALL synthetics show ~10x outer rise => Q3 ratio is largely a math")
print("     artifact of the reconstruction (flat-ish v -> eta rises by construction).")
print("   - if synthetics rise much LESS than SPARC's ~10x median, the SPARC excess")
print("     carries real structure beyond the generic flat-curve baseline.")

# ============================= PART B: SEALED PHOTOMETRY ======================
print("\n"+"="*70); print("PART B — SEALED PHOTOMETRY CROSS-CHECK"); print("="*70)

def parse(name):
    fp=ROT/f'{name}_rotmod.dat'; rows=[]
    for line in fp.read_text(errors='replace').splitlines():
        s=line.strip()
        if not s or s.startswith('#'): continue
        p=s.split()
        if len(p)>=6:
            try: vv=[float(x) for x in p[:8]]
            except: continue
            while len(vv)<8: vv.append(0.0)
            rows.append(vv)
    a=np.asarray(rows,float)
    if a.ndim<2 or len(a)<3: return None
    return dict(name=name, r=a[:,0], vobs=a[:,1], errv=a[:,2],
                vgas=a[:,3], vdisk=a[:,4], vbul=a[:,5], sbdisk=a[:,6], sbbul=a[:,7])

# STEP 1: FREEZE eta-transition from V_obs ONLY (no photometry touched)
frozen=[]
for fp in sorted(ROT.glob('*_rotmod.dat')):
    nm=fp.name.replace('_rotmod.dat','')
    g=parse(nm)
    if g is None or len(g['r'])<N_MIN: continue
    eh=eta_hat_from_v(g['r'], g['vobs'])
    rt,ratio=transition_and_ratio(g['r'], eh)
    frozen.append(dict(name=nm, r_trans=rt, ratio=ratio, r_max=g['r'][-1], g=g))
print(f"  froze eta-transition for {len(frozen)} well-sampled galaxies (V_obs only)")

# STEP 2: NOW unseal photometry. Baryonic concentration proxy:
#   baryonic "scale" = radius enclosing half the baryonic rotational support,
#   computed from Vdisk/Vgas/Vbul (the photometric mass model in velocity units).
def baryon_half_radius(g):
    r=g['r']; vb2=np.abs(g['vgas'])*g['vgas']+0.5*np.abs(g['vdisk'])*g['vdisk']+0.7*np.abs(g['vbul'])*g['vbul']
    vb2=np.maximum(vb2,0.0)
    # proxy baryonic "mass profile" ~ integral vb2 dr (monotone); half-point radius
    M=cumulative_trapezoid(vb2,r,initial=0.0)
    if M[-1]<=0: return np.nan
    half=0.5*M[-1]; idx=int(np.searchsorted(M,half))
    idx=min(max(idx,0),len(r)-1)
    return r[idx]
# also: radius of peak baryonic rotational contribution
def baryon_peak_radius(g):
    r=g['r']; vb=np.sqrt(np.maximum(np.abs(g['vgas'])*g['vgas']+0.5*np.abs(g['vdisk'])*g['vdisk']+0.7*np.abs(g['vbul'])*g['vbul'],0.0))
    if np.all(vb<=0): return np.nan
    return r[int(np.argmax(vb))]

for a in frozen:
    a['r_bar_half']=baryon_half_radius(a['g'])
    a['r_bar_peak']=baryon_peak_radius(a['g'])

rt=np.array([a['r_trans'] for a in frozen])
rbh=np.array([a['r_bar_half'] for a in frozen])
rmax=np.array([a['r_max'] for a in frozen])
m=np.isfinite(rt)&np.isfinite(rbh)
rt,rbh,rmax=rt[m],rbh[m],rmax[m]

# STEP 3: does eta-transition predict baryon scale BETTER than radius-only null?
# Null predictor: fixed fraction of r_max (the "dumb" predictor).
print(f"\n  --- eta-transition vs baryonic half-support radius (n={m.sum()}) ---")
r_eta,p_eta=stats.pearsonr(rt,rbh)
print(f"  corr(eta_transition, r_bar_half)      = {r_eta:+.3f}  (p={p_eta:.2e})")
# null: r_max as predictor of r_bar_half
r_null,p_null=stats.pearsonr(rmax,rbh)
print(f"  corr(r_max [NULL],    r_bar_half)      = {r_null:+.3f}  (p={p_null:.2e})")
# does eta_transition add info beyond r_max? partial corr
def partial(x,y,z):
    X=np.column_stack([np.ones_like(z),z])
    bx=np.linalg.lstsq(X,x,rcond=None)[0]; by=np.linalg.lstsq(X,y,rcond=None)[0]
    rx=x-X@bx; ry=y-X@by; return stats.pearsonr(rx,ry)
r_part,p_part=partial(rt,rbh,rmax)
print(f"  partial corr(eta_trans, r_bar_half | r_max) = {r_part:+.3f}  (p={p_part:.2e})")
print("  KEY: if eta_transition correlates with baryon scale AND adds info beyond")
print("       r_max (partial != 0), then eta-transition genuinely 'knows' baryon")
print("       structure. If partial ~ 0, it's just tracking overall galaxy size.")

# context: how big is the SPARC outer/inner ratio vs the synthetic baseline?
sparc_ratio=np.array([a['ratio'] for a in frozen]); sparc_ratio=sparc_ratio[np.isfinite(sparc_ratio)]
print(f"\n  SPARC outer/inner eta median = {np.median(sparc_ratio):.2f}")
print(f"  synthetic flat-curve baseline = {syn_ratios['flat']:.2f}")
print(f"  -> SPARC/synthetic excess factor = {np.median(sparc_ratio)/max(syn_ratios['flat'],EPS):.2f}")
print(f"     (>1 means SPARC carries structure beyond the generic flat-curve artifact)")

print(f"\n{'#'*68}")
print("VERDICT LOGIC:")
print(" - Part A tells us how much of the 10x is reconstruction artifact.")
print(" - Part B tells us whether eta-transition beats a dumb radius null at")
print("   locating baryons. Only if BOTH favor physics is Q3 publishable-adjacent.")
print(f"{'#'*68}")
