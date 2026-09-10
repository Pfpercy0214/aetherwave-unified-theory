# XXVI V5.4 Legacy Audit — Zero-Parameter Baryonic Retrodiction

**Status:** LEGACY / PUBLISHED RESULT WITH KNOWN POST-PUBLICATION IMPLEMENTATION FLAW  
**Historical source:** `XXVI Zero-Parameter Baryonic Retrodiction from Scalar Geometry.pdf` (March 2026)  
**Correction source:** Zenodo record summary/notes — pending retrieval when Zenodo is available.

## Why preserve this paper

This paper should remain intact as provenance. It records what was actually published before a later implementation flaw was recognized. The purpose of this note is not to silently repair the paper but to separate the historical result from the current epistemic status.

## Published claims

The paper reports the ARK V5.4 inverse solver as a zero-free-parameter retrodiction of baryonic velocity from observed SPARC rotation curves. It reports 175 galaxies, 167/175 convergence, global RMS 34.8 km/s, and global Pearson r = 0.8922 for the core solver. It also presents environmental-entropy extensions and several negative full-PDE variants.

The paper explicitly characterizes several solver implementation choices as non-free-parameter numerical devices, including bounded regularization of `k^c`, adaptive smoothing, damping/convergence behavior, and a 20x radial boundary extension.

The published interpretation then argues that the remaining residual ceiling is primarily limited by the quality of SPARC baryonic decomposition rather than by missing framework physics.

## Known post-publication flaw

Paul later discovered that a solver hyperparameter / numerical constraint created an **artificial wall in the solution space**. The effect was not ordinary parameter tuning toward a desired result. Instead, the implementation forced apparently perfect or near-perfect answers for roughly 60–70% of the galaxy sample by driving solutions against the artificial constraint.

This means the apparent agreement for that subset cannot be treated as independent evidence for the physical framework. A numerical boundary that forces an output into the target region is an implementation artifact even if the parameter was not fitted per galaxy.

**Important:** The exact offending hyperparameter, its code path, and quantitative effect should not be reconstructed from memory. Add the exact mechanism from the Zenodo correction and/or archived solver code when available.

## Claims whose status changes immediately

Until the correction is recovered and the solver is reproduced without the artificial wall, do **not** treat the following published statements as established:

- that V5.4's reported global performance is a clean zero-parameter test of ARK;
- that its convergence fraction demonstrates physical closure;
- that the residual ceiling is demonstrably imposed primarily by SPARC input quality;
- that improving beyond the reported ceiling requires better data rather than a changed numerical treatment;
- that solver regularization/bounds are empirically innocuous;
- or that apparently exact/perfect galaxy-level solutions are evidentiary.

The paper remains useful for:

- documenting the historical solver architecture;
- preserving negative variants;
- identifying numerical choices that require independent audit;
- showing the development path toward later galaxy solvers;
- and providing a concrete example of why `zero fitted parameters` is not equivalent to `zero structural/numerical degrees of freedom`.

## Why this is not the same as ordinary tuning

The distinction should be explicit in future summaries:

```text
Tunable-fit failure:
    choose a parameter value to move predictions closer to the target.

Artificial-wall failure:
    impose a numerical constraint that restricts the solver's accessible
    state space so strongly that many outputs are mechanically driven to
    an apparently correct boundary/solution.
```

The second can be especially deceptive because the solver may still contain no per-object fitted parameter while the architecture itself strongly determines the answer.

## Relation to later galaxy work

Later galaxy work should be evaluated independently rather than inheriting either the success claims or failure mode of V5.4. In particular, any later solver must document:

- all clipping, saturation, floors, ceilings, damping, smoothing, boundary extensions, convergence criteria, normalization, and initialization;
- whether solutions accumulate at numerical boundaries;
- ablations with each guard removed;
- sensitivity to numerical choices;
- and whether the target quantity enters directly or indirectly into any guard or stopping behavior.

## Pending provenance update

When Zenodo is available, add verbatim-enough metadata (without overwriting this historical record) for:

1. date the correction/admission was posted;
2. exact affected hyperparameter / numerical wall;
3. fraction of galaxies affected and how that fraction was calculated;
4. corrected interpretation of the published V5.4 metrics;
5. link/DOI/version metadata for the public correction;
6. any corrected/re-run solver results, if supplied.

This note should then point to the correction as the authoritative statement of what failed.
