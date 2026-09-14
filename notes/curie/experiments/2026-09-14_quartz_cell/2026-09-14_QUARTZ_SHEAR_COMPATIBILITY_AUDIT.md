# 2026-09-14 Research — Quartz Shear Compatibility and the Limit of Perfect Rigidity

**Status:** EXECUTED COMPATIBILITY AUDIT / NEGATIVE RESULT FOR AN EXACT RIGID-UNIT REDUCTION. NOT AN ARK VALIDATION OR A PREDICTED ATOMIC DISPLACEMENT FIELD.

**Starting checkpoint:** `f3035c02d828cf568e2398fa0234b2cc78c642b5`, branch `workspace/curie`.

**Scope:** The compatibility-first test marked pending in this folder's checkpoint README is now executed. Other pending steps, including microscopic force constants and Born-charge response, remain pending.

**Code:** [quartz_shear_compatibility.py](./quartz_shear_compatibility.py). Requires the unchanged [quartz_cell_audit.py](./quartz_cell_audit.py), Python 3.10+, and NumPy. Run `python quartz_shear_compatibility.py --out compatibility_results`.

## 1. Question and conclusion

Can the three infinitesimal deformation directions of our perfectly rigid, corner-connected SiO4 model reproduce the homogeneous, zero-mechanical-stress piezoelectric strain predicted by the previously imported quartz material tensors?

**No.** After an explicit material-convention registration, the nearest compatible strain leaves a **0.4130288732 relative tensor-norm residual** for the selected AT-oriented field. The same relative mismatch occurs for the X and Y field controls. This is a model-to-model compatibility result, not a measurement uncertainty, quartz-frequency error, fraction of atoms, current fraction, or energy loss.

Releasing the internal tetrahedral-angle restriction while preserving all Si–O bond lengths at first order makes the target strain kinematically attainable. That diagnoses a specific restriction to remove: **perfect tetrahedral shape preservation is too strong for this static material control**. It does not establish a force law or validate an arbitrary added freedom.

No stiffness, piezoelectric coefficient, coordinate, direction, frequency, or nonlinear term was fitted to reduce the mismatch. The closest-strain projection is a diagnostic of incompatibility, not a prediction disguised as a fit.

## 2. Source registration: handedness is not just a sign to optimize

The inherited atomic basis is IUCr's dextro P3221 quartz in the reverse z(+) setting [S1]. The inherited ANSYS material coefficients have the signs `c14<0`, `e11>0`, `e14<0` [S2]. The published COMSOL sign table associates that sign family with IRE left-handed quartz [S3]. ANSYS's comment describing an IEEE matrix format specifies the matrix ordering; it must not by itself be treated as proof of a particular crystallographic setting.

For this control we adopt the corresponding laevo, obverse r(+) structural description and leave all inherited material coefficients unchanged. The registration is:

```text
dextro z(+) -> inversion -> laevo z(-) -> rotate basal setting by 180 degrees -> laevo r(+)
```

The net transformation of the Cartesian coordinates is `M=diag(1,1,-1)`; in this lattice basis, fractional `z` is negated modulo one. This is an **enantiomorph plus setting conversion**, not a proper rotation of the same physical specimen.

As an independent coordinate check, we generate laevo z(-) directly from S1 Tables 3 and 5, then apply its Table 8 basal-setting conversion. This reproduces the registered basis to `1.11e-16` in fractional coordinates. Inherited atomic labels remain our labels, not labels assigned to atoms in the separate X-ray experiment.

The sign-family registration is an inference from the cited convention tables, not a new measurement of a resonator's handedness. No actual specimen or twin-domain identification is available. To ensure the conclusion does not depend on merely favoring a sign choice, the code also transforms the whole comparison back into the original dextro geometry, including all material tensors and the electric field. The relative residual is unchanged to `6.11e-16`.

Deliberately combining the original dextro geometry with the untransformed inherited tensor signs gives a larger **0.67261035** residual. That mismatched combination is retained as a negative convention control, not used as the main result.

## 3. What was held fixed

The initial nine-atom coordinates, lattice dimensions, neighbor connectivity, elastic constants, piezoelectric constants, and engineering-shear convention are unchanged from the first-construction package, apart from the explicitly stated enantiomorph/setting registration.

The old source SHA-256 is checked at runtime:

```text
593b2f441a3f6c0c8e71e06b81138a50be8687f1538bbde66466393cc39d44f5
```

The implemented strain vector is:

```text
s = (Sxx, Syy, Szz, 2Syz, 2Sxz, 2Sxy).
```

The target is `s_control = inverse(C) e^T E` at zero imposed mechanical stress. It is a conventional, homogeneous, linear material-point response, not the complete displacement or stress distribution of an electroded resonator. The specified field is:

```text
E = 100000 * (0, cos(35.25 degrees), sin(35.25 degrees)) V/m
```

in the registered material-control frame. This normalization is not a proposed operating voltage or a damage test. The response lies in the X/Y electrically active subspace; the Z field gives zero strain in this linear tensor control, so no relative-error percentage is assigned to that zero target.

## 4. Compatibility method and a compact mechanical diagnosis

Use 27 non-affine atomic displacement components plus six symmetric homogeneous cell strains. Preserve four Si–O and six O–O distances for each of the three tetrahedra. Fix three overall translations. The resulting matrix has rank 30 in 33 variables, reproducing the three-dimensional infinitesimal compatible space from the earlier calculation.

For each constrained bond with reference vector b, impose:

```text
b_hat dot (u_j - u_i + S b) = 0.
```

The three-dimensional space has a three-dimensional image in strain space. Its strain relations in the registered frame simplify to:

```text
s3 = 0.7841810009 * (s1 + s2)
s4 = 0.6576782646 * (s1 - s2)
s5 = 0.6576782646 * s6.
```

These are consequences of the declared exact geometric constraints for these coordinates, not fitted response laws.

For the selected field, only s5 and s6 of the conventional target are nonzero:

```text
s5_control = -5.9257109209e-8
s6_control = -3.7682421114e-7
s5_control / s6_control = 0.1572539860.
```

But exact rigidity requires a ratio of **0.6576782646**, not **0.1572539860**. Changing the overall amplitude cannot fix that ratio. No choice of forces within the exactly constrained space can produce a strain that lies outside it.

That identifies the failure before any microscopic stiffness fitting: the allowed geometric motion ratios do not contain the specified bulk shear.

## 5. How the 41.3% mismatch was measured

Let N span the nullspace of the full compatibility matrix and let B be its six strain rows. The closest compatible strain solves:

```text
min_a || W (s_control - B a) ||_2
W = diag(1,1,1,1/sqrt(2),1/sqrt(2),1/sqrt(2)).
```

The weights convert engineering shear to a norm equal to the full symmetric strain tensor's Frobenius norm. An unweighted norm of engineering Voigt components would not be invariant under arbitrary rotations.

Define the diagnostic:

```text
eta_incompatible = min_a ||W(s_control-B a)|| / ||W s_control||.
```

This eta is a dimensionless audit label only; it is NOT the viscosity variable used in V9.5.

For the AT-oriented control, the nearest compatible strain has:

```text
s5_nearest = -1.9089175252e-7
s6_nearest = -2.9025096736e-7
```

The remaining components are numerical roundoff. The normalized residual is **0.4130288732425296**, corresponding to a **24.39524644-degree angle in strain-coordinate space**, not a bond angle or physical crystal-cut rotation.

The X, Y, reversed-AT, and doubled-AT field controls return the same fractional mismatch. Doubling or reversing the drive therefore cannot remove this geometric incompatibility in the linear approximation.

## 6. Numerical and convention guards

| Check | Result |
|---|---:|
| Rigid-unit nullspace residual | 1.48e-15 |
| Constraint Jacobian versus central finite difference, maximum difference | 7.01e-11 |
| Equivalent mirrored material description, residual difference | 6.11e-16 |
| Sixteen arbitrary proper rotations of geometry, tensors, and field together, largest residual difference | 7.77e-16 |
| Permuting constraint rows, residual difference | 0 |
| Rescaling translation-gauge rows, residual difference | 1.67e-16 |
| Neighbor cutoffs 1.7, 1.8, 1.9 angstrom | Same connectivity and residual |
| One hundred symmetry-preserving prototype-coordinate rounding probes | Residual 0.41240816 to 0.41370071 |

The rounding probes vary each printed prototype coordinate by at most half of its final printed decimal place, using a fixed random seed. They are a sensitivity check, NOT confidence intervals or sampled experimental uncertainties. Material-coefficient uncertainty and covariance have not been characterized here.

The result is not rescued by the tested numerical conventions, rotations, or input rounding. This does not constitute a proof for every possible quartz structure or specimen.

## 7. Controlled relaxation: shape rigidity, not necessarily Si–O stretching

A second calculation retains all 12 Si–O length constraints and removes the O–O distance constraints that had fixed the internal O–Si–O angles. The rank including translation gauge falls to 15, leaving 18 compatible coordinates. Their strain image has rank six: all infinitesimal homogeneous strains are kinematically accessible in this relaxed model.

The same target can now be represented to a relative tensor-norm residual of **7.82e-16**. This is **not** a newly correct ARK prediction: extra freedoms have been allowed, and the target is supplied to the compatibility test. It shows only that permitting internal angular deformation removes this particular obstruction.

To estimate a possible magnitude of the required shape changes, we hold the target strain fixed, retain exact first-order Si–O lengths, and minimize the sum of squared fractional O–O distance changes. This is a declared geometric selector, not an inferred microscopic energy or force law.

For that one target-conditioned representative:

- Maximum fractional Si–O change: `2.48e-22` (roundoff).
- RMS fractional O–O change: `3.8368e-8`.
- Maximum fractional O–O change: `5.9662e-8`.
- Maximum absolute internal O–Si–O angle change: `9.8657e-6 degrees`.

The non-affine atomic coordinates for this representative are stored in the full generated results and labeled **not predicted motion**. With only Si–O lengths and strain fixed, 12 internal freedoms remain before this additional selector is imposed.

Thus failure of exact rigidity does not imply large atomic distortion, damage, or identity loss. Even tiny internal angular changes can matter to a strain-ratio test when the total applied strain is itself tiny. Nor does this establish that Si–O lengths remain exactly fixed in real driven quartz; finite bond-stretch response must eventually be included or bounded.

## 8. Relation to the experimental motivation and ARK

The X-ray account motivating the first construction describes relatively unchanged intra-tetrahedral geometry within measurement uncertainty and a larger role for inter-tetrahedral angle changes [S4]. That does not justify infinite stiffness. Our test concerns a static imported tensor response, not the same resonant specimen, drive, or measured atom-by-atom trajectory. We have not calculated experimental resolution or shown that the small illustrative angle changes would or would not be detectable in that experiment.

The refinement is:

```text
relatively stiff structural units + coupled angular response
```

rather than:

```text
perfectly rigid units are an exact complete model.
```

This is compatible with investigating the ARK principle of finite resistance to reconfiguration. It is not evidence for aether channels, channel recruitment, field-flow localization, a derived bond force, quantum outcome selection, or unification with gravity. The field and microscopic electrical response have still not been solved from an ARK substrate law.

The earlier three-direction result remains correct for its specified constraints. Its interpretation is now narrower: it is an idealized geometric limit that does not reproduce the entire static piezoelectric strain control.

## 9. What is now next

The compatibility-first checkpoint has done its job. Do not tune the rigid constraints to the target or treat the relaxed feasibility fit as the new solver.

The next physical model needs finite internal deformation costs and consistent electrical coupling: interatomic force constants, internal-strain coupling, Born effective charges, and clamped-ion contributions in one registered basis. These should determine the atomic response through the same energy, rather than choosing one from the many compatible displacements by an arbitrary norm.

Near a reference configuration, a finite-stiffness representation can be organized around bond-length and angular changes. Its coefficients must be derived or independently constrained; none are supplied by this audit. The construction can then recover the rigid-unit limit when internal deformation costs are large, while permitting the small shape changes needed by the current control.

No new resonance frequency, damping rate, heat production, irreversible change, or substrate flux was computed in this pass.

## 10. Reproducibility and files

New source SHA-256:

```text
41a64ef80eae89e79903e39a1b79161e0ea6347af5f26214c248e188f83ebf4e
```

Full generated `compatibility_results/results.json` SHA-256 for this run:

```text
f84627e8bdf4eea7320333e848dbb8998bb8c914a6d788784ffd1f549fbf51c2
```

The script generates the complete nullspace, strain projector, registered coordinates, control tensors, field tests, illustrative displacement representative, and diagnostic checks in `results.json`, plus `comparison.csv`. The accompanying download package preserves those full outputs and the exact source dependency. Floating-point roundoff and file hashes may differ across NumPy/platform versions; the dimensional, symmetry, and tolerance-based checks are the substantive reproducibility criteria.

The old script and first-construction notes are unchanged. This record narrows the earlier perfect-rigidity interpretation and advances the checkpoint, rather than rewriting its history.

## Sources

S1. Sutter et al. (2022), *Calculating temperature-dependent X-ray structure factors of alpha-quartz with an extensible Python 3 package*, DOI 10.1107/S1600576722005945. Sections 2, 4, 5; Tables 3, 4, 5, 8. https://journals.iucr.org/j/issues/2022/04/00/te5094/

S2. ANSYS Coupled-Field Analysis Guide, section 2.3.7, Table 2.15 and matrix listing, material constants attributed to Ballato (2008). Only the previously imported real elastic and piezoelectric inputs are used; no assumed losses or resonance outputs are fitted. https://ansyshelp.ansys.com/public/Views/Secured/corp/v261/en/ans_cou/Hlp_G_COU3_piezo.html

S3. COMSOL, *Piezoelectric Material Orientation*, sign table and IRE/IEEE cut conventions. https://doc.comsol.com/6.4/doc/com.comsol.help.sme/sme_ug_modeling.05.108.html

S4. Aoyagi and Takeda (2022), *Transient Crystal Structure of Oscillating Quartz*, DOI 10.5772/intechopen.107414, authors' account of time-resolved diffraction work. https://www.intechopen.com/chapters/83792

Sources checked 2026-09-14. The geometric incompatibility and relaxation calculations above are new model calculations; the cited sources supply inputs and experimental context, not these numerical findings.
