# Stowe 2026 × ARK V9.4/V9.5 — Guarded Comparison

Date: 2026-08-30
Data: user-supplied SPARC 175 rotmod archive

## V9.5 reproduction
The uploaded V9.5 null guards reproduce the recorded negative result exactly:
- synthetic flat eta outer/inner = 9.53
- Keplerian = 10.68
- solid-to-flat = 9.53
- exponential-disk-like = 11.49
- SPARC median = 10.06 (only 1.06x the flat synthetic artifact)
- eta-transition vs baryon half-support radius r = +0.831
- dumb r_max null r = +0.897
- partial eta-transition vs baryon radius controlling r_max = +0.119, p=0.281

Thus V9.5's 1-D eta-shape observable remains closed.

## V9.5-style guards applied to the Stowe-inspired V9.4 bridge
Canonical V9.4 mixed-slope + Yd=0.475, Yb=0.35 baseline: 24.3600 km/s.

Five-fold galaxy-level CV:
- Stowe inverse radial factor x/sinh(x), x=alpha*C: 23.6485 km/s (+2.92%)
- Gaussian cumulative suppressor exp[-(alpha*C)^2/6]: 23.6503 (+2.91%)
- Rational cumulative suppressor 1/[1+(alpha*C)^2/6]: 23.6296 (+3.00%)
- Stowe factor on normalized C/H: 23.8395 (+2.14%)
- Stowe factor on radius only r/rmax: 24.0327 (+1.34%)

A simple amplitude-weighted radius null,
  x = alpha * H * sqrt(r/rmax),
gets 23.6299 km/s on a refined alpha grid, slightly better than the Stowe C profile (23.6481).

Interpretation: the numerical gain is real, but the exact Beer-Lambert/Stowe radial form is not identified. Generic monotone cumulative/radial suppression can reproduce it.

## Boundary degeneracy
The Stowe alpha is strongly degenerate with the assumed exterior acceleration tail.
For g_ext proportional to r^-p (20 rmax horizon):

p    baseline RMS   Stowe-C CV RMS   fold alpha behavior
1.00 60.348         60.348           all 0
1.25 46.957         46.957           all 0
1.50 34.471         34.471           all 0
1.75 25.606         25.606           all 0
1.85 24.021         24.021           all 0
1.90 23.772         23.842           mixed 0-350
1.95 23.890         23.690           ~350-500
2.00 24.360         23.649           ~500-600
2.05 25.150         23.762           ~600-700
2.10 26.221         23.916           ~700-750
2.25 30.691         25.085           ~850-950
2.50 40.340         27.844           alpha hits 1000 grid ceiling

With the V9.5-style flat-v boundary extended to 50 rmax, the baseline is 69.126 km/s against the N-baryon target and both the Stowe-C and radius-only corrections select alpha=0 in every fold.

This means the apparent Stowe parameter partly acts as a compensator for the chosen exterior/boundary geometry. It cannot presently be interpreted as an independently measured attenuation coefficient.

## Revised ruling
The earlier statement that Stowe had likely exposed a missing nonlinear radial operator in V9.4 should be demoted.

What survives:
1. Cumulative nonlocal geometry contains useful information beyond a radius-only null (C/H beats r/rmax), but not enough to identify Stowe's exponential law.
2. The strongest conceptual convergence between Stowe and V9.5 is directional: Stowe's force is an opposing-column difference, while the V9.5 record independently concludes that a 1-D azimuthally averaged curve cannot carry directional bulk-flow information.
3. A meaningful next test therefore needs resolved 2-D/3-D baryonic column/thickness information and preferably resolved velocity fields; another 1-D SPARC reweighting is unlikely to discriminate the mechanism.
4. The persistent absolute-surface-density axis in V9.4 remains unresolved. The Stowe bridge does not remove it.

## Files generated
- stowe_v95_guard_results.csv: model/null comparison
- stowe_v95_guard_output.txt: printed comparison
- stowe_tail_sweep.txt: tail-exponent degeneracy sweep
- v95_guard_repro.txt: reproduced V9.5 artifact guard
- v95_autopsy_repro.txt: reproduced V9.5 stage autopsy
