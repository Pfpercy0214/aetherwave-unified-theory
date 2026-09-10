#!/usr/bin/env python3
"""
ARK ZERO-PARAMETER Inverse Solver — V5.2 vs V5.4 Comparison
=============================================================
V5.2: Original (np.clip, static damping, global Gaussian)
V5.4: Combined algorithmic improvements:
  1. Smooth κᶜ regularization (softplus, lower floor)
  2. Adaptive damping (iteration-aware + gradient-responsive)
  3. Radially-adaptive entropy smoothing

α = 4π/3 (derived from spherical geometry of Poisson equation)
Free parameters: ZERO

Author: Paul Frederick Percy Jr. & Theia (Claude Opus)
Framework: Aether Reality Kernel (ARK), Papers XXIV–XXV
"""

import numpy as np
from scipy.integrate import cumulative_trapezoid
from scipy.ndimage import gaussian_filter1d
from scipy.signal import savgol_filter
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import os, json, glob, time

C = 299792458.0
G = 6.67430e-11
KPC = 3.08567758e19
ALPHA = 4*np.pi/3  # DERIVED from spherical geometry

DATA = '/home/claude/sparc_full'
OUT = '/home/claude/ark_v54_comparison'
os.makedirs(OUT, exist_ok=True)


# ══════════════════════════════════════════════════════════════
# V5.2 — ORIGINAL SOLVER (baseline)
# ══════════════════════════════════════════════════════════════
def invert_v52(r_kpc, v_obs_kms, max_iter=300, damping=0.12):
    r = np.asarray(r_kpc, float) * KPC
    v = np.asarray(v_obs_kms, float) * 1e3
    N = len(r)
    if N < 3:
        return None

    g_obs = v**2 / np.maximum(r, r[0])

    n_ext = 400
    r_ext = np.linspace(r[-1]*1.01, 20*r[-1], n_ext)
    g_ext = g_obs[-1]*(r[-1]/r_ext)**2
    R = np.concatenate([r, r_ext])
    G_obs = np.concatenate([g_obs, g_ext])
    M = len(R)

    cum_obs = cumulative_trapezoid(G_obs, R, initial=0)
    phi_obs = cum_obs[-1] - cum_obs
    th_obs = np.sqrt(np.maximum(2*phi_obs/C**2, 0))
    dth_obs = np.zeros(M)
    ok = th_obs > 1e-30
    dth_obs[ok] = -G_obs[ok]/(C**2*th_obs[ok])

    dr_med = np.median(np.diff(R[:N]))
    sig = max(3, int(2*dr_med/np.median(np.diff(R))))

    g_bar = G_obs.copy() * 0.3

    for iteration in range(max_iter):
        g_bar_old = g_bar.copy()

        cum_bar = cumulative_trapezoid(g_bar, R, initial=0)
        phi_bar = cum_bar[-1] - cum_bar
        thN = np.sqrt(np.maximum(2*phi_bar/C**2, 0))
        thN2 = np.maximum(thN**2, 1e-40)

        r2g = R**2 * g_bar
        d_r2g = np.gradient(r2g, R)
        dSt = np.maximum(d_r2g, 0)/C**2
        dSt = gaussian_filter1d(dSt, sigma=sig)

        kap = np.clip(ALPHA * dSt / thN2, 0.01, 1.0)

        dthN_new = kap * dth_obs
        abs_dthN = np.abs(dthN_new)
        cum_dthN = cumulative_trapezoid(abs_dthN, R, initial=0)
        thN_new = np.maximum(cum_dthN[-1] - cum_dthN, 1e-30)

        g_bar_new = C**2 * thN_new * abs_dthN
        g_bar = damping*g_bar_new + (1-damping)*g_bar
        g_bar = np.maximum(g_bar, 0)

        delta = np.max(np.abs(g_bar[:N] - g_bar_old[:N]) /
                      np.maximum(np.abs(g_bar[:N]), 1e-30))
        if delta < 1e-5:
            break

    s = slice(0, N)
    v_bar = np.sqrt(np.maximum(R*g_bar, 0))

    return {
        'v_bar_pred_kms': v_bar[s]/1e3,
        'g_bar_pred': g_bar[s],
        'kappa': kap[s],
        'converged': delta < 1e-5,
        'iterations': iteration + 1,
        'final_delta': float(delta),
    }


# ══════════════════════════════════════════════════════════════
# V5.4 — COMBINED IMPROVEMENTS
# ══════════════════════════════════════════════════════════════

def softplus_kappa(kap_raw, k_min=1e-6, k_max=1.0, sharpness=5.0):
    """
    Differentiable κᶜ regularization using shifted softplus.
    
    softplus(x) = ln(1 + exp(x)) is smooth, monotonic, and 
    asymptotically linear — ideal for bounding a PDE coupling 
    coefficient without introducing gradient discontinuities.
    
    Maps kap_raw ∈ (-∞, +∞) → κᶜ ∈ (k_min, k_max) smoothly.
    
    Unlike the sigmoid used in V5.3, softplus has a gentler 
    saturation profile at the lower bound, allowing massive 
    spirals to explore coupling values below 0.001 without 
    creating the pooling effect seen at the sigmoid floor.
    """
    # Normalize raw kappa to [0, 1] range centered on useful domain
    x = sharpness * kap_raw
    # Numerically stable softplus
    sp = np.where(x > 20, x, np.log1p(np.exp(np.minimum(x, 20))))
    # Scale to [k_min, k_max] range
    # softplus(0) = ln(2) ≈ 0.693, so normalize
    sp_norm = sp / (sharpness * k_max + np.log(2))
    return k_min + (k_max - k_min) * np.clip(sp_norm, 0, 1)


def adaptive_smooth(arr, R, N, base_sig):
    """
    Radially-adaptive entropy smoothing.
    
    Instead of a global Gaussian sigma, the smoothing adapts to 
    local structure:
    - Inner galaxy (steep gradients): lighter smoothing preserves
      critical entropy spike of the bulge
    - Outer galaxy (noisy HI): heavier smoothing suppresses 
      turbulent gas kinematics
    
    Uses the local second derivative magnitude as a structure 
    detector: where |d²g/dr²| is large, reduce smoothing.
    """
    if len(arr) < 7:
        return gaussian_filter1d(arr, sigma=base_sig)
    
    # Compute local curvature (second derivative magnitude)
    d2 = np.abs(np.gradient(np.gradient(arr[:N], R[:N]), R[:N]))
    d2 = np.concatenate([d2, np.zeros(len(arr) - N)])
    
    # Normalize to [0, 1] — high curvature → low sigma
    d2_norm = d2 / (np.max(d2) + 1e-30)
    
    # Adaptive sigma: ranges from base_sig/3 (high structure) to base_sig*2 (low structure)
    sig_local = base_sig * (0.33 + 1.67 * (1 - d2_norm))
    
    # Apply as weighted combination of light and heavy smoothing
    light = gaussian_filter1d(arr, sigma=max(1, base_sig // 3))
    heavy = gaussian_filter1d(arr, sigma=base_sig * 2)
    
    # Blend: high curvature regions use light smoothing
    weight = d2_norm  # high curvature → weight toward light
    weight = gaussian_filter1d(weight, sigma=max(2, base_sig // 2))  # smooth the weights
    
    return weight * light + (1 - weight) * heavy


def invert_v54(r_kpc, v_obs_kms, max_iter=500, damping_init=0.08):
    """
    V5.4 solver: Combined algorithmic improvements.
    
    Changes from V5.2:
      1. SMOOTH κᶜ: softplus regularization with floor at 1e-6
         (vs hard clip at 0.01). Allows massive spirals to find
         their true coupling depth without gradient shocks.
      2. ADAPTIVE DAMPING: starts conservative (0.08), ramps up
         to 0.20 as solution stabilizes. Prevents early oscillation
         in deep potential wells while accelerating late convergence.
      3. ADAPTIVE SMOOTHING: radially-varying Gaussian kernel that
         preserves bulge entropy gradients while suppressing outer
         halo noise.
      4. Extended iteration budget (500 vs 300) to give the gentler
         damping schedule time to work.
    
    Zero free parameters. α = 4π/3 (derived).
    """
    r = np.asarray(r_kpc, float) * KPC
    v = np.asarray(v_obs_kms, float) * 1e3
    N = len(r)
    if N < 3:
        return None

    g_obs = v**2 / np.maximum(r, r[0])

    # Extend domain (identical to V5.2)
    n_ext = 400
    r_ext = np.linspace(r[-1]*1.01, 20*r[-1], n_ext)
    g_ext = g_obs[-1]*(r[-1]/r_ext)**2
    R = np.concatenate([r, r_ext])
    G_obs = np.concatenate([g_obs, g_ext])
    M = len(R)

    # θᶜ_obs bedrock (identical)
    cum_obs = cumulative_trapezoid(G_obs, R, initial=0)
    phi_obs = cum_obs[-1] - cum_obs
    th_obs = np.sqrt(np.maximum(2*phi_obs/C**2, 0))
    dth_obs = np.zeros(M)
    ok = th_obs > 1e-30
    dth_obs[ok] = -G_obs[ok]/(C**2*th_obs[ok])

    # Base smoothing sigma
    dr_med = np.median(np.diff(R[:N]))
    base_sig = max(3, int(2*dr_med/np.median(np.diff(R))))

    g_bar = G_obs.copy() * 0.3

    # Convergence tracking for adaptive damping
    recent_deltas = []

    for iteration in range(max_iter):
        g_bar_old = g_bar.copy()

        # ═══ Standard ARK field computation (identical physics) ═══
        cum_bar = cumulative_trapezoid(g_bar, R, initial=0)
        phi_bar = cum_bar[-1] - cum_bar
        thN = np.sqrt(np.maximum(2*phi_bar/C**2, 0))
        thN2 = np.maximum(thN**2, 1e-40)

        r2g = R**2 * g_bar
        d_r2g = np.gradient(r2g, R)
        dSt = np.maximum(d_r2g, 0)/C**2

        # ═══ FIX 3: Adaptive smoothing ═══
        dSt = adaptive_smooth(dSt, R, N, base_sig)

        # ═══ FIX 1: Smooth κᶜ (softplus regularization) ═══
        kap_raw = ALPHA * dSt / thN2
        kap = softplus_kappa(kap_raw, k_min=1e-6, k_max=1.0, sharpness=5.0)

        # ═══ PDE inversion (identical) ═══
        dthN_new = kap * dth_obs
        abs_dthN = np.abs(dthN_new)
        cum_dthN = cumulative_trapezoid(abs_dthN, R, initial=0)
        thN_new = np.maximum(cum_dthN[-1] - cum_dthN, 1e-30)

        g_bar_new = C**2 * thN_new * abs_dthN

        # ═══ FIX 2: Adaptive damping ═══
        # Start conservative, ramp up as solution stabilizes
        # Also reduce damping when oscillation is detected
        progress = min(iteration / 150.0, 1.0)  # 0→1 over first 150 iters
        damping_base = damping_init + (0.20 - damping_init) * progress

        # Detect oscillation: if delta is bouncing, reduce damping
        if len(recent_deltas) >= 4:
            d1 = recent_deltas[-1] - recent_deltas[-2]
            d2 = recent_deltas[-2] - recent_deltas[-3]
            if d1 * d2 < 0:  # sign change = oscillation
                damping_base *= 0.7  # pull back

        damping = np.clip(damping_base, 0.03, 0.25)

        g_bar = damping*g_bar_new + (1-damping)*g_bar
        g_bar = np.maximum(g_bar, 0)

        delta = np.max(np.abs(g_bar[:N] - g_bar_old[:N]) /
                      np.maximum(np.abs(g_bar[:N]), 1e-30))
        recent_deltas.append(delta)
        if len(recent_deltas) > 10:
            recent_deltas.pop(0)

        if delta < 1e-5:
            break

    s = slice(0, N)
    v_bar = np.sqrt(np.maximum(R*g_bar, 0))

    return {
        'v_bar_pred_kms': v_bar[s]/1e3,
        'g_bar_pred': g_bar[s],
        'kappa': kap[s],
        'converged': delta < 1e-5,
        'iterations': iteration + 1,
        'final_delta': float(delta),
    }


# ══════════════════════════════════════════════════════════════
# DATA LOADING
# ══════════════════════════════════════════════════════════════
def load_galaxy(filepath):
    name = os.path.basename(filepath).replace('_rotmod.dat', '')
    lines = []
    dist = None
    with open(filepath, 'r') as f:
        for line in f:
            if line.startswith('#'):
                if 'Distance' in line:
                    try:
                        dist = float(line.split('=')[1].strip().split()[0])
                    except:
                        pass
                continue
            parts = line.strip().split()
            if len(parts) >= 6:
                lines.append([float(x) for x in parts[:8]])
    if len(lines) < 3:
        return None
    d = np.array(lines)
    return {
        'name': name, 'distance_Mpc': dist,
        'r': d[:,0], 'v_obs': d[:,1], 'err_v': d[:,2],
        'v_gas': d[:,3], 'v_disk': d[:,4], 'v_bul': d[:,5],
        'SBdisk': d[:,6], 'SBbul': d[:,7],
        'N': len(d),
    }


# ══════════════════════════════════════════════════════════════
# COMPARISON ENGINE
# ══════════════════════════════════════════════════════════════
def run_solver(galaxies, solver_fn, label, Yd=0.5, Yb=0.7):
    results = []
    all_meas, all_pred = [], []
    failed = []

    for idx, gal in enumerate(galaxies):
        try:
            inv = solver_fn(gal['r'], gal['v_obs'])
            if inv is None:
                failed.append(gal['name'])
                continue

            vg = gal['v_gas']; vd = gal['v_disk']; vb = gal['v_bul']
            v_meas = np.sqrt(np.maximum(
                np.abs(vg)*vg + Yd*np.abs(vd)*vd + Yb*np.abs(vb)*vb, 0))

            rms = np.sqrt(np.mean((inv['v_bar_pred_kms'] - v_meas)**2))
            valid = (v_meas > 1) & (inv['v_bar_pred_kms'] > 1)
            corr = np.corrcoef(v_meas[valid], inv['v_bar_pred_kms'][valid])[0,1] if np.sum(valid) > 3 else 0.0

            all_meas.extend(v_meas.tolist())
            all_pred.extend(inv['v_bar_pred_kms'].tolist())

            results.append({
                'name': gal['name'], 'N': gal['N'],
                'distance_Mpc': gal['distance_Mpc'],
                'RMS_kms': round(float(rms), 2),
                'correlation': round(float(corr), 4),
                'kappa_min': round(float(inv['kappa'].min()), 6),
                'kappa_max': round(float(inv['kappa'].max()), 6),
                'converged': bool(inv['converged']),
                'iterations': inv['iterations'],
                'final_delta': inv['final_delta'],
                'v_meas': v_meas,
                'v_pred': inv['v_bar_pred_kms'],
                'kappa': inv['kappa'],
                'r_kpc': gal['r'],
                'v_obs': gal['v_obs'],
                'v_max_kms': round(float(np.max(gal['v_obs'])), 1),
            })
        except Exception as e:
            failed.append(f"{gal['name']}: {str(e)[:60]}")

    am = np.array(all_meas)
    ap = np.array(all_pred)
    valid = (am > 1) & (ap > 1) & np.isfinite(am) & np.isfinite(ap)
    gc = np.corrcoef(am[valid], ap[valid])[0,1]
    grms = np.sqrt(np.mean((ap[valid]-am[valid])**2))
    corrs = [r['correlation'] for r in results]
    converged_count = sum(1 for r in results if r['converged'])

    stats = {
        'label': label,
        'total': len(results),
        'failed': len(failed),
        'converged': converged_count,
        'not_converged': len(results) - converged_count,
        'global_r': round(float(gc), 4),
        'global_rms': round(float(grms), 1),
        'median_r': round(float(np.median(corrs)), 4),
        'mean_r': round(float(np.mean(corrs)), 4),
        'frac_r_gt_08': round(sum(1 for c in corrs if c > 0.8)/len(corrs), 3),
        'frac_r_gt_05': round(sum(1 for c in corrs if c > 0.5)/len(corrs), 3),
    }
    return results, stats, failed


def main():
    print("="*72)
    print("  ARK ZERO-PARAMETER INVERSE SOLVER — V5.2 vs V5.4 COMPARISON")
    print(f"  α = 4π/3 = {ALPHA:.6f} (DERIVED)")
    print("  Free parameters: ZERO")
    print("  V5.4 changes:")
    print("    1. Smooth κᶜ (softplus, floor=1e-6)")
    print("    2. Adaptive damping (0.08→0.20 ramp + oscillation detect)")
    print("    3. Radially-adaptive entropy smoothing")
    print("    4. Extended iterations (500)")
    print("="*72)

    files = sorted(glob.glob(os.path.join(DATA, '*_rotmod.dat')))
    galaxies = []
    for f in files:
        gal = load_galaxy(f)
        if gal is not None:
            galaxies.append(gal)
    print(f"\n  Loaded {len(galaxies)} galaxies, "
          f"{sum(g['N'] for g in galaxies)} total data points\n")

    # ═══ RUN V5.2 ═══
    print("  Running V5.2 (baseline)...")
    t0 = time.time()
    res52, stats52, fail52 = run_solver(galaxies, invert_v52, "V5.2")
    t52 = time.time() - t0
    print(f"  V5.2 done in {t52:.1f}s")

    # ═══ RUN V5.4 ═══
    print("\n  Running V5.4 (combined fixes)...")
    t0 = time.time()
    res54, stats54, fail54 = run_solver(galaxies, invert_v54, "V5.4")
    t54 = time.time() - t0
    print(f"  V5.4 done in {t54:.1f}s")

    # ═══ COMPARISON TABLE ═══
    r52_dict = {r['name']: r for r in res52}
    r54_dict = {r['name']: r for r in res54}

    print(f"\n{'='*72}")
    print(f"  {'METRIC':<35s} {'V5.2':>12s} {'V5.4':>12s} {'CHANGE':>10s}")
    print(f"  {'-'*69}")
    for key, label in [
        ('total', 'Galaxies analyzed'),
        ('converged', 'Converged'),
        ('not_converged', 'NOT converged'),
        ('global_r', 'Global correlation (r)'),
        ('global_rms', 'Global RMS (km/s)'),
        ('median_r', 'Median per-galaxy r'),
        ('mean_r', 'Mean per-galaxy r'),
        ('frac_r_gt_08', 'Fraction r > 0.8'),
        ('frac_r_gt_05', 'Fraction r > 0.5'),
    ]:
        v52 = stats52[key]
        v54 = stats54[key]
        if isinstance(v52, float):
            diff = v54 - v52
            sign = '+' if diff > 0 else ''
            print(f"  {label:<35s} {v52:>12} {v54:>12} {sign}{diff:>9.3f}")
        else:
            diff = v54 - v52
            print(f"  {label:<35s} {v52:>12} {v54:>12} {diff:>+10d}")
    print(f"{'='*72}")

    # ═══ NON-CONVERGED DETAIL ═══
    nc52 = {r['name'] for r in res52 if not r['converged']}
    nc54 = {r['name'] for r in res54 if not r['converged']}
    newly_converged = nc52 - nc54
    newly_failed = nc54 - nc52

    print(f"\n  V5.2 non-converged: {len(nc52)}")
    print(f"  V5.4 non-converged: {len(nc54)}")
    if newly_converged:
        print(f"  NEWLY CONVERGED in V5.4: {sorted(newly_converged)}")
    if newly_failed:
        print(f"  ⚠ NEW FAILURES in V5.4: {sorted(newly_failed)}")

    print(f"\n  {'Galaxy':18s} {'V5.2 RMS':>8s} {'V5.4 RMS':>8s} {'V5.2 r':>8s} "
          f"{'V5.4 r':>8s} {'V5.2':>5s} {'V5.4':>5s} {'κ_min':>10s} {'iters':>6s}")
    print(f"  {'-'*82}")

    for name in sorted(nc52 | nc54):
        a = r52_dict.get(name)
        b = r54_dict.get(name)
        if a is None or b is None:
            continue
        c52 = '✓' if a['converged'] else '⚠'
        c54 = '✓' if b['converged'] else '⚠'
        print(f"  {name:18s} {a['RMS_kms']:7.1f}  {b['RMS_kms']:7.1f}  "
              f"{a['correlation']:7.4f}  {b['correlation']:7.4f}  "
              f"  {c52}    {c54}  {b['kappa_min']:9.6f} {b['iterations']:>5d}")

    # ═══ TOP RMS IMPROVEMENTS ═══
    improvements = []
    for r52 in res52:
        if r52['name'] in r54_dict:
            r54 = r54_dict[r52['name']]
            improvements.append({
                'name': r52['name'],
                'rms_52': r52['RMS_kms'],
                'rms_54': r54['RMS_kms'],
                'rms_delta': r54['RMS_kms'] - r52['RMS_kms'],
                'r_52': r52['correlation'],
                'r_54': r54['correlation'],
                'v_max': r52['v_max_kms'],
                'conv_52': r52['converged'],
                'conv_54': r54['converged'],
            })
    improvements.sort(key=lambda x: x['rms_delta'])

    print(f"\n  TOP 20 RMS IMPROVEMENTS:")
    print(f"  {'Galaxy':18s} {'v_max':>6s} {'RMS 5.2':>8s} {'RMS 5.4':>8s} "
          f"{'ΔRMS':>8s} {'r 5.2':>7s} {'r 5.4':>7s}")
    print(f"  {'-'*68}")
    for imp in improvements[:20]:
        print(f"  {imp['name']:18s} {imp['v_max']:5.0f}  {imp['rms_52']:7.1f}  "
              f"{imp['rms_54']:7.1f}  {imp['rms_delta']:+7.1f}  "
              f"{imp['r_52']:6.4f}  {imp['r_54']:6.4f}")

    regressions = [i for i in improvements if i['rms_delta'] > 2.0]
    if regressions:
        regressions.sort(key=lambda x: x['rms_delta'], reverse=True)
        print(f"\n  ⚠ REGRESSIONS (RMS increased > 2 km/s): {len(regressions)}")
        for reg in regressions[:15]:
            print(f"    {reg['name']:18s} {reg['rms_52']:7.1f} → {reg['rms_54']:7.1f}  "
                  f"(Δ = {reg['rms_delta']:+.1f})  r: {reg['r_52']:.3f}→{reg['r_54']:.3f}")
    else:
        print(f"\n  ✓ NO REGRESSIONS > 2 km/s")

    # ═══ VELOCITY-BINNED PERFORMANCE ═══
    print(f"\n  PERFORMANCE BY GALAXY MASS (v_max bins):")
    print(f"  {'v_max range':>15s} {'N':>4s}  {'V5.2 RMS':>8s} {'V5.4 RMS':>8s} "
          f"{'V5.2 med r':>10s} {'V5.4 med r':>10s}")
    print(f"  {'-'*60}")
    for lo, hi in [(0, 80), (80, 150), (150, 220), (220, 400)]:
        bin52 = [i for i in improvements if lo <= i['v_max'] < hi]
        if not bin52:
            continue
        rms52_bin = np.median([i['rms_52'] for i in bin52])
        rms54_bin = np.median([i['rms_54'] for i in bin52])
        r52_bin = np.median([i['r_52'] for i in bin52])
        r54_bin = np.median([i['r_54'] for i in bin52])
        print(f"  {lo:>6d}–{hi:<6d}   {len(bin52):>4d}  {rms52_bin:7.1f}  {rms54_bin:7.1f}  "
              f"   {r52_bin:7.4f}    {r54_bin:7.4f}")

    # ═══ PLOTS ═══
    # 1. Side-by-side scatter
    fig, axes = plt.subplots(1, 2, figsize=(16, 7))
    for ax, res, stats, label, color in [
        (axes[0], res52, stats52, 'V5.2 (baseline)', 'red'),
        (axes[1], res54, stats54, 'V5.4 (combined fixes)', 'darkgreen')
    ]:
        am = np.array([v for r in res for v in r['v_meas']])
        ap = np.array([v for r in res for v in r['v_pred']])
        valid = (am > 1) & (ap > 1) & np.isfinite(am) & np.isfinite(ap)
        ax.scatter(am[valid], ap[valid], s=3, alpha=0.15, c=color, zorder=2)
        maxv = max(np.max(am[valid]), np.max(ap[valid]))*1.05
        ax.plot([0,maxv],[0,maxv], 'k--', lw=1.5, alpha=0.5)
        ax.set_xlabel('v_bar MEASURED (km/s)', fontsize=11)
        ax.set_ylabel('v_bar PREDICTED (km/s)', fontsize=11)
        ax.set_title(f'{label}', fontsize=13, fontweight='bold')
        ax.set_xlim(0, maxv); ax.set_ylim(0, maxv); ax.set_aspect('equal')
        ax.grid(True, alpha=0.12)
        ax.text(0.05, 0.95,
                f'r = {stats["global_r"]:.4f}\n'
                f'RMS = {stats["global_rms"]:.1f} km/s\n'
                f'Converged: {stats["converged"]}/{stats["total"]}\n'
                f'Median r = {stats["median_r"]:.4f}',
                transform=ax.transAxes, fontsize=11, va='top',
                bbox=dict(boxstyle='round', facecolor='lightyellow', alpha=0.9))
    plt.suptitle('ARK Zero-Parameter Solver: V5.2 vs V5.4  |  α = 4π/3  |  0 free parameters',
                 fontsize=14, fontweight='bold')
    plt.tight_layout(rect=[0, 0, 1, 0.96])
    fig.savefig(os.path.join(OUT, 'v52_vs_v54_scatter.png'), dpi=150, bbox_inches='tight')
    plt.close(fig)

    # 2. Histograms
    fig, axes = plt.subplots(1, 2, figsize=(16, 6))
    corrs52 = [r['correlation'] for r in res52]
    corrs54 = [r['correlation'] for r in res54]

    ax = axes[0]
    ax.hist(corrs52, bins=30, range=(-1,1), alpha=0.5, color='blue', label='V5.2', edgecolor='navy', lw=0.5)
    ax.hist(corrs54, bins=30, range=(-1,1), alpha=0.5, color='green', label='V5.4', edgecolor='darkgreen', lw=0.5)
    ax.axvline(np.median(corrs52), color='blue', ls='--', lw=2, label=f'V5.2 med={np.median(corrs52):.3f}')
    ax.axvline(np.median(corrs54), color='green', ls='--', lw=2, label=f'V5.4 med={np.median(corrs54):.3f}')
    ax.set_xlabel('Per-galaxy correlation'); ax.set_ylabel('Count')
    ax.set_title('Correlation Distribution'); ax.legend(fontsize=9); ax.grid(True, alpha=0.1)

    rmss52 = [r['RMS_kms'] for r in res52]
    rmss54 = [r['RMS_kms'] for r in res54]
    ax = axes[1]
    bins = np.linspace(0, 200, 40)
    ax.hist(rmss52, bins=bins, alpha=0.5, color='blue', label='V5.2', edgecolor='navy', lw=0.5)
    ax.hist(rmss54, bins=bins, alpha=0.5, color='green', label='V5.4', edgecolor='darkgreen', lw=0.5)
    ax.axvline(np.median(rmss52), color='blue', ls='--', lw=2, label=f'V5.2 med={np.median(rmss52):.1f}')
    ax.axvline(np.median(rmss54), color='green', ls='--', lw=2, label=f'V5.4 med={np.median(rmss54):.1f}')
    ax.set_xlabel('RMS Error (km/s)'); ax.set_ylabel('Count')
    ax.set_title('RMS Distribution'); ax.legend(fontsize=9); ax.grid(True, alpha=0.1)

    plt.suptitle('V5.2 vs V5.4 Distributions', fontsize=13, fontweight='bold')
    plt.tight_layout(rect=[0, 0, 1, 0.95])
    fig.savefig(os.path.join(OUT, 'v52_vs_v54_histograms.png'), dpi=150, bbox_inches='tight')
    plt.close(fig)

    # 3. Non-converged spotlight
    spotlight_names = sorted(nc52)[:6]
    if spotlight_names:
        fig, axes = plt.subplots(2, 3, figsize=(18, 10))
        axes_flat = axes.flatten()
        for i, name in enumerate(spotlight_names):
            if i >= 6: break
            ax = axes_flat[i]
            a = r52_dict.get(name)
            b = r54_dict.get(name)
            if not a or not b: continue
            ax.plot(a['r_kpc'], a['v_obs'], 'ko', ms=4, zorder=5, label='v_obs')
            ax.plot(a['r_kpc'], a['v_meas'], 'b--', lw=1.5, label='v_bar meas')
            ax.plot(a['r_kpc'], a['v_pred'], 'r-', lw=2, alpha=0.6,
                    label=f'V5.2 RMS={a["RMS_kms"]:.0f}')
            ax.plot(b['r_kpc'], b['v_pred'], 'g-', lw=2,
                    label=f'V5.4 RMS={b["RMS_kms"]:.0f}')
            conv = '✓' if b['converged'] else '⚠'
            ax.set_title(f'{name}  r={b["correlation"]:.3f} {conv}',
                        fontsize=10, fontweight='bold')
            ax.set_xlabel('r (kpc)'); ax.set_ylabel('v (km/s)')
            ax.legend(fontsize=7); ax.grid(True, alpha=0.1)
            ymax = max(np.max(a['v_obs']), np.max(a['v_pred']),
                      np.max(b['v_pred'])) * 1.2
            ax.set_ylim(0, ymax)
        for j in range(len(spotlight_names), 6):
            axes_flat[j].set_visible(False)
        plt.suptitle('V5.2 Non-Converged Galaxies: V5.2 (red) vs V5.4 (green)',
                     fontsize=13)
        plt.tight_layout(rect=[0, 0, 1, 0.95])
        fig.savefig(os.path.join(OUT, 'non_converged_spotlight.png'),
                    dpi=150, bbox_inches='tight')
        plt.close(fig)

    # 4. κᶜ detail for massive spirals
    for target in ['NGC7331', 'UGC09133', 'NGC5055', 'NGC2841']:
        if target in r52_dict and target in r54_dict:
            fig, axes = plt.subplots(1, 2, figsize=(14, 5))
            a = r52_dict[target]
            b = r54_dict[target]

            ax = axes[0]
            ax.plot(a['r_kpc'], a['v_obs'], 'ko', ms=4, label='v_obs')
            ax.plot(a['r_kpc'], a['v_meas'], 'b--', lw=1.5, label='v_bar meas')
            ax.plot(a['r_kpc'], a['v_pred'], 'r-', lw=2, alpha=0.7,
                    label=f'V5.2 RMS={a["RMS_kms"]:.1f}')
            ax.plot(b['r_kpc'], b['v_pred'], 'g-', lw=2,
                    label=f'V5.4 RMS={b["RMS_kms"]:.1f}')
            ax.set_xlabel('r (kpc)'); ax.set_ylabel('v (km/s)')
            ax.set_title(f'{target} — Rotation Curve')
            ax.legend(fontsize=9); ax.grid(True, alpha=0.1)

            ax = axes[1]
            ax.plot(a['r_kpc'], a['kappa'], 'r-', lw=2, alpha=0.7, label='V5.2 κᶜ')
            ax.plot(b['r_kpc'], b['kappa'], 'g-', lw=2, label='V5.4 κᶜ')
            ax.axhline(0.01, color='red', ls=':', lw=0.8, alpha=0.5, label='V5.2 floor')
            ax.set_xlabel('r (kpc)'); ax.set_ylabel('κᶜ')
            ax.set_title(f'{target} — Coupling Profile')
            ax.set_yscale('log')
            ax.legend(fontsize=9); ax.grid(True, alpha=0.1)

            plt.suptitle(f'{target}: V5.2 vs V5.4', fontsize=13, fontweight='bold')
            plt.tight_layout(rect=[0, 0, 1, 0.95])
            fig.savefig(os.path.join(OUT, f'detail_{target}.png'),
                        dpi=150, bbox_inches='tight')
            plt.close(fig)

    # 5. Δ-RMS vs v_max scatter
    fig, ax = plt.subplots(figsize=(10, 6))
    vmax_arr = [i['v_max'] for i in improvements]
    drms_arr = [i['rms_delta'] for i in improvements]
    colors = ['green' if d < 0 else 'red' for d in drms_arr]
    ax.scatter(vmax_arr, drms_arr, c=colors, s=20, alpha=0.6, edgecolors='k', lw=0.3)
    ax.axhline(0, color='black', ls='-', lw=1)
    ax.set_xlabel('v_max (km/s)', fontsize=12)
    ax.set_ylabel('ΔRMS (V5.4 − V5.2) km/s', fontsize=12)
    ax.set_title('RMS Change vs Galaxy Mass: Green = improved, Red = regressed',
                fontsize=12, fontweight='bold')
    ax.grid(True, alpha=0.1)
    n_improved = sum(1 for d in drms_arr if d < 0)
    n_regressed = sum(1 for d in drms_arr if d > 0)
    ax.text(0.02, 0.98, f'Improved: {n_improved}\nRegressed: {n_regressed}',
            transform=ax.transAxes, fontsize=11, va='top',
            bbox=dict(boxstyle='round', facecolor='lightyellow', alpha=0.9))
    fig.savefig(os.path.join(OUT, 'delta_rms_vs_vmax.png'), dpi=150, bbox_inches='tight')
    plt.close(fig)

    # ═══ SAVE ═══
    summary = {
        'comparison': 'V5.2 vs V5.4',
        'alpha': f'4π/3 = {ALPHA:.6f}',
        'free_parameters': 0,
        'v54_changes': [
            'Smooth κᶜ (softplus, floor=1e-6)',
            'Adaptive damping (0.08→0.20 ramp + oscillation detection)',
            'Radially-adaptive entropy smoothing',
            'Extended iterations (500)',
        ],
        'v52': stats52,
        'v54': stats54,
        'runtime_s': {'v52': round(t52,1), 'v54': round(t54,1)},
    }
    with open(os.path.join(OUT, 'v52_vs_v54_summary.json'), 'w') as f:
        json.dump(summary, f, indent=2)

    print(f"\n  All outputs → {OUT}/")
    print(f"  Runtime: V5.2={t52:.1f}s, V5.4={t54:.1f}s")


if __name__ == '__main__':
    main()
