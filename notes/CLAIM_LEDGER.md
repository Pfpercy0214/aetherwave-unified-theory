# CLAIM_LEDGER — hot results with status labels

**Dated:** 2026-09-10  
**Rulebook:** [`EPISTEMIC_DISCIPLINE.md`](EPISTEMIC_DISCIPLINE.md)  
**Artifact homes:** cited by branch/path — not necessarily present on `workspace/gwok`.

Update this file whenever a number or thesis is quoted in chat or papers.

## Galaxy / SPARC

| Claim | Approx. value | Label | Where | Notes / falsifier |
|-------|---------------|-------|-------|-------------------|
| **V5.4 inverse solver** (SPARC retrodiction) | Summary: r≈0.89, RMS≈34.8; reported 167/175 “converged” | **NEGATIVE RESULT / CLOSED FOR ORIGINAL INTENT** | `ARK-GAL-1D-5.4` | Inverse: v_obs → v_bar; α=4π/3 claimed derived; Υ 0.5/0.7. **Paul’s operational read (authoritative over glossy summary):** only ~**34 true convergences** before **forced perfect closure** on the remainder; last **six** missed consistently; best-case correct enclosure ~**30%**. Do **not** cite summary converged-count or RMS as a catalog win. Failure path → 9.x. |
| Raw V9.4 `mixed_slope` global RMS | ~30.55 km/s | **RAW RESULT** | `ARK-GAL-1D-9.4` (`model_comparison.csv`) | Forward projector; N=175, 3213 pts; Y_disk=0.5, Y_bulge=0.7 in target; no photometry in predictor |
| Raw V9.4 global correlation | r ≈ 0.91–0.92 | **RAW RESULT** | same | Strong shape correlation |
| κ_outer median / CV | ≈0.912 / ≈0.077 | **RAW RESULT** (structural regularity) | same | Stable across projectors — treat as claim only with cross-checks |
| residual_vs_logSB (raw) | ≈ −0.38 to −0.63 | **RAW RESULT** / open interpretation | same | SB sealed from predictor but residuals track log SB |
| Global Y recalibration OOS | ~24.36 km/s | **CALIBRATED RESULT** | `recovery/galaxy-artifacts` → `v9.4-audit-mid20s/` | Y≈0.475 / 0.35 — **not** raw V9.4 |
| Guarded / Stowe-style OOS | ~23.63–23.65 km/s | **COMPATIBLE BUT UNDERDETERMINED** | same audit folder | Exact Stowe form not identified; boundary-degenerate |
| V9.5 viscosity-shape ~10× radial rise | — | **NEGATIVE RESULT / CLOSED ROUTE** | `recovery/.../v9.5-negative-result/` | Guards: largely reconstruction artifact |
| Projection loss vs outside influence as residual story | — | **EXPLORATORY HYPOTHESIS** | discussion + notes | Needs discriminating tests before promotion |

**Lineage note:** V5.4 failure → later 9.4 (forward) / 9.5 (closed negative). Do not collapse inverse V5.4 RMS with forward 9.4 or mid-20s audit numbers.

## Theory / corpus

| Claim | Label | Where | Notes |
|-------|-------|-------|-------|
| GR/QM as calibration surfaces; medium mechanism underneath | **EXPLORATORY / PROGRAM THESIS** | XXIV, XXV, `FRAMEWORK.md` | XXIV more completionist; XXV more containment |
| Most “intrinsic” constants are condition-indexed; behavior portable | **EXPLORATORY HYPOTHESIS** | chat + XXV implications | **Not yet a paper page** |
| Measurement injects unrecorded perturbation (dSₜ); catalog values are composites | **EXPLORATORY HYPOTHESIS** | chat; neutron/XXV thread | Known unknown — not a free knob |
| Paper XX periodic-table near-perfect match | **DEPENDENT ON EXTERNAL/ESTIMATED CONDITIONS** (legacy presentation) | `XX Modeling Atomic Structure with ARKV2.pdf` | Estimated measurement conditions; looks like pasted perfection — do not cite as demonstration |
| Paper XX shared-environment congruency rescue | **EXPLORATORY HYPOTHESIS** (proposed) | chat | Same T→dSₜ / boundary for all Z; label as internal congruency, not lab reproduction |

## How to cite

When summarizing to Paul or into a draft, carry the **label with the number**. Never say “we got ~23 km/s” without saying **CALIBRATED / guarded** vs **RAW ~30.55**. Never cite V5.4 as meeting the original galaxy-modeling bar; prefer Paul’s ~34 true / ~30% enclosure read over the summary’s 167/175 converged.
