# ARK V9.4 — Global SB Correction Test (ε-as-data, step 1)
Date: 2026-07-03 (night shift session)
Analyst: Theia (Claude) with P. Percy

## Provenance
- SPARC data: user upload `SPARC_175_rotmod.zip` (175 rotmod files, SPARC 2016 distribution, Lelli/McGaugh/Schombert). No external data fetched this session.
- Solver: user upload `ark_v94_scalar_geom_bundle.zip` → `ark_v94_scalar_geom.py` (V9.4, pre-EPS-fix bundle).
- Reproducibility check: re-run of bundled script on uploaded SPARC zip reproduced all six projector RMS values to <1e-9 km/s (bit-exact). Instrument verified before analysis.

## Bundle forensics
- div_partition RMS ≡ const_1_2 RMS to 13 decimal places, F pinned at 0.500:
  this bundle is the PRE-FIX run; the EPS safety-floor bug saturates the
  partition projector into the constant-1/2 control. Preserved as the
  "before" record of the V9.4 EPS bug.

## Step 0 — ε structure scan (mixed_slope, best projector, RMS 30.550)
Per-galaxy mean_resid (ε proxy) vs observables (n=175):
- log_SBdisk: r = −0.580 (p≈4e−17)  ← dominant
- f_gas: +0.423 | f_bul: −0.431 | v_max: −0.386
- distance (signed): r = +0.009 — NULL (systematics check passed)
- Multivariate R² (7 observables → ε): 0.482
Verdict: ε is structured, dominated by INTERNAL observables → missing
baryon-mapping physics, not external perturbation. Environmental ε claims
must control for SB/f_gas first.

## Step 1 — Two-parameter GLOBAL correction (no per-galaxy freedom)
Forms tested on per-point residuals (n=3213):
- additive:        Δv = a + b·logSB
- multiplicative:  v_corr = v_pred·(1 + a + b·logSB)

In-sample: additive 27.361 | multiplicative 26.979 km/s
5-fold cross-validation, folds split BY GALAXY (seed=42):
- additive OOS RMS = 27.432
- multiplicative OOS RMS = 27.069   ← selected
- baseline = 30.550

OOS ≈ in-sample ⇒ structure is real, not overfit.
Result: 30.55 → 27.07 km/s (−11.4%) for 2 global parameters total.
Best-fit law: v_corr = v_pred·(1 + 0.479 − 0.236·logSB)
Correction zero-crossing: logSB ≈ 2.03 → SB ≈ 107 L/pc²
(order of MOND critical surface density Σ† = a0/2πG ≈ 137 M☉/pc²; suggestive, not exact — M/L dependent)

## Post-correction residual scan (what survives)
- vs logSB: r = −0.215 (was −0.580) — linear law captures most, not all
- vs f_bul: r = −0.252 (p=8e−4) — bulge structure survives
- vs f_gas: r = +0.193
- vs v_max: r = −0.103 — now null

## Rulings
1. "Tune ε per galaxy" is REJECTED for this residual: 48% of it is
   predictable from internal observables; per-galaxy freedom would bury
   identifiable physics. (Partition principle: identified structure must
   move from the bin to the resolved column.)
2. Next candidates: nonlinear SB law; f_bul term; THEN environment
   cross-match (tidal index, CMB-frame peculiar velocity) on whatever
   residue remains.
3. Any future external data pulls get logged here with source + date.

## Step 2 — Acceleration reframing test (NEGATIVE, informative)
Residuals do NOT collapse onto a universal acceleration function: offset vs
log(g) is an arch, accel power-law OOS = 29.3 (worse than SB law), SB
structure survives accel correction at r=-0.55. Miss is organized by GLOBAL
galaxy property, not local acceleration.
Structural finding: all V9.4 projectors are built from log-slopes/ratios —
scale-invariant BY CONSTRUCTION — hence blind to absolute surface density.
Paper XXIV licenses the fix (running κᶜ with energy density).
Internal-scalar replacement test: log(theta) correlates with logSB (r=0.76)
but predicts the miss poorly (R²=0.07 vs 0.33 photometric). Miss tracks the
SB component orthogonal to dynamical depth → suspect the TARGET.

## Step 3 — Global mass-to-light recalibration (target side)
Joint grid over (Y_disk, Y_bul), 5-fold CV by galaxy (seed=42):
- ALL FIVE FOLDS independently select Yd=0.475, Yb=0.35 (perfect stability)
- OOS RMS = 24.360 (baseline 30.550)
- f_bul residual correlation: -0.43 -> +0.006  (bulge structure FULLY
  explained by Y_bul recalibration)
- remaining: logSB r=-0.406, f_gas +0.262
Stacked Y-recal + SB multiplicative law (4 global params total):
- OOS RMS = 22.023   (30.550 -> 22.023, -27.9%)

## Flags (honesty)
1. Y_disk=0.475 ≈ canonical 0.5 (reassuring). Y_bul=0.35 is HALF the SPARC
   convention (0.7) and astrophysically low for old bulge populations at
   3.6um. Two readings: (a) true M/L lower than convention, or (b) Y_bul is
   absorbing a projector systematic in high-curvature inner regions.
   Discriminator (future): check whether improvement concentrates at small
   radii in bulge galaxies.
2. Forking-paths caveat: all structure was discovered and validated on the
   same 175 galaxies. CV protects against overfit but not against
   sample-specific systematics. Final claims should be tested on
   independent rotation-curve samples (e.g., LITTLE THINGS) before
   publication.
3. Remaining derivation target: the post-Y SB correlation (-0.406) is the
   true projector-side miss. Scale-blind projector family cannot capture
   it; running-κᶜ term is the framework-native candidate.

## Session bottom line
30.550 -> 22.023 km/s OOS, four global parameters, zero per-galaxy freedom,
fold-stable, provenance clean (all data from user uploads).

## Step 4 — Boundary ("glass") sensitivity sweep [purity-preserving, velocity-only]
Canonical predictor reverted to velocity-only (SB law demoted to appendix);
headline chain = Y-recal only: OOS 24.360. Noise floor from SPARC errV:
~8.2 km/s (realistic 8-12 after error propagation) => ε budget ≈ 22 km/s.

Exterior assumption varied (all galaxies uniformly):
  ext=20x, r^-2.0 (baseline): 24.360
  ext=5x: 30.378 | ext=50x: 23.887 | r^-1.5: 34.471 | r^-2.5: 40.340
Findings:
- Boundary is LOAD-BEARING: global optimum near Keplerian r^-2, long horizon.
- |per-galaxy shift| vs |residual|: r=+0.55 (p=5e-15) — the residual-heavy
  galaxies ARE the boundary-sensitive ones (balloon hypothesis consistent).
- BUT signed shift vs signed residual: r=+0.06 — a UNIFORM glass change
  cannot close individual galaxies. Per-galaxy exterior variation remains
  the viable ε carrier.
- Caveat: |shift| correlations with SB (+0.71) use absolute km/s; recheck
  with fractional shift (scales with v_max).
Proposed ε parametrization (next): per-galaxy effective tail exponent
ε_g = deviation of exterior profile from Keplerian vacuum. One number per
galaxy, boundary-localized (XXV-consistent), physically interpretable,
fit as DIAGNOSTIC then regressed against environment observables.

## Step 5 — ε_g audit, round 1 (internal observables, split-sample)
ε_g := per-galaxy effective exterior tail-exponent deviation from Keplerian
(fit range 1.2–3.2, err-weighted; 4% at bounds — well-posed).
Diagnostic ceiling: RMS 22.45 -> 13.54 km/s; mean per-galaxy chi2 54 -> 12,
with ONE boundary parameter per galaxy. (Now comparable to MOND-family
per-galaxy M/L fits at equal parameter count.)
Split audit (seed=20260703, halves 87/88):
  REPEATS: logSB +0.46/+0.45 | f_gas -0.44/-0.50 (both halves p<1e-4)
  Blanks PASS: dist, N, errV-quality all null in both halves.
Sign check: gas-rich galaxies prefer SHALLOWER exteriors (ε<0) — the exact
signature predicted by extended-HI-envelope mechanism ("glass bigger than
measured region"). High-SB prefer steeper (more sealed). Consistent with
envelope hypothesis; still confounded with internal-physics reading until
external HI extents (R_HI/R_opt) are pulled and tested at fixed SB.
Next: external catalog pulls (HI extents, tidal indices) with provenance.

## Step 6 — External pull #1 + pre-registered envelope test [FAILED — recorded]
Provenance: SPARC master table (Table1/SPARC_Lelli2016c.mrt), pulled
2026-07-04 from github.com/amidou/amiga-xmatch mirror; MD5
6181df386bfc05868a3700c196e800da verified IDENTICAL to official Zenodo
archive (record 16284118). Columns used: RHI, MHI, Inc, Q, T, Rdisk.

Pre-registered prediction (logged before pull): envelope mechanism =>
eps_g anti-correlates with HI extent at fixed SB, both halves.
RESULT: SIGN REVERSAL on primary measure. eps ~ RHI/rmax | SB = +0.315
(p=3e-5), repeats in both halves (+0.35/+0.26) and in clean Q=1,i>=45
subsample (+0.32). Secondary measure (RHI/Rdisk) weakly negative but does
not repeat in discovery half. PREDICTION FALSIFIED as stated.
Blank partially failed: eps ~ inclination +0.217 (p=0.004) full sample;
drops to +0.13 (n.s.) in clean subsample => part of eps_g absorbs
inclination-linked systematics; not all (SB axis STRENGTHENS to +0.64 in
clean subsample).
Verdict (V9.5-style): the "extended HI envelope" identification of eps_g
is rejected in its simple form. The dominant eps_g axis is the SB axis,
which sharpens in the best data — consistent with INTERNAL physics
(scale-blind projector / running-kappa) rather than exterior structure.
The positive RHI/rmax sign (more unmeasured gas disk => steeper fitted
tail) is unexplained; candidate reading: eps_g compensates curve
truncation, not physical exterior. Flagged for theory, not rescued.
