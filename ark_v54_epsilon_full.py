#!/usr/bin/env python3
"""
═══════════════════════════════════════════════════════════════════════
  ARK V5.4ε-FULL — RESIDUAL-DERIVED ENVIRONMENTAL ENTROPY
═══════════════════════════════════════════════════════════════════════

  For EVERY galaxy (not just the 8 that fail), find the ε that
  minimizes the RMS residual against measured baryonic velocity.

  This is explicitly circular as a prediction — we're using the
  answer to find the correction. But the DISTRIBUTION of ε across
  175 galaxies is informative:
    - If most ε ≈ 0: V5.4 is already capturing the physics
    - If ε correlates with observables: that's the missing piece
    - If ε is random: it's noise/systematics, not physics

  Method: For each galaxy, golden section search on ε ∈ [-0.5, 2.0]
  to minimize RMS(v_pred - v_meas). Negative ε allowed (galaxy
  in underdense environment, less entropy than isolated assumption).

  Author: Paul Frederick Percy Jr. & Theia (Claude Opus)
  Framework: ARK, Papers XXI–XXV
═══════════════════════════════════════════════════════════════════════
"""

import numpy as np
from scipy.integrate import cumulative_trapezoid
from scipy.ndimage import gaussian_filter1d
from scipy.optimize import minimize_scalar
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import os, json, glob, time

C = 299792458.0
KPC = 3.08567758e19
ALPHA = 4*np.pi/3
Yd, Yb = 0.5, 0.7

DATA = '/home/claude/sparc_full'
OUT = '/home/claude/ark_v54_epsilon_full'
os.makedirs(OUT, exist_ok=True)


def softplus_kappa(kap_raw, k_min=1e-6, k_max=1.0, sharpness=5.0):
    x = sharpness * kap_raw
    sp = np.where(x > 20, x, np.log1p(np.exp(np.minimum(x, 20))))
    sp_norm = sp / (sharpness * k_max + np.log(2))
    return k_min + (k_max - k_min) * np.clip(sp_norm, 0, 1)

def adaptive_smooth(arr, R, N, base_sig):
    if len(arr) < 7:
        return gaussian_filter1d(arr, sigma=base_sig)
    d2 = np.abs(np.gradient(np.gradient(arr[:N], R[:N]), R[:N]))
    d2 = np.concatenate([d2, np.zeros(len(arr) - N)])
    d2_norm = d2 / (np.max(d2) + 1e-30)
    light = gaussian_filter1d(arr, sigma=max(1, base_sig // 3))
    heavy = gaussian_filter1d(arr, sigma=base_sig * 2)
    weight = gaussian_filter1d(d2_norm, sigma=max(2, base_sig // 2))
    return weight * light + (1 - weight) * heavy

def compute_baryonic_velocity(gal):
    vg, vd, vb = gal['v_gas'], gal['v_disk'], gal['v_bul']
    return np.sqrt(np.maximum(
        np.abs(vg)*vg + Yd*np.abs(vd)*vd + Yb*np.abs(vb)*vb, 0))

def compute_chi2(v_pred, v_meas, err_v, v_obs):
    N = len(v_pred)
    residuals = v_pred - v_meas
    v_obs_safe = np.maximum(np.abs(v_obs), 1.0)
    v_meas_safe = np.maximum(np.abs(v_meas), 1.0)
    f_bar = v_meas_safe / v_obs_safe
    sigma_kin = np.maximum(err_v * f_bar, 2.0)
    sigma_sys = 0.12 * v_meas_safe
    sigma_comp = np.sqrt(sigma_kin**2 + sigma_sys**2)
    sigma_cons = np.maximum(err_v, 0.20 * v_meas_safe + 2.0)
    return {
        'N': N,
        'rms_kms': float(np.sqrt(np.mean(residuals**2))),
        'comp_chi2r': float(np.sum(residuals**2 / sigma_comp**2) / N),
        'cons_chi2r': float(np.sum(residuals**2 / sigma_cons**2) / N),
    }

def load_galaxy(filepath):
    name = os.path.basename(filepath).replace('_rotmod.dat', '')
    lines = []; dist = None
    with open(filepath, 'r') as f:
        for line in f:
            if line.startswith('#'):
                if 'Distance' in line:
                    try: dist = float(line.split('=')[1].strip().split()[0])
                    except: pass
                continue
            parts = line.strip().split()
            if len(parts) >= 6:
                lines.append([float(x) for x in parts[:8]])
    if len(lines) < 3: return None
    d = np.array(lines)
    return {
        'name': name, 'distance_Mpc': dist,
        'r': d[:,0], 'v_obs': d[:,1], 'err_v': d[:,2],
        'v_gas': d[:,3], 'v_disk': d[:,4], 'v_bul': d[:,5],
        'SBdisk': d[:,6], 'SBbul': d[:,7], 'N': len(d),
    }


def invert_with_epsilon(r_kpc, v_obs_kms, epsilon=0.0,
                         max_iter=500, damping_init=0.08):
    r = np.asarray(r_kpc, float) * KPC
    v = np.asarray(v_obs_kms, float) * 1e3
    N = len(r)
    if N < 3: return None

    g_obs = v**2 / np.maximum(r, r[0])
    n_ext = 400
    r_ext = np.linspace(r[-1]*1.01, 20*r[-1], n_ext)
    g_ext = g_obs[-1]*(r[-1]/r_ext)**2
    R = np.concatenate([r, r_ext]); G_obs = np.concatenate([g_obs, g_ext]); M = len(R)

    cum_obs = cumulative_trapezoid(G_obs, R, initial=0)
    phi_obs = cum_obs[-1] - cum_obs
    th_obs = np.sqrt(np.maximum(2*phi_obs/C**2, 0))
    dth_obs = np.zeros(M)
    ok = th_obs > 1e-30; dth_obs[ok] = -G_obs[ok]/(C**2*th_obs[ok])

    dr_med = np.median(np.diff(R[:N]))
    base_sig = max(3, int(2*dr_med/np.median(np.diff(R))))
    g_bar = G_obs.copy() * 0.3; recent_deltas = []

    for iteration in range(max_iter):
        g_bar_old = g_bar.copy()
        cum_bar = cumulative_trapezoid(g_bar, R, initial=0)
        phi_bar = cum_bar[-1] - cum_bar
        thN = np.sqrt(np.maximum(2*phi_bar/C**2, 0))
        thN2 = np.maximum(thN**2, 1e-40)
        r2g = R**2 * g_bar; d_r2g = np.gradient(r2g, R)
        dSt = np.maximum(d_r2g, 0)/C**2
        dSt = adaptive_smooth(dSt, R, N, base_sig)
        dSt_eff = dSt * (1.0 + epsilon)
        kap_raw = ALPHA * dSt_eff / thN2
        kap = softplus_kappa(kap_raw)
        dthN_new = kap * dth_obs; abs_dthN = np.abs(dthN_new)
        cum_dthN = cumulative_trapezoid(abs_dthN, R, initial=0)
        thN_new = np.maximum(cum_dthN[-1] - cum_dthN, 1e-30)
        g_bar_new = C**2 * thN_new * abs_dthN

        progress = min(iteration / 150.0, 1.0)
        damping_base = damping_init + (0.20 - damping_init) * progress
        if len(recent_deltas) >= 4:
            if (recent_deltas[-1]-recent_deltas[-2])*(recent_deltas[-2]-recent_deltas[-3]) < 0:
                damping_base *= 0.7
        damping = np.clip(damping_base, 0.03, 0.25)
        g_bar = damping*g_bar_new + (1-damping)*g_bar; g_bar = np.maximum(g_bar, 0)
        delta = np.max(np.abs(g_bar[:N]-g_bar_old[:N])/np.maximum(np.abs(g_bar[:N]),1e-30))
        recent_deltas.append(delta)
        if len(recent_deltas) > 10: recent_deltas.pop(0)
        if delta < 1e-5: break

    s = slice(0, N)
    v_bar = np.sqrt(np.maximum(R*g_bar, 0))
    return {
        'v_bar_pred_kms': v_bar[s]/1e3, 'g_bar_pred': g_bar[s],
        'kappa': kap[s], 'converged': delta < 1e-5,
        'iterations': iteration+1, 'final_delta': float(delta),
        'epsilon': epsilon,
    }


def find_optimal_epsilon(r_kpc, v_obs_kms, v_meas):
    """
    Find ε that minimizes RMS(v_pred - v_meas).
    Search range: [-0.5, 2.5] (allow underdense environments).
    """
    def objective(eps):
        inv = invert_with_epsilon(r_kpc, v_obs_kms, epsilon=eps)
        if inv is None or not inv['converged']:
            return 1e6
        resid = inv['v_bar_pred_kms'] - v_meas
        return float(np.sqrt(np.mean(resid**2)))

    # Coarse scan first to find good region
    eps_scan = np.linspace(-0.3, 2.0, 24)
    rms_scan = [objective(e) for e in eps_scan]
    best_idx = np.argmin(rms_scan)

    # Refine around best
    lo = eps_scan[max(0, best_idx-1)]
    hi = eps_scan[min(len(eps_scan)-1, best_idx+1)]

    result = minimize_scalar(objective, bounds=(lo, hi), method='bounded',
                             options={'xatol': 0.001})
    best_eps = result.x
    best_inv = invert_with_epsilon(r_kpc, v_obs_kms, epsilon=best_eps)

    return best_inv, best_eps


def main():
    print("═"*72)
    print("  ARK V5.4ε-FULL — OPTIMAL ε FOR ALL 175 GALAXIES")
    print("  Method: minimize RMS via ε search per galaxy")
    print("  Purpose: map the environmental entropy landscape")
    print("═"*72)

    files = sorted(glob.glob(os.path.join(DATA, '*_rotmod.dat')))
    galaxies = [g for g in (load_galaxy(f) for f in files) if g is not None]
    print(f"\n  Loaded {len(galaxies)} galaxies\n")

    results_v54 = []
    results_opt = []
    all_v54 = {'meas':[], 'pred':[], 'err':[], 'vobs':[], 'fbul':[]}
    all_opt = {'meas':[], 'pred':[], 'err':[], 'vobs':[], 'fbul':[]}

    galaxy_data = []  # full per-galaxy info

    t0 = time.time()
    for i, gal in enumerate(galaxies):
        if (i+1) % 25 == 0:
            print(f"  Processing {i+1}/{len(galaxies)}...")
        try:
            v_meas = compute_baryonic_velocity(gal)
            vb2 = np.abs(gal['v_bul'])**2
            vtot2 = np.abs(gal['v_gas'])**2 + np.abs(gal['v_disk'])**2 + vb2
            f_bul = vb2 / np.maximum(vtot2, 1e-30)

            # V5.4 baseline
            inv54 = invert_with_epsilon(gal['r'], gal['v_obs'], epsilon=0.0)
            if inv54 is None: continue

            # Optimal ε
            inv_opt, eps_opt = find_optimal_epsilon(gal['r'], gal['v_obs'], v_meas)
            if inv_opt is None:
                inv_opt = inv54
                eps_opt = 0.0

            chi54 = compute_chi2(inv54['v_bar_pred_kms'], v_meas, gal['err_v'], gal['v_obs'])
            chi_opt = compute_chi2(inv_opt['v_bar_pred_kms'], v_meas, gal['err_v'], gal['v_obs'])

            valid54 = (v_meas > 1) & (inv54['v_bar_pred_kms'] > 1)
            valid_opt = (v_meas > 1) & (inv_opt['v_bar_pred_kms'] > 1)
            corr54 = np.corrcoef(v_meas[valid54], inv54['v_bar_pred_kms'][valid54])[0,1] if np.sum(valid54) > 3 else 0
            corr_opt = np.corrcoef(v_meas[valid_opt], inv_opt['v_bar_pred_kms'][valid_opt])[0,1] if np.sum(valid_opt) > 3 else 0

            # Observables for correlation analysis
            n_outer = max(3, gal['N']//3)
            v_slope = float(np.polyfit(gal['r'][-n_outer:], gal['v_obs'][-n_outer:], 1)[0])
            v_bar_ratio = float(np.mean(v_meas) / np.maximum(np.mean(gal['v_obs']), 1))
            mean_sb = float(np.mean(gal['SBdisk'][gal['SBdisk'] > 0])) if np.any(gal['SBdisk'] > 0) else 0

            galaxy_data.append({
                'name': gal['name'],
                'N': gal['N'],
                'v_max': float(np.max(gal['v_obs'])),
                'epsilon_opt': round(eps_opt, 6),
                'rms_v54': round(chi54['rms_kms'], 2),
                'rms_opt': round(chi_opt['rms_kms'], 2),
                'rms_improvement': round(chi54['rms_kms'] - chi_opt['rms_kms'], 2),
                'corr_v54': round(float(corr54), 4),
                'corr_opt': round(float(corr_opt), 4),
                'converged_v54': bool(inv54['converged']),
                'converged_opt': bool(inv_opt['converged']),
                'distance_Mpc': gal.get('distance_Mpc'),
                'r_last_kpc': float(gal['r'][-1]),
                'v_slope': v_slope,
                'v_bar_ratio': v_bar_ratio,
                'mean_SBdisk': mean_sb,
                'f_bul_max': float(np.max(f_bul)),
            })

            for acc, inv in [(all_v54, inv54), (all_opt, inv_opt)]:
                acc['meas'].extend(v_meas.tolist())
                acc['pred'].extend(inv['v_bar_pred_kms'].tolist())
                acc['err'].extend(gal['err_v'].tolist())
                acc['vobs'].extend(gal['v_obs'].tolist())
                acc['fbul'].extend(f_bul.tolist())

            for res_list, chi, corr_val, inv in [
                (results_v54, chi54, corr54, inv54),
                (results_opt, chi_opt, corr_opt, inv_opt),
            ]:
                res_list.append({
                    'name': gal['name'], 'N': gal['N'],
                    'v_max_kms': round(float(np.max(gal['v_obs'])), 1),
                    'RMS_kms': round(chi['rms_kms'], 2),
                    'correlation': round(float(corr_val), 4),
                    'chi2_comp': round(chi['comp_chi2r'], 4),
                    'chi2_cons': round(chi['cons_chi2r'], 4),
                    'converged': bool(inv['converged']),
                    'v_meas': v_meas, 'v_pred': inv['v_bar_pred_kms'],
                    'v_obs': gal['v_obs'], 'r_kpc': gal['r'], 'f_bul': f_bul,
                })
        except Exception as e:
            print(f"  !! {gal['name']}: {e}")
            continue

    elapsed = time.time() - t0
    print(f"\n  Completed in {elapsed:.0f}s")

    # ═══ GLOBAL STATS ═══
    def gstats(results, all_data, label):
        am = np.array(all_data['meas']); ap = np.array(all_data['pred'])
        ae = np.array(all_data['err']); av = np.array(all_data['vobs'])
        af = np.array(all_data['fbul'])
        valid = (am > 1) & (ap > 1) & np.isfinite(am) & np.isfinite(ap)
        gc = np.corrcoef(am[valid], ap[valid])[0,1]
        grms = np.sqrt(np.mean((ap[valid]-am[valid])**2))
        gchi = compute_chi2(ap[valid], am[valid], ae[valid], av[valid])
        corrs = [r['correlation'] for r in results]
        conv = sum(1 for r in results if r['converged'])
        resid = ap - am; rv = resid[valid]; amv = am[valid]; afv = af[valid]
        fm = np.isfinite(rv) & np.isfinite(afv)
        rbc = float(np.corrcoef(rv[fm], afv[fm])[0,1]) if np.sum(fm) > 10 else 0
        bins = [(0,20),(20,40),(40,80),(80,150),(150,200),(200,260),(260,400)]
        br = {}
        for lo,hi in bins:
            m = (amv >= lo) & (amv < hi)
            if np.sum(m) > 0:
                br[f'{lo}-{hi}'] = {'mean_resid': round(float(np.mean(rv[m])),1), 'count': int(np.sum(m))}
        return {
            'label': label, 'total': len(results), 'converged': conv,
            'global_r': round(float(gc),4), 'global_rms': round(float(grms),1),
            'median_r': round(float(np.median(corrs)),4),
            'mean_r': round(float(np.mean(corrs)),4),
            'frac_r_gt_08': round(sum(1 for c in corrs if c>0.8)/len(corrs),3),
            'chi2_comp_global': round(gchi['comp_chi2r'],4),
            'chi2_cons_global': round(gchi['cons_chi2r'],4),
            'chi2_cons_median': round(float(np.median([r['chi2_cons'] for r in results])),4),
            'binned_residuals': br, 'resid_bulge_corr': round(rbc,4),
        }, (am, ap, resid, af)

    stats54, diag54 = gstats(results_v54, all_v54, "V5.4")
    stats_opt, diag_opt = gstats(results_opt, all_opt, "V5.4ε-opt")

    # ═══ REPORT ═══
    print(f"\n{'═'*72}")
    print(f"  {'METRIC':<35s} {'V5.4':>12s} {'V5.4ε-opt':>12s} {'CHANGE':>10s}")
    print(f"  {'─'*69}")
    for key, lbl in [
        ('total','Galaxies'), ('converged','Converged'),
        ('global_r','Global correlation'), ('global_rms','Global RMS (km/s)'),
        ('median_r','Median per-galaxy r'), ('mean_r','Mean per-galaxy r'),
        ('frac_r_gt_08','Fraction r > 0.8'),
        ('chi2_comp_global','χ²/N composite (global)'),
        ('chi2_cons_global','χ²/N conservative (global)'),
        ('chi2_cons_median','χ²/N conservative (median)'),
        ('resid_bulge_corr','Residual–bulge corr'),
    ]:
        v54 = stats54[key]; vo = stats_opt[key]
        if isinstance(v54, float):
            d = vo-v54; s = '+' if d > 0 else ''
            print(f"  {lbl:<35s} {v54:>12} {vo:>12} {s}{d:>9.4f}")
        else:
            print(f"  {lbl:<35s} {v54:>12} {vo:>12} {vo-v54:>+10d}")
    print(f"{'═'*72}")

    # Binned residuals
    print(f"\n  RESIDUAL vs v_bar_meas:")
    print(f"  {'Bin':>10s}  {'V5.4':>8s}  {'ε-opt':>8s}  {'Δ':>8s}")
    print(f"  {'─'*40}")
    for b in stats54['binned_residuals']:
        r54v = stats54['binned_residuals'][b]['mean_resid']
        rov = stats_opt['binned_residuals'].get(b,{}).get('mean_resid',0)
        n = stats54['binned_residuals'][b]['count']
        print(f"  {b:>10s}  {r54v:>+7.1f}  {rov:>+7.1f}  {rov-r54v:>+7.1f}  (n={n})")

    # ═══ EPSILON DISTRIBUTION ═══
    eps_all = np.array([g['epsilon_opt'] for g in galaxy_data])
    vmax_all = np.array([g['v_max'] for g in galaxy_data])

    print(f"\n{'═'*72}")
    print(f"  EPSILON DISTRIBUTION ACROSS ALL {len(galaxy_data)} GALAXIES")
    print(f"  {'─'*69}")
    print(f"  Mean:     {np.mean(eps_all):.4f}")
    print(f"  Median:   {np.median(eps_all):.4f}")
    print(f"  Std:      {np.std(eps_all):.4f}")
    print(f"  Min:      {np.min(eps_all):.4f}  ({galaxy_data[np.argmin(eps_all)]['name']})")
    print(f"  Max:      {np.max(eps_all):.4f}  ({galaxy_data[np.argmax(eps_all)]['name']})")
    print(f"  |ε| < 0.01:  {np.sum(np.abs(eps_all) < 0.01)}")
    print(f"  |ε| < 0.05:  {np.sum(np.abs(eps_all) < 0.05)}")
    print(f"  |ε| < 0.10:  {np.sum(np.abs(eps_all) < 0.10)}")
    print(f"  ε < 0:       {np.sum(eps_all < 0)}  (underdense environments)")
    print(f"  ε > 0.5:     {np.sum(eps_all > 0.5)}  (high external pressure)")

    # Mass-binned epsilon
    print(f"\n  ε BY GALAXY MASS:")
    print(f"  {'v_max bin':>12s} {'N':>4s} {'ε mean':>8s} {'ε med':>8s} {'ε std':>8s}")
    for lo, hi in [(0,80),(80,150),(150,220),(220,400)]:
        mask = (vmax_all >= lo) & (vmax_all < hi)
        if np.sum(mask) > 0:
            e = eps_all[mask]
            print(f"  {lo:>5d}–{hi:<5d}  {np.sum(mask):>4d}  "
                  f"{np.mean(e):>+7.4f}  {np.median(e):>+7.4f}  {np.std(e):>7.4f}")

    # ═══ CORRELATION ANALYSIS ═══
    print(f"\n  OBSERVABLE CORRELATIONS WITH ε (all {len(galaxy_data)} galaxies):")
    obs_keys = [
        ('v_max', 'v_max'),
        ('r_last (kpc)', 'r_last_kpc'),
        ('distance (Mpc)', 'distance_Mpc'),
        ('mean SBdisk', 'mean_SBdisk'),
        ('f_bul_max', 'f_bul_max'),
        ('outer v slope', 'v_slope'),
        ('v_bar/v_obs ratio', 'v_bar_ratio'),
    ]
    for obs_name, obs_key in obs_keys:
        obs_arr = np.array([g.get(obs_key, np.nan) for g in galaxy_data])
        valid = np.isfinite(obs_arr) & np.isfinite(eps_all) & (obs_arr != 0)
        if np.sum(valid) >= 10:
            r_corr = np.corrcoef(eps_all[valid], obs_arr[valid])[0,1]
            print(f"    {obs_name:>25s}:  r = {r_corr:+.4f}  (n={np.sum(valid)})")

    # ═══ PLOTS ═══
    # 1. Scatter comparison
    fig, axes = plt.subplots(1, 2, figsize=(16, 7))
    for ax, diag, stats, lbl, color in [
        (axes[0], diag54, stats54, 'V5.4 (ε = 0)', 'darkgreen'),
        (axes[1], diag_opt, stats_opt, 'V5.4ε-optimal', 'darkblue'),
    ]:
        am, ap = diag[0], diag[1]
        v = (am > 1) & (ap > 1) & np.isfinite(am) & np.isfinite(ap)
        ax.scatter(am[v], ap[v], s=3, alpha=0.15, c=color)
        mx = max(np.max(am[v]), np.max(ap[v]))*1.05
        ax.plot([0,mx],[0,mx], 'k--', lw=1.5, alpha=0.5)
        ax.set_xlabel('v_bar MEASURED (km/s)'); ax.set_ylabel('v_bar PREDICTED (km/s)')
        ax.set_title(lbl, fontsize=12, fontweight='bold')
        ax.set_xlim(0,mx); ax.set_ylim(0,mx); ax.set_aspect('equal'); ax.grid(True, alpha=0.12)
        ax.text(0.05, 0.95, f'r = {stats["global_r"]:.4f}\nRMS = {stats["global_rms"]:.1f} km/s\n'
                f'χ²/N = {stats["chi2_cons_global"]:.3f} (cons)\n'
                f'Conv: {stats["converged"]}/{stats["total"]}',
                transform=ax.transAxes, fontsize=11, va='top',
                bbox=dict(boxstyle='round', facecolor='lightyellow', alpha=0.9))
    plt.suptitle('V5.4 vs V5.4ε-optimal (per-galaxy ε)', fontsize=14, fontweight='bold')
    plt.tight_layout(rect=[0,0,1,0.96])
    fig.savefig(os.path.join(OUT, 'scatter.png'), dpi=150, bbox_inches='tight'); plt.close()

    # 2. Residual bias
    fig, axes = plt.subplots(1, 2, figsize=(16, 6))
    for ax, diag, stats, lbl, color in [
        (axes[0], diag54, stats54, 'V5.4', 'green'),
        (axes[1], diag_opt, stats_opt, 'V5.4ε-opt', 'blue'),
    ]:
        am, ap, resid = diag[0], diag[1], diag[2]
        v = (am > 1) & np.isfinite(resid)
        ax.scatter(am[v], resid[v], s=3, alpha=0.1, c=color)
        ax.axhline(0, color='black', lw=1.5)
        edges = [0,20,40,80,150,200,260,400]; bc, bm = [], []
        for i in range(len(edges)-1):
            m = v & (am >= edges[i]) & (am < edges[i+1])
            if np.sum(m) > 5: bc.append((edges[i]+edges[i+1])/2); bm.append(np.mean(resid[m]))
        ax.plot(bc, bm, 'ko-', ms=8, lw=2, zorder=5, label='Binned mean')
        ax.set_xlabel('v_bar MEASURED (km/s)'); ax.set_ylabel('Residual (km/s)')
        ax.set_title(f'{lbl}: resid–bulge r={stats["resid_bulge_corr"]:.3f}')
        ax.legend(); ax.grid(True, alpha=0.1); ax.set_ylim(-200, 100)
    plt.suptitle('Residual Bias: V5.4 vs V5.4ε-optimal', fontsize=13, fontweight='bold')
    plt.tight_layout(rect=[0,0,1,0.95])
    fig.savefig(os.path.join(OUT, 'residual_bias.png'), dpi=150, bbox_inches='tight'); plt.close()

    # 3. Epsilon distribution histogram
    fig, axes = plt.subplots(1, 2, figsize=(16, 6))
    ax = axes[0]
    ax.hist(eps_all, bins=50, color='steelblue', alpha=0.8, edgecolor='black', linewidth=0.5)
    ax.axvline(0, color='red', lw=2, ls='--', label='ε = 0')
    ax.axvline(np.median(eps_all), color='orange', lw=2, ls='--',
              label=f'median = {np.median(eps_all):.3f}')
    ax.set_xlabel('ε (optimal)', fontsize=11)
    ax.set_ylabel('Count', fontsize=11)
    ax.set_title('Distribution of Optimal ε', fontsize=12, fontweight='bold')
    ax.legend()

    ax = axes[1]
    ax.scatter(vmax_all, eps_all, s=20, alpha=0.6, c='steelblue')
    ax.set_xlabel('v_max (km/s)', fontsize=11)
    ax.set_ylabel('ε (optimal)', fontsize=11)
    ax.set_title('ε vs Galaxy Mass', fontsize=12, fontweight='bold')
    ax.axhline(0, color='red', lw=1, ls='--')
    ax.grid(True, alpha=0.2)
    plt.tight_layout()
    fig.savefig(os.path.join(OUT, 'epsilon_analysis.png'), dpi=150, bbox_inches='tight'); plt.close()

    # 4. ε vs RMS improvement
    rms_imp = np.array([g['rms_improvement'] for g in galaxy_data])
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.scatter(eps_all, rms_imp, s=20, alpha=0.6, c=vmax_all, cmap='viridis')
    ax.set_xlabel('ε (optimal)', fontsize=11)
    ax.set_ylabel('RMS improvement (km/s)', fontsize=11)
    ax.set_title('ε vs RMS Improvement (color = v_max)', fontsize=12, fontweight='bold')
    ax.axhline(0, color='red', lw=1, ls='--')
    ax.axvline(0, color='red', lw=1, ls='--')
    plt.colorbar(ax.collections[0], label='v_max (km/s)')
    ax.grid(True, alpha=0.2)
    plt.tight_layout()
    fig.savefig(os.path.join(OUT, 'epsilon_vs_improvement.png'), dpi=150, bbox_inches='tight'); plt.close()

    # Save
    summary = {
        'method': 'V5.4ε-full: RMS-optimal ε for all galaxies',
        'explicitly_circular': True,
        'purpose': 'Map environmental entropy landscape',
        'v54': stats54, 'v54_eps_opt': stats_opt,
        'epsilon_stats': {
            'mean': round(float(np.mean(eps_all)), 4),
            'median': round(float(np.median(eps_all)), 4),
            'std': round(float(np.std(eps_all)), 4),
            'min': round(float(np.min(eps_all)), 4),
            'max': round(float(np.max(eps_all)), 4),
        },
        'galaxy_data': [{k:v for k,v in g.items()} for g in galaxy_data],
        'runtime': round(elapsed, 1),
    }
    with open(os.path.join(OUT, 'summary.json'), 'w') as f:
        json.dump(summary, f, indent=2, default=str)

    print(f"\n  Outputs → {OUT}/")


if __name__ == '__main__':
    main()
