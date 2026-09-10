#!/usr/bin/env python3
# ============================================================================
# ARK V9.5 — ARTIFACT AUTOPSY (diagnostic only; V9.5 Q3 treated as FAILED)
# ============================================================================
# Curie's protocol: push synthetic curves through each pipeline stage and print
# the radial log-log slope introduced at each transformation. Find the exact
# step where a featureless flat curve becomes a ~10x outward eta rise.
#
#   V(r) -> g_obs -> theta_c -> kappa_c -> Pi -> dS_t -> eta_c
#
# NO tuning. NO new physics. We are locating the operation that manufactures
# the rise, to decide if a null-flat observable can ever fall out.
#
# For each stage X(r) we report:
#   - outer/inner ratio  (median last-third / median first-third)
#   - mean log-log slope  d ln X / d ln r   (the radial trend the stage imposes)
# A flat curve SHOULD give ratio~1, slope~0 at a stage that adds no false trend.
# ============================================================================
import numpy as np
from scipy.integrate import cumulative_trapezoid

C=299_792_458.0; KPC=3.08567758e19; SQRT2=np.sqrt(2.0); EPS=1e-300
r_syn=np.linspace(0.5,30,40)

def theta_flatv(r,g_obs):
    r_last=r[-1]; v2=g_obs[-1]*r_last
    r_ext=np.linspace(r_last*1.001,r_last*50,2000); g_ext=v2/r_ext
    R=np.concatenate([r,r_ext]); G=np.concatenate([g_obs,g_ext])
    cum=cumulative_trapezoid(G,R,initial=0.0); return (cum[-1]-cum)[:len(r)]

def pipeline(r_kpc,vobs_kms):
    r=r_kpc*KPC; v=vobs_kms*1e3
    g_obs=v**2/np.maximum(r,r[0])
    phi=theta_flatv(r,g_obs); theta=np.sqrt(np.maximum(2*phi/C**2,0.0))
    tau=v*SQRT2/C
    kappa=tau/np.maximum(theta,EPS)
    dtheta=np.gradient(theta,r); flux=r**2*kappa*dtheta
    div=np.gradient(flux,r)/np.maximum(r**2,EPS)
    Pi=-div; chi=tau/np.maximum(kappa,EPS); dSt=Pi/np.maximum(chi,EPS)
    eta=tau/np.maximum(np.abs(dSt),EPS)
    return dict(v=np.abs(v),g_obs=np.abs(g_obs),theta=np.abs(theta),tau=np.abs(tau),
                kappa=np.abs(kappa),flux=np.abs(flux),div=np.abs(div),
                Pi=np.abs(Pi),dSt=np.abs(dSt),eta=np.abs(eta),r=r)

def stage_stats(X,r,trim=2):
    N=len(X); a,b=(trim,N-trim) if N-2*trim>=6 else (0,N)
    XX=np.maximum(X[a:b],EPS); rr=r[a:b]
    inner=np.median(XX[:max(1,len(XX)//3)]); outer=np.median(XX[-max(1,len(XX)//3):])
    ratio=outer/max(inner,EPS)
    slope=np.polyfit(np.log(rr),np.log(XX),1)[0]
    return ratio,slope

curves={'flat':150*np.ones_like(r_syn),
        'kepler':150*np.sqrt(3.0/np.maximum(r_syn,0.3)),
        'solid_then_flat':np.where(r_syn<3.0,150*r_syn/3.0,150.0)}

stages=['v','g_obs','theta','tau','kappa','flux','div','Pi','dSt','eta']
for cname,v in curves.items():
    P=pipeline(r_syn,v)
    print(f"\n{'='*64}\nCURVE: {cname}\n{'='*64}")
    print(f"  {'stage':<8} {'outer/inner':>13} {'d ln X/d ln r':>15}   note")
    prev_ratio=1.0
    for st in stages:
        ratio,slope=stage_stats(P[st],P['r'])
        jump=ratio/max(prev_ratio,EPS)
        flag=''
        if abs(np.log(max(jump,EPS)))>np.log(2.0):
            flag='  <== big change introduced HERE'
        print(f"  {st:<8} {ratio:>13.3f} {slope:>15.3f}{flag}")
        prev_ratio=ratio
print(f"\n{'#'*64}")
print("READ: the stage whose outer/inner ratio first departs strongly from ~1")
print("(and the >2x jump flag) is where the false rise enters. That localizes")
print("the artifact: geometry (g_obs/flux r^2), boundary (theta), the balance")
print("inversion (Pi=-div), or the viscosity denominator (eta=tau/dSt).")
print(f"{'#'*64}")
