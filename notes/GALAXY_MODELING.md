# GALAXY_MODELING — status

**Dated:** 2026-09-10 (updated after `recovery/galaxy-artifacts` landed)  
**Raw v9.4 package:** `ARK-GAL-1D-9.4`  
**Recovered later analysis:** `recovery/galaxy-artifacts` → `modeling/galaxy/recovered/`

## Branch lineage

```text
main
 └── galaxy-modeling
      └── galaxy-1d
           └── ARK-GAL-1D-9.4          # raw v9.4 projector package (~30.55 RMS)

workspace/gwok  (office + notes)
recovery/galaxy-artifacts              # Curie/Paul recovery: mid-20s audit + v9.5 negative result
  └── modeling/galaxy/recovered/
        ├── v9.4-audit-mid20s/
        └── v9.5-negative-result/
```

## Canonical result labels (do not collapse)

From `modeling/galaxy/recovered/README.md` on `recovery/galaxy-artifacts`:

| Label | Approx. RMS | What it is |
|-------|-------------|------------|
| **Raw V9.4** `mixed_slope` | **~30.55 km/s** | Untouched projector vs standard SPARC baryonic target in the `ARK-GAL-1D-9.4` package |
| **V9.4-derived global Y recalibration** | **~24.36 km/s** OOS | `Y_disk=0.475`, `Y_bulge=0.35` — post-V9.4 audit, **not** raw V9.4 |
| **Guarded V9.4 / Stowe-style radial-response** | **~23.63–23.65 km/s** OOS | Guarded tests; exact Stowe form not identified; boundary-degenerate |
| **V9.5 viscosity-shape** | — | **CLOSED negative result** — apparent ~10× radial rise largely reconstruction artifact (synthetic/null guards) |

**This reconciles the earlier ~23–25 vs ~30+ confusion:** mid-20s numbers are **audit / recalibration / guarded** lineages; ~30.55 is the **raw projector** result.

## Raw V9.4 package (`ARK-GAL-1D-9.4`)

**N = 175 galaxies, 3213 radial points.** No photometry in predictor; Y_DISK=0.5, Y_BULGE=0.7 in target.

| projector | global_r | global_rms_kms | residual_vs_logSB_r |
|-----------|----------|----------------|---------------------|
| const_1_3 | 0.915 | 32.98 | −0.627 |
| const_1_2 | 0.911 | 31.99 | −0.383 |
| theta_slope | 0.918 | 30.73 | −0.568 |
| kappa_slope | 0.921 | 30.63 | −0.581 |
| **mixed_slope** | 0.921 | **30.55** | −0.580 |
| div_partition | 0.911 | 31.99 | −0.383 |

`kappa_outer_median ≈ 0.912`, CV ≈ 0.077. `const_1_2` ≈ `div_partition` (investigate).

## Recovered folders (`recovery/galaxy-artifacts`)

### `v9.4-audit-mid20s/`
Toolkit / harness / Stowe bridge notes / CV CSVs / SB correction record / comparison md. **Home of the ~24.36 and ~23.6 results.**

### `v9.5-negative-result/`
Negative-result record (docx), viscosity/relax/autopsy/guard scripts + repro text. Two filenames referenced but **not** in Library at recovery (not invented): `stowe_v95_guard_output.txt`, `v95_autopsy_repro.txt` — findings preserved in comparison/guard records.

## Open questions

| Issue | Status |
|-------|--------|
| 23–25 vs 30+ | **Reconciled in labels** — cite which lineage |
| residual_vs_logSB on raw V9.4 | Still open on raw package |
| const_1_2 ≈ div_partition | Still open |
| Stowe form identity | Unidentified; boundary-degenerate per recovery README |
| Merge recovery into `galaxy-1d` / version branches | Not done — recovery branch is provenance home for now |

## Norms

- Zero articulation in core projector; label Y-recal / guards as calibration/experiment.
- Do not cite mid-20s as “raw V9.4.”
- No deletes without Paul’s OK.
