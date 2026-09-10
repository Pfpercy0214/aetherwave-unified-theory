# Recovered galaxy-modeling artifacts

This directory restores prior ARK/SPARC analysis artifacts recovered from earlier project sessions without modifying the raw `ARK-GAL-1D-9.4` branch.

The material is deliberately split into two provenance families:

- `v9.4-audit-mid20s/` — post-V9.4 audit, target recalibration, residual analysis, and guarded bridge work. This is where the ~24.36 km/s and ~23.6 km/s results belong. They are not the untouched V9.4 projector result.
- `v9.5-negative-result/` — V9.5 viscosity-shape experiment, guards, autopsy, and closed negative-result record. V9.5 is not the source of the original mid-20s RMS result.

Canonical result labels:

- Raw V9.4 mixed-slope projector: ~30.55 km/s RMS against the standard SPARC baryonic target used in that package.
- V9.4-derived global Y recalibration (`Y_disk=0.475`, `Y_bulge=0.35`): ~24.36 km/s OOS.
- Guarded V9.4/Stowe-style radial-response tests: ~23.63–23.65 km/s OOS, but the exact Stowe form is not identified and is boundary-degenerate.
- V9.5 viscosity-shape observable: CLOSED negative result after synthetic/null guards showed the apparent ~10x radial rise was largely reconstruction artifact.

## Recovery completeness

Recovered source/record files are preserved under the folders below. Two output filenames referenced by `stowe_v95_comparison.md` were not present in the saved Library at recovery time and are therefore **not reconstructed or invented**:

- `stowe_v95_guard_output.txt`
- `v95_autopsy_repro.txt`

Their substantive findings are preserved in the recovered comparison/guard records.

Do not collapse these folders into a single version label when citing results. Historical raw branches remain authoritative for their original runs; this recovery branch exists to restore later analysis provenance.
