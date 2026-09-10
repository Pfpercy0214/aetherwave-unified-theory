# ARK-GAL-1D-9.4

**Version 9.4 offshoot of [`galaxy-1d`](https://github.com/Pfpercy0214/aetherwave-unified-theory/tree/galaxy-1d).**

This branch is the home for the **ARK V9.4** 1D scalar-geometry projector runs (SPARC), not a separate repository. It was created from `galaxy-1d` when the v9.4 materials were uploaded.

## Lineage

```text
main
 └── galaxy-modeling
      └── galaxy-1d
           └── ARK-GAL-1D-9.4   ← you are here (v9.4)
```

Sibling / office branches: `workspace/gwok` (corpus organization), `Papers` (early paper set).

## v9.4 modeling artifacts (this version)

Method note: *ARK V9.4 scalar-derived geometry projector test*

| File | Role |
|------|------|
| `ark_v94_scalar_geom.txt` | Run / method log |
| `ark_v94_scalar_geom_stdout.txt` | Stdout capture |
| `v94_summary.txt` | Per-projector summary (r, RMS, residuals, κ, F) |
| `model_comparison.csv` | Cross-model comparison table |
| `*_galaxy_info.csv` + `*_scatter.png` | Per projector: `const_1_2`, `const_1_3`, `theta_slope`, `kappa_slope`, `mixed_slope`, `div_partition` |

Summary snapshot from `v94_summary.txt` (175 galaxies, 3213 radial points): global RMS roughly **~30.6–33.0 km/s** across projectors in this dump (best in-file: `mixed_slope` / `kappa_slope` / `theta_slope` near ~30.5–30.7).

## About the theory PDFs on this branch

Root still contains the inherited paper corpus from `main` / `galaxy-1d`. Those are **not** part of the v9.4 modeling package — they came along because the branch was cut from a paper-heavy tip. Treat this branch’s *purpose* as the v9.4 artifacts above; we can tidy layout later without deleting anything unless Paul says so.

## Ground rules

1. **No deletes without Paul’s explicit OK.**
2. Version branches stay specific (9.4 here); newer versions get their own offshoot off `galaxy-1d`.
3. Residual interpretation: keep projection loss vs outside influence as separate hypotheses.

---

*ARK GAL 1D v9.4 — versioned offshoot under galaxy-1d.*
