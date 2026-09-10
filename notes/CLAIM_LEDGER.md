# CLAIM_LEDGER — hot results with status labels

**Dated:** 2026-09-10  
**Rulebook:** [`EPISTEMIC_DISCIPLINE.md`](EPISTEMIC_DISCIPLINE.md)  
**Artifact homes:** cited by branch/path — not necessarily present on `workspace/gwok`.  
**Work order:** [`WORK_QUEUE.md`](WORK_QUEUE.md) (three-body at top).

Update this file whenever a number or thesis is quoted in chat or papers.

## Galaxy / SPARC

| Claim | Approx. value | Label | Where | Notes / falsifier |
|-------|---------------|-------|-------|-------------------|
| **V5.4 inverse solver** (SPARC retrodiction) | Summary artifacts: r≈0.89, RMS≈34.8; reported 167/175 “converged” | **NEGATIVE RESULT / CLOSED FOR ORIGINAL INTENT** | `ARK-GAL-1D-5.4` | Inverse: v_obs → v_bar; α=4π/3 claimed derived; Υ 0.5/0.7. Failure path → 9.x — **do not rerun**. Paul’s from-memory operational caveat (~34 true convergences, forced closure, last six miss, ~30% enclosure) is **PROVISIONAL** until the Zenodo result README is on the branch; then align ledger to that note. Do **not** cite summary converged-count as a catalog win. |
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
| Three-body / full matter–substrate program | **HIGH-PRIORITY EXPLORATORY / NOT ESTABLISHED** | Curie `…_STUDYING_THE_THREE_BODY…`; [`WORK_QUEUE.md`](WORK_QUEUE.md) §1 | Upstream accuracy driver for 2D–3D; figure-eight = control only |
| Matter–substrate forward coupling architecture (`E_ARK = C_static + C_reactive + C_dissipative`) | **CANDIDATE CONSTITUTIVE ARCHITECTURE / NOT A LAW** | Curie `2026-09-10_MATTER_SUBSTRATE_FORWARD_COUPLING_FORMALIZATION.md` | No coefficients; uniform-motion null; momentum reciprocity; first bench = one accelerated body |
| Gravity-map lineage: `(θᶜ)² = 2\|Φ\|/c²` vs `Φ := θᶜ c²` | **OPEN LINEAGE / AUDIT ISSUE** | XXIV vs later galaxy bridge; Curie three-body §11 | Must reconcile before paper-grade three-body / action claims |
| Quadratic `θᶜ` N-body compatibility | **COMPATIBLE / DEPENDENT ON EXTERNAL NEWTONIAN U** | Curie three-body §2–3 | Change-of-variable, not independent derivation |
| Substrate “near-superfluid / low dissipation + strong collective response” | **EXPLORATORY ANALOGY / HYPOTHESIS** | Coupling formalization §2, §11 | Not established ARK fluid equations |
| Inertia as resistance to coherent reconfiguration (not drag) | **EXPLORATORY HYPOTHESIS** | Coupling formalization §9, §17–18 | Needs frozen law + one-body momentum ledger |
| GR/QM as calibration surfaces; medium mechanism underneath | **EXPLORATORY / PROGRAM THESIS** | XXIV, XXV, `FRAMEWORK.md` | XXIV more completionist; XXV more containment |
| Most “intrinsic” constants are condition-indexed; behavior portable | **EXPLORATORY HYPOTHESIS** | chat + XXV implications | **Not yet a paper page** |
| Measurement injects unrecorded perturbation (dSₜ); catalog values are composites | **EXPLORATORY HYPOTHESIS** | chat; neutron/XXV thread | Known unknown — not a free knob |
| Paper XX periodic-table near-perfect match | **DEPENDENT ON EXTERNAL/ESTIMATED CONDITIONS** (legacy presentation) | `XX Modeling Atomic Structure with ARKV2.pdf` | Estimated measurement conditions; looks like pasted perfection — do not cite as demonstration |
| Paper XX shared-environment congruency rescue | **EXPLORATORY HYPOTHESIS** (proposed) | chat | Same T→dSₜ / boundary for all Z; label as internal congruency, not lab reproduction |

## How to cite

When summarizing to Paul or into a draft, carry the **label with the number**. Never say “we got ~23 km/s” without saying **CALIBRATED / guarded** vs **RAW ~30.55**. Never cite V5.4 as meeting the original galaxy-modeling bar. Prefer Paul’s operational caveat once the Zenodo README lands; until then treat ~34 / ~30% as **from-memory provisional**, not frozen ledger truth. Never cite figure-eight closure as ARK newly solving three-body. Never cite the coupling formalization as an established constitutive law.
