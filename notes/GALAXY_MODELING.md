# GALAXY_MODELING — status

**Dated:** 2026-09-10  
**Primary artifact branch:** `ARK-GAL-1D-9.4`  
**Sources:** `ark_v94_scalar_geom.txt` header, `model_comparison.csv`, `v94_summary.txt`, branch READMEs.

## Branch lineage

```text
main
 └── galaxy-modeling          # parent home (+ 1d/ drop zone)
      └── galaxy-1d           # 1D charter (parameter-free)
           └── ARK-GAL-1D-9.4 # v9.4 run package (present)
                └── ARK-GAL-1D-9.5  # pending — not on repo
```

| Branch | Content relevant to galaxy |
|--------|----------------------------|
| `galaxy-modeling` | Charter + `1d/README.md` stub |
| `galaxy-1d` | 1D charter only (inherits theory PDFs) |
| `ARK-GAL-1D-9.4` | Script, stdout, summary, CSVs, scatters |

## Method sketch (V9.4) — from `ark_v94_scalar_geom.txt` header

Builds on corrected **V9.3** baseline:

| Quantity | Definition |
|----------|------------|
| τ(r) | `v_obs(r) * √2 / c` |
| θ_obs(r) | `√(2\|Φ(r)\| / c²)` |
| κ(r) | `τ(r) / θ_obs(r)` |

Integrand form:

```text
I(r) = |κ dθ/dr| + F_geom(r) * r * |div(κ ∇θ)|
```

- **V9.3:** constant λ on the divergence term.
- **V9.4:** scalar-only geometry projectors **F_geom(r)** replace λ.
- **No photometry in the predictor.** Surface brightness / morphology saved only as **audit** variables in per-galaxy output.
- **Target / baryonic proxy** uses SPARC components with **Y_DISK = 0.5**, **Y_BULGE = 0.7** (in `compute_sparc_baryonic`).
- SI bridge: θ̄ from outer integral of I; `g_bar = c² θ̄ |dθ̄/dr|`; `v_bar = √(r g_bar)`.

### Candidate projectors

| Name | F_geom idea |
|------|-------------|
| `const_1_3` | F = 1/3 (V9.3-style control) |
| `const_1_2` | F = 1/2 (control) |
| `theta_slope` | F = 1/(2 + 2 clip(χ_θ,0,1)), χ_θ = \|d ln θ / d ln r\| |
| `kappa_slope` | same with χ_κ |
| `mixed_slope` | χ = ½(χ_θ + χ_κ) |
| `div_partition` | q from grad-coupling vs plain curvature share; F = 1/(2+2q) |

## Metrics (dump on `ARK-GAL-1D-9.4`)

**N = 175 galaxies, 3213 radial points** (from `model_comparison.csv` / `v94_summary.txt`).

| projector | global_r | global_rms_kms | mean_resid_kms | residual_vs_vmax_r | residual_vs_logSB_r | F_median |
|-----------|----------|----------------|----------------|--------------------|---------------------|----------|
| const_1_3 | 0.915 | **32.98** | −9.62 | −0.460 | **−0.627** | 0.333 |
| const_1_2 | 0.911 | 31.99 | +7.20 | −0.090 | −0.383 | 0.500 |
| theta_slope | 0.918 | 30.73 | −4.52 | −0.373 | −0.568 | 0.396 |
| kappa_slope | **0.921** | 30.63 | −6.29 | −0.387 | −0.581 | 0.373 |
| mixed_slope | 0.921 | **30.55** | −5.75 | −0.386 | −0.580 | 0.378 |
| div_partition | 0.911 | 31.99 | +7.20 | −0.090 | −0.383 | 0.500 |

Shared: `kappa_outer_median ≈ 0.912`, `kappa_outer_cv ≈ 0.077`.

**Best in-file RMS:** `mixed_slope` ≈ 30.55 km/s (then kappa_slope / theta_slope).

### Files present

| File | Role |
|------|------|
| `ark_v94_scalar_geom.txt` | Full method + runner script |
| `ark_v94_scalar_geom_stdout.txt` | Stdout JSON dump |
| `v94_summary.txt` | Per-projector summary |
| `model_comparison.csv` | Comparison table |
| `{projector}_galaxy_info.csv` | Per-galaxy rows |
| `{projector}_scatter.png` | Pred vs baryonic-proxy scatter |

## Open questions

| Issue | Note |
|-------|------|
| **23–25 vs ~30+ RMS** | Charter / discussion cites typical SPARC RMS ~23–25; **this v9.4 dump** shows ~30.5–33. Reconcile run definition, sample cuts, or prior version — do not blur numbers. |
| **residual_vs_logSB** | Strong negative correlation especially for `const_1_3` (−0.63); photometry not in predictor but residuals still track log SB — audit / open. |
| **const_1_2 ≈ div_partition** | Metrics match to numerical noise (F≈½ everywhere for div_partition in this run) — projector may be collapsing to constant ½; investigate before interpreting as geometry signal. |
| **v9.5** | **Pending upload** — expected as new offshoot off `galaxy-1d` / latest version branch. |
| Residual attribution | Keep **projection loss** vs **external/phase influence** as separate hypotheses. |

## Norms (from charters)

- Zero articulation / no free knobs in core method; label any tuning as calibration/experiment.
- MOND-style low residuals ≠ proof of mechanical completeness if knobs absorb lost 3D structure.
- No deletes without Paul’s OK.
