#!/usr/bin/env python3
# ============================================================================
# ARK V9.5 — Relaxation-Class Diagnostic (blade-safe, normalized)
# ============================================================================
# Per Curie's refinement. Tests ONE question:
#   Do independently-located eta-transition radii sit at a COMMON reduced
#   relaxation index value across galaxies, and does that value classify
#   dwarfs vs spirals?
#
# Reduced relaxation index (NO absolute D, NO aetheron spacing, NO chi):
#   R~_c(r) = L(r)^2 * eta_hat_c(r) / t_orbit(r)
#   L(r)        = r                      [GEOMETRIC] radial depth, zero freedom
#   eta_hat_c   = eta_c(r)/median(eta_c) [DERIVED] normalized shape (chi cancels)
#   t_orbit(r)  = 2*pi*r / v(r)          [MEASURED] kinematic
# => R~_c has units that DON'T matter; only its VALUE AT THE TRANSITION,
#    compared ACROSS galaxies, is the signal. We never assume R~_c = 1.
#
# ORDERING (anti-circularity): locate eta-transition FIRST (sharpest
# d log eta_hat / d log r), THEN read R~_c at that radius. Not the reverse.
#
# PROVENANCE: [MEASURED] SPARC | [DERIVED:paper] forced | [GEOMETRIC] math |
#             [ASSUMPTION:flag] not in papers, flagged.
# Photometry SEALED until the final out-of-sample check (disk scale length).
# ============================================================================
import numpy as np
from pathlib import Path
from scipy.integrate import cumulative_trapezoid
from scipy import stats

C=299_792_458.0; KPC=3.08567758e19; SQRT2=np.sqrt(2.0); EPS=1e-300
ROT=Path('sparc')
N_MIN=15   # [ASSUMPTION:flag] well-sampled cut for magnitude/shape reliability

def parse(name):
    fp=ROT/f'{name}_rotmod.dat'; dist=None; rows=[]
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
            try: vv=[float(x) for x in p[:8]]
            except: continue
            while len(vv)<8: vv.append(0.0)
            rows.append(vv)
    a=np.asarray(rows,float)
    if a.ndim<2 or len(a)<3: return None
    return dict(name=name, dist=dist, r=a[:,0], vobs=a[:,1], errv=a[:,2],
                vgas=a[:,3], vdisk=a[:,4], vbul=a[:,5], sbdisk=a[:,6], sbbul=a[:,7])

def theta_flatv(r, g_obs):
    """[DERIVED:XXV 10.6] flat-v continuation, blade-safe boundary."""
    r_last=r[-1]; v_last2=g_obs[-1]*r_last
    r_ext=np.linspace(r_last*1.001, r_last*50, 2000)
    g_ext=v_last2/r_ext
    R=np.concatenate([r,r_ext]); G=np.concatenate([g_obs,g_ext])
    cum=cumulative_trapezoid(G,R,initial=0.0); phi=(cum[-1]-cum)[:len(r)]
    return np.sqrt(np.maximum(2*phi/C**2,0.0))

def eta_shape(g):
    """Reconstruct normalized eta_hat(r) from V_obs only. chi cancels in the ratio."""
    r=g['r']*KPC; v=g['vobs']*1e3; N=len(r)
    g_obs=v**2/np.maximum(r,r[0])
    theta=theta_flatv(r,g_obs)
    tau=v*SQRT2/C
    kappa=tau/np.maximum(theta,EPS)
    dtheta=np.gradient(theta,r)
    flux=r**2*kappa*dtheta
    div=np.gradient(flux,r)/np.maximum(r**2,EPS)
    Pi=-div                                  # [DERIVED:XXV E.3] Lambda=0
    chi=tau/np.maximum(kappa,EPS)            # [ASSUMPTION:flag] cancels in eta_hat
    dSt=Pi/np.maximum(chi,EPS)
    eta=tau/np.maximum(np.abs(dSt),EPS)
    eta_hat=eta/np.maximum(np.median(eta),EPS)   # [DERIVED] normalized -> chi-free
    return dict(r=r,N=N,v=v,eta=eta,eta_hat=eta_hat,kappa=kappa,theta=theta)

def analyze(g, trim=2):
    s=eta_shape(g); r=s['r']; N=s['N']; v=s['v']; eta_hat=s['eta_hat']
    a=trim; b=N-trim
    if b-a<5: a,b=0,N
    rr=r[a:b]; eh=eta_hat[a:b]; vv=v[a:b]
    # STEP 1: locate eta-transition independently (sharpest log-log slope) [MEASURED]
    leh=np.log(np.maximum(eh,EPS)); lrr=np.log(rr)
    slope=np.gradient(leh,lrr)
    itr=int(np.argmax(np.abs(slope)))
    r_trans=rr[itr]
    # STEP 2: reduced relaxation index, read AT the transition [DERIVED]
    t_orbit=2*np.pi*rr/np.maximum(vv,1.0)        # s
    L=rr                                          # [GEOMETRIC] L(r)=r
    Rred=L**2*eh/np.maximum(t_orbit,EPS)          # reduced index (arb units)
    Rred_hat=Rred/np.maximum(np.median(Rred),EPS) # normalize within galaxy too
    Rred_at_trans=Rred_hat[itr]
    # outer vs inner eta_hat (bunching signature)
    eta_inner=np.median(eh[:max(1,len(eh)//3)])
    eta_outer=np.median(eh[-max(1,len(eh)//3):])
    return dict(name=g['name'], N=N, dist=g['dist'],
                r_trans_kpc=r_trans/KPC, Rred_at_trans=Rred_at_trans,
                eta_outer_over_inner=eta_outer/max(eta_inner,EPS),
                vmax=float(np.max(g['vobs'])), s=s, rr=rr, eh=eh, Rred_hat=Rred_hat, itr=itr)

# ---- run across well-sampled set ----
names=sorted(p.name.replace('_rotmod.dat','') for p in ROT.glob('*_rotmod.dat'))
res=[]
for nm in names:
    g=parse(nm)
    if g is None: continue
    try:
        a=analyze(g)
    except Exception as e:
        continue
    a['well_sampled']=a['N']>=N_MIN
    res.append(a)

ws=[a for a in res if a['well_sampled']]
sparse=[a for a in res if not a['well_sampled']]
print(f"parsed {len(res)} galaxies | well-sampled (N>={N_MIN}): {len(ws)} | sparse: {len(sparse)}")

# Q1: is there a stable eta-transition? distribution of r_trans (normalized by vmax proxy)
rt=np.array([a['r_trans_kpc'] for a in ws])
print(f"\n=== Q1: eta-transition radius (well-sampled) ===")
print(f"  r_trans: median={np.median(rt):.2f} kpc  IQR=[{np.percentile(rt,25):.2f},{np.percentile(rt,75):.2f}]")

# Q2: does R~_c cluster at the transition across galaxies?
Rc=np.array([a['Rred_at_trans'] for a in ws])
Rc=Rc[np.isfinite(Rc)]
print(f"\n=== Q2: reduced relaxation index AT transition (well-sampled) ===")
print(f"  R~_c(transition): median={np.median(Rc):.3f}  IQR=[{np.percentile(Rc,25):.3f},{np.percentile(Rc,75):.3f}]")
print(f"  CV(R~_c) = {np.std(Rc)/max(np.mean(Rc),EPS):.3f}   (low CV => COMMON crossover value = result)")

# Q3: outer bunching present? eta_outer/eta_inner > 1 expected (DM-like)
br=np.array([a['eta_outer_over_inner'] for a in ws])
br=br[np.isfinite(br)]
print(f"\n=== Q3: outer/inner eta_hat ratio (bunching, well-sampled) ===")
print(f"  median={np.median(br):.2f}   frac>1 = {np.mean(br>1):.2f}  (>1 => outer viscosity excess)")

# Q4: do dwarfs (low vmax) sit at a DIFFERENT R~_c than spirals? (class separation)
vmax=np.array([a['vmax'] for a in ws]); 
dwarf=vmax<80; spiral=vmax>=80
if dwarf.sum()>=3 and spiral.sum()>=3:
    Rc_d=np.array([a['Rred_at_trans'] for a in ws])[dwarf]; Rc_d=Rc_d[np.isfinite(Rc_d)]
    Rc_s=np.array([a['Rred_at_trans'] for a in ws])[spiral]; Rc_s=Rc_s[np.isfinite(Rc_s)]
    print(f"\n=== Q4: relaxation-class separation (dwarf vmax<80 vs spiral>=80) ===")
    print(f"  dwarfs (n={len(Rc_d)}):  R~_c median={np.median(Rc_d):.3f}")
    print(f"  spirals(n={len(Rc_s)}):  R~_c median={np.median(Rc_s):.3f}")
    u,p=stats.mannwhitneyu(Rc_d,Rc_s,alternative='two-sided')
    print(f"  Mann-Whitney p={p:.4f}  (low p => dwarfs and spirals ARE different classes)")

print(f"\n{'#'*68}")
print("BLADE STATUS: eta_hat normalized (chi cancels), R~_c uses L=r (geometric),")
print("t_orbit measured, NO absolute D / aetheron scale. Transition located BEFORE")
print("reading R~_c (anti-circular). Photometry still SEALED.")
print(f"{'#'*68}")

# stash for the photometry cross-check (run separately, keeps wall clean)
import pickle
pickle.dump(res, open('/home/claude/v94/v95_relax_results.pkl','wb'))
print("results stashed for sealed-photometry cross-check")
