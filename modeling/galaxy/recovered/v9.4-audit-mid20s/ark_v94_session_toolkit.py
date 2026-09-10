#!/usr/bin/env python3
"""
ARK V9.4 Session Toolkit — 2026-07-03/04 night-shift session
============================================================
Consolidates every analysis routine used in the session (record:
v94_sb_correction_record.md, Steps 1-13) into one documented module.

REQUIRES: ark_v94_scalar_geom.py (the V9.4 solver, user's bundle) on path,
and the SPARC rotmod files in a directory. numpy/scipy/pandas.

PROVENANCE: SPARC 2016 (Lelli, McGaugh, Schombert). Master table mirror
verified MD5 6181df386bfc05868a3700c196e800da == Zenodo record 16284118.

CANONICAL CHAIN (velocity-pure predictor):
    mixed_slope projector + global Y-recal (YD=0.475, YB=0.35)
    -> 24.36 km/s OOS on 175 galaxies, zero per-galaxy freedom.
TERMINOLOGY: the comparison target is the "N-BARYON expectation" — the
Newtonian circular-velocity composition of SPARC photometry (audit P1).
It is NOT a raw measurement; Newton enters via component superposition.
"""
import numpy as np
import importlib.util, sys
from pathlib import Path
from scipy.integrate import cumulative_trapezoid
from scipy.ndimage import gaussian_filter1d
from scipy.optimize import brentq

C = 299_792_458.0
KPC = 3.08567758e19
EPS = 1e-30
YD, YB = 0.475, 0.35          # session-calibrated global M/L (fold-stable 5/5)
GDAG = 1.2e-10                # MLS16 RAR scale (for the benchmark ONLY)

def load_ark(path="ark_v94_scalar_geom.py"):
    """Import the V9.4 solver module from a file path."""
    spec = importlib.util.spec_from_file_location("ark", path)
    ark = importlib.util.module_from_spec(spec)
    sys.modules["ark"] = ark
    spec.loader.exec_module(ark)
    return ark

def nbaryon_target(gal, Yd=YD, Yb=YB):
    """N-baryon expectation (P1: Newtonian composition — ledgered)."""
    vg, vd, vb = gal.v_gas_kms, gal.v_disk_kms, gal.v_bul_kms
    return np.sqrt(np.maximum(np.abs(vg)*vg + Yd*np.abs(vd)*vd
                              + Yb*np.abs(vb)*vb, 0.0))

def solve_boundary(ark, gal, ext_factor=20.0, tail_exp=2.0):
    """mixed_slope inverse solve with PARAMETERIZED exterior ('the glass').
    tail_exp=2.0 Keplerian (V9.4 default; carries Newtonian-vacuum prior P2),
    tail_exp=1.0 = flat-v continuation (XXV §10.6 framework prediction;
    scores 60.3 vs 24.4 against the N-baryon target — unresolved tension).
    Returns v_pred (km/s) or None."""
    r = np.asarray(gal.r_kpc, float)*KPC
    v = np.asarray(gal.v_obs_kms, float)*1e3
    N = len(r)
    if N < 3 or not np.all(np.isfinite(r)) or not np.all(np.isfinite(v)):
        return None
    g = v**2/np.maximum(r, r[0])
    re = np.linspace(r[-1]*1.01, ext_factor*r[-1], 400)
    R = np.concatenate([r, re])
    G = np.concatenate([g, g[-1]*(r[-1]/re)**tail_exp])
    cum = cumulative_trapezoid(G, R, initial=0.0)
    phi = cum[-1] - cum
    tf = np.sqrt(np.maximum(2*phi/C**2, 0)); th = tf[:N]
    bs = max(3, int(2*np.median(np.diff(R[:N]))/np.median(np.diff(R))))
    Vf = np.concatenate([v, v[-1]*np.ones(len(re))])
    tauf = np.maximum(ark.adaptive_smooth(Vf*np.sqrt(2)/C, R, N, bs), EPS)
    kf = np.maximum(gaussian_filter1d(tauf/np.maximum(tf, EPS),
                                      sigma=max(2, bs//2)), EPS)
    dtf = np.gradient(tf, R)
    base = np.abs(kf[:N]*dtf[:N])
    flux = R**2*kf*dtf
    div = (np.gradient(flux, R)/np.maximum(R**2, 1e-300))[:N]
    rr = np.asarray(gal.r_kpc)*KPC
    chi = np.clip(0.5*(ark.safe_log_slope(th, rr)
                       + ark.safe_log_slope(kf[:N], rr)), 0, 1)
    F = ark.smooth_projector(1/(2+2*chi), sigma=max(1, bs//4))
    integ = base + F*rr*np.abs(div)
    ci = cumulative_trapezoid(integ, rr, initial=0.0)
    tb = np.maximum(ci[-1]-ci, EPS)
    gb = C**2*tb*np.abs(np.gradient(tb, rr))
    return np.sqrt(np.maximum(rr*gb, 0))/1e3

def fit_epsilon_g(ark, gal, te_grid=np.arange(1.2, 3.21, 0.1)):
    """Per-galaxy diagnostic boundary parameter (Step 5). eps_g = best
    tail exponent minus 2.0, chi2-weighted. DIAGNOSTIC ONLY — audited in
    Steps 5-6: dominant axis is internal (SB); envelope reading FALSIFIED
    (sign reversal vs HI extent); partly absorbs inclination/truncation
    systematics. Do not treat as identified physics."""
    vm = nbaryon_target(gal)
    ev = np.maximum(gal.err_v_kms, 0.5)
    best = (np.inf, None)
    for te in te_grid:
        vp = solve_boundary(ark, gal, 20.0, te)
        if vp is None:
            return None
        m = (vm > 1) & (vp > 1) & np.isfinite(vm) & np.isfinite(vp)
        if m.sum() < 3:
            continue
        c2 = np.mean((((vp-vm)/ev)[m])**2)
        if c2 < best[0]:
            best = (c2, te)
    return None if best[1] is None else best[1]-2.0

def rar_inversion_vbar(gal):
    """Benchmark competitor (Step: ARK-vs-RAR race): invert the MLS16 RAR
    point-wise to predict v_bar from v_obs. ARK beat this 24.6 vs 31.2
    globally (nonlocal information advantage), while losing 64% of
    galaxies head-to-head (dwarf regime)."""
    r = np.asarray(gal.r_kpc)*KPC
    vo = np.asarray(gal.v_obs_kms)*1e3
    gobs = vo**2/np.maximum(r, r[0])
    out = []
    for gg, ri in zip(gobs, r):
        f = lambda gb: gb/(1-np.exp(-np.sqrt(gb/GDAG))) - gg
        try:
            out.append(np.sqrt(brentq(f, gg*1e-4, gg)*ri)/1e3)
        except ValueError:
            out.append(np.nan)
    return np.array(out)

def metrics(vp, vm, ev):
    """Session-standard scoring: RMS (km/s) and reduced chi2 vs errV.
    Noise floor ~8.2 km/s raw (median errV 4.6; realistic floor 8-12
    after target-side error propagation). chi2=1 is the instrument
    match criterion; canonical chain sits ~54-74 (weighting-dependent)."""
    m = (vm > 1) & (vp > 1) & np.isfinite(vm) & np.isfinite(vp)
    res = (vp-vm)[m]
    return (np.sqrt(np.mean(res**2)),
            np.mean((res/np.maximum(ev[m], 0.5))**2))

def exceedance_scan(gal, Yd=YD, Yb=YB, nsig=3.0):
    """Superposition-failure points (Steps 10-11): N-baryon exceeds v_obs
    beyond nsig*errV. Measured: 29/3108 pts, dose-response in LOCAL surface
    density (zero below ~logSB 1.3, ramp to 4.8% in densest decile),
    survives fixed-radius stratification (density effect, not radius).
    Fork A2 (kappa = k0(1+rho/rho_c)) reproduces the shape on synthetics."""
    vm = nbaryon_target(gal, Yd, Yb)
    vo = np.asarray(gal.v_obs_kms)
    ev = np.maximum(gal.err_v_kms, 0.5)
    sb = np.asarray(gal.sb_disk) + np.asarray(gal.sb_bul)
    m = (vm > 1) & np.isfinite(vm) & np.isfinite(vo) & (sb > 0)
    return (vm > vo + nsig*ev) & m, np.where(m, np.log10(np.maximum(sb, EPS)), np.nan)

def y_recal_scan(ark, gals, grid_d=np.arange(0.30,0.75,0.025),
                 grid_b=np.arange(0.20,0.80,0.05)):
    """Joint global (Y_disk, Y_bul) scan. Session result: (0.475, 0.35),
    identical in all 5 galaxy-level CV folds; OOS RMS 24.360 (from 30.550).
    Killed the f_bul residual axis (-0.43 -> +0.006). FLAG: Y_bul=0.35 is
    half the SPARC convention — may absorb a projector systematic; also
    halves inner exceedances (entangled with stretch signal, Step 7-add)."""
    sols = {g.name: ark.solve(g,'mixed_slope') for g in gals}
    def rms(Yd,Yb):
        sq=n=0
        for g in gals:
            s=sols[g.name]
            if s is None: continue
            vp=s['v_pred_kms']; vm=nbaryon_target(g,Yd,Yb)
            m=(vm>1)&(vp>1)&np.isfinite(vm)&np.isfinite(vp)
            if m.sum()<3: continue
            sq+=np.sum((vp-vm)[m]**2); n+=m.sum()
        return np.sqrt(sq/n)
    return min(((rms(a,b),a,b) for a in grid_d for b in grid_b))

class ForkA2:
    """DERIVED (Step 13, firewall-compliant): kappa = k0(1 + rho/rho_c),
    leading analytic term of XXIV running, 'energy density' = MATTER
    density. R = 1 + rho/rho_c. Exterior Newtonian by Gauss (solar system
    safe BY STRUCTURE). Harness: T1/T3/T4 PASS, T2 FAIL (recorded, F3 —
    deep regime needs its own axiom; see next-session target).
    Claim class: derived-form + one-calibrated-scale (rho_c: calibrate
    ONCE from the measured density turn-on; NEVER per galaxy).
    Fork A1 (gradient-energy running, kappa=k0/(1-y^2), hard ceiling g_c)
    was FALSIFIED by solar-system ephemerides — do not reopen."""
    def __init__(self, rho_c): self.rho_c = rho_c
    def g(self, r, rho, G=1.0):
        M = cumulative_trapezoid(4*np.pi*r**2*rho, r, initial=0.0)
        g_N = G*M/np.maximum(r, r[0])**2
        return g_N/(1.0 + rho/self.rho_c)

# ------------------------------------------------------------- provenance
PROVENANCE = {
 "SPARC rotmods": "user upload SPARC_175_rotmod.zip (Lelli+2016 SPARC)",
 "V9.4 solver":   "user upload ark_v94_scalar_geom_bundle.zip; re-run "
                  "reproduced all 6 projector RMS to <1e-9 (bit-exact)",
 "SPARC Table1":  "github.com/amidou/amiga-xmatch mirror, 2026-07-04; "
                  "MD5 6181df386bfc05868a3700c196e800da == Zenodo 16284118",
 "V9.5 files":    "user upload (autopsy, guards, viscosity, relax, record) "
                  "— eta route CLOSED, R-tilde parked, eps_bulk parked",
}

if __name__ == "__main__":
    print(__doc__)
    print("Provenance:")
    for k,v in PROVENANCE.items(): print(f"  {k}: {v}")

# Audit protocol constants (Steps 5-6): split seed for discovery/confirmation
AUDIT_SPLIT_SEED = 20260703
# Firewall protocol: see record Step 12. Harness: forward_harness.py.
# Fork A2 candidate + derivation: record Step 13.
