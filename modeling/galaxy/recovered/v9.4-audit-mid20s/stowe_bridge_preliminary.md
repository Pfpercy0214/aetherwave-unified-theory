# Stowe 2026 × ARK V9.4 — Preliminary Bridge Audit

Date: 2026-08-30
Data: SPARC 175 rotmod archive supplied by user
ARK baseline: V9.4 mixed_slope projector
Comparison target for current canonical chain: Y_disk=0.475, Y_bulge=0.35

## Reproducibility
Re-running the supplied V9.4 source on the supplied SPARC archive reproduced the mixed_slope baseline exactly:
- standard SPARC M/L target RMS = 30.5500625153 km/s
- current Y-recalibrated target RMS = 24.3599816392 km/s

## 1. Cumulative ARK quantity H
Define
H_ARK = integral I(r) dr
where I is the V9.4 mixed_slope integrand.

Across 175 galaxies:
- corr(log H_ARK, log mean stellar SB) = +0.763
- corr(log H_ARK, log stellar line-column H_star) = +0.919
- corr(log H_ARK, log v_max) = +0.969

The H_ARK-H_star association remains partial r~+0.40 after controlling v_max and r_max, but falls to ~+0.06 after also controlling stellar SB. Thus H_ARK contains strong column-like scaling, but the evidence does not show that it independently recovers the missing absolute-SB degree of freedom.

Critically, after the canonical Y recalibration:
- corr(mean residual, log H_ARK) = -0.037
- corr(mean residual, log SB) = -0.406

A one-feature multiplicative correction based on log H_ARK worsens 5-fold galaxy-level OOS RMS from 24.360 to 24.614 km/s. A compactness variant log(H_ARK/r_max) gives only 24.136 km/s (~0.9% improvement).

Conclusion: the simple hypothesis that the remaining SB miss is just a global exponential function of H_ARK is rejected.

## 2. Stowe-inspired inverse radial response
Stowe's symmetric attenuation response can be written
D = 2 exp(-alpha H) sinh(alpha C).
Relative to its weak-linear limit, the inverse radial response contains the factor
w_rad(C) = alpha C / sinh(alpha C),
with w_rad -> 1 as alpha -> 0.

As a structural bridge test only, this factor was applied to the V9.4 integrand with one universal alpha. Alpha was selected only on training galaxies in 5-fold CV (seed 42); no photometry entered the predictor.

Results on the Y-recalibrated target:
- baseline OOS RMS: 24.360 km/s
- radial-response OOS RMS: 23.648 km/s
- improvement: 2.92%
- fold-selected alpha: 500, 550, 570, 600, 600 (stable range)
- 67.4% of galaxies improve in per-galaxy RMS

However:
- residual-vs-SB correlation worsens from -0.406 to -0.509
- bulgeless subset (f_bul < 0.01): 18.907 -> 19.214 km/s (1.62% worse)
- bulge-heavy subset (f_bul > 0.3): 31.776 -> 29.276 km/s (7.87% better)

The full Stowe-like factor including the global exp(+alpha H) inverse-scale term selects alpha=0; no improvement. The literal forward factor also selects alpha=0.

Interpretation: the useful signal is radial/nonlinear geometry, concentrated in bulge/high-curvature systems, not the missing global surface-density axis. This aligns with the prior V9.4 warning that the low fitted bulge M/L may be absorbing an inner-projector systematic.

## 3. Direct Beer-Lambert toy forward model
A deliberately simple forward model was also tested using the available stellar surface-brightness profile as the attenuating column, with two universal fit parameters and galaxy-level CV.

- stellar surface-column toy RMS vs observed rotation: ~111.8 km/s
- crude thickness-normalized version (Sigma/R_d): ~108.5 km/s
- N-baryon vs observed RMS for comparison: ~66.4 km/s

This toy fails strongly. It is not a faithful KSM test because the rotmod archive does not contain the gas surface-density profile or full 3-D disk thickness/volume-density geometry. It does show that a naive 1-D Beer-Lambert substitution is not sufficient.

## Preliminary ruling
Stowe's paper appears useful as a geometry clue, but not as a drop-in scale correction. The first numerical evidence separates the two pieces:
- radial exponential/nonlinear weighting: modestly useful, especially in bulge/high-curvature galaxies;
- global cumulative H amplitude: does not resolve the remaining SB miss.

V9.5 is requested next because the surviving improvement sits exactly in the inner/high-curvature regime already flagged as a likely V9.4 projector systematic.
