# 2026-09-11 Research — Quartz Spatial Channel Null Model

**Status:** PRE-ARK SPATIAL NULL TEST / CHANNEL-EMERGENCE GUARD — NOT AN ARK ONTOLOGY VALIDATION  
**Research date:** 2026-09-11  
**Purpose:** Test the concern that a mathematically convenient uniform-flow assumption could manufacture agreement. The narrow question is whether the declared quartz/electrode geometry, by itself, naturally produces a strongly localized electrical/field pathway, or whether a channel must be added through additional material state, anisotropy, heterogeneity, or nonlinear coupling.

Companion records:

- `2026-09-11_QUARTZ_BENCHMARK_METHOD_THEORY_RESULT_FREEZE.md`
- `2026-09-11_QUARTZ_THICKNESS_SHEAR_FIRST_PASS_BENCHMARK.md`
- `2026-09-11_QUARTZ_3D_EXTENSION_AND_OVERTONE_PRECOMPARISON.md`
- `2026-09-11_QUARTZ_OVERTONE_FIRST_COMPARISON.md`
- `2026-09-11_TAU_OMEGA_AS_EXPRESSIONS_OF_BEHAVIOR.md`

---

## 1. Modeling guard

The new rule is:

> **Do not prescribe the channel. Solve for the channel.**

A spatial mode, active radius, preferred pathway, or effective `k_perp` is not allowed to be selected because it reproduces the measured resonance.

The physical ordering should be

```text
material structure
+ electrode geometry
+ crystal orientation
+ boundary conditions
+ constitutive law
    -> spatial field / flux solution
    -> driven deformation / mode shape
    -> recurrence
    -> measured frequency.
```

The forbidden ordering is

```text
measured frequency
-> choose effective active region / channel
-> recover measured frequency.
```

---

## 2. Continuum least-resistance principle does not mean one path

For a linear passive medium, a generalized potential `Psi` and mobility/conductivity tensor `M` can be represented schematically as

```text
J = -M grad(Psi)
```

with conservation

```text
div(J) = 0
```

away from sources.

For fixed boundary potentials, the corresponding linear solution extremizes a global quadratic functional of the form

```text
F[Psi] = 1/2 integral (grad Psi)^T M (grad Psi) dV.
```

The important consequence is:

> **"Path of least resistance" in a continuous linear medium generally means a distributed solution over all available parallel paths, weighted by conductance. It does not automatically imply one narrow filament.**

Strong localization requires something additional, for example:

- spatial heterogeneity or defects,
- a large directional anisotropy,
- a geometric constriction,
- a nonlinear state-dependent mobility,
- a threshold / breakdown process,
- or positive feedback by which existing flow changes the medium and makes the same path easier to use.

This is directly relevant to the present ARK discussion. A localized substrate channel must emerge from specified mechanics; it cannot be inserted as a verbal interpretation of a smooth field solution.

---

## 3. Conventional calibration equations

For ordinary linear piezoelectric quartz, the coupled continuum problem is conventionally expressed as

```text
D = epsilon E + e : S
T = c : S - e^T E
E = -grad(phi)
```

with

```text
div(D) = 0
rho u_double_dot = div(T).
```

These equations are not claimed as ARK laws. They provide a calibration surface showing what a spatially resolved treatment must at minimum respect.

Published finite-element and plate treatments of AT-cut quartz explicitly solve mechanical displacement and electric potential together, include electric boundary conditions/electrode geometry, and recover resonance and mode shapes rather than assuming a uniform deformation field. Relevant references include:

- ANSYS AT-cut quartz piezoelectric benchmark: `https://ansyshelp.ansys.com/public/Views/Secured/corp/v252/en/ans_cou/Hlp_G_COU3_piezo.html`
- electroded quartz plate theory / FEM: `https://doi.org/10.1016/S0020-7683(99)00241-3`
- Cassiede et al. overtone study: `https://doi.org/10.1016/j.sna.2010.03.028`

The Cassiede study specifically emphasizes finite active area and energy trapping in real finite quartz resonators.

---

## 4. Stage-0 numerical null model

The first spatial test intentionally removes ARK-specific assumptions.

Use the already declared Q5-like geometry:

```text
blank diameter     = 13.6 mm
blank radius       = 6.8 mm
quartz thickness   = 335 um
electrode diameter = 6.7 mm
electrode radius   = 3.35 mm
```

Apply a normalized potential difference of 1 V between equal circular electrodes on the two major faces.

Stage 0 uses a homogeneous isotropic linear dielectric and solves the axisymmetric electrostatic boundary-value problem

```text
laplacian(phi) = 0
```

with:

```text
phi = +0.5 V on the top electrode,
phi = -0.5 V on the bottom electrode,
zero normal electric flux on unelectroded major-face regions,
zero radial flux at the outer blank edge,
axis symmetry at r = 0.
```

This is deliberately a null model. It asks whether finite electrode geometry alone creates a narrow internal path.

Numerical method:

- axisymmetric finite-difference discretization in `(r,z)`,
- mixed Dirichlet/Neumann boundary conditions,
- sparse linear solve,
- convergence check using `121 x 41`, `181 x 61`, and `241 x 81` grids.

No measured resonance frequency enters the calculation.

---

## 5. Stage-0 result

Let the ideal parallel-plate field scale be

```text
E0 = V/h.
```

At the crystal midplane, the solved axial field is essentially uniform through most of the electrode footprint and then rolls off near the electrode edge.

Across the grid-convergence study, the midplane field remains approximately:

```text
within 0.1% of E0 out to r ~ 3.0 mm,
within 1%   of E0 out to r ~ 3.1 mm,
within 5%   of E0 out to r ~ 3.2 mm.
```

For comparison, the electrode radius is

```text
R_e = 3.35 mm.
```

Using the midplane axial displacement/field flux as a radial weighting diagnostic:

```text
~94-95% of the integrated midplane flux lies inside the electrode radius,
95% cumulative flux occurs at r ~ 3.35-3.37 mm,
99% cumulative flux occurs at r ~ 3.53-3.56 mm.
```

Therefore the null result is:

> **Finite circular electrodes on an otherwise homogeneous linear dielectric do not spontaneously produce a narrow preferred channel. They produce a broad field column under the electrode with edge fringing.**

This is a useful negative result. It means a future ARK channel model cannot obtain microscopic localization merely by solving a symmetric homogeneous Laplace problem and then verbally reinterpreting the smooth field as a narrow path.

---

## 6. Quartz is not microscopically structureless

The null model is intentionally homogenized. Real alpha-quartz has genuine microscopic directional structure.

A modern mineralogical review describes alpha-quartz as a three-dimensional network of corner-linked `SiO4` tetrahedra arranged in helical chains along the crystallographic `c` axis, forming structural channels. These channels are real crystallographic features and can host/migrate small ions under appropriate conditions.

Reference:

`https://www.cambridge.org/core/journals/mineralogical-magazine/article/mineralogy-and-mineral-chemistry-of-quartz-a-review/68D0E3F05734D0E1B25F6A9A267B12EF`

This fact is **not evidence that electromagnetic energy or an ARK substrate literally flows through those channels**. It does establish that the material contains a physically real, repeated directional geometry that a microscopic channel hypothesis would have to account for rather than replacing with an invented path.

---

## 7. AT-cut geometry makes the microscopic structure oblique to thickness

Under the IEEE convention, AT-cut quartz is `(YXl) -35.25 degrees`: the plate begins with its thickness direction along crystal `Y` and is rotated by `35.25 degrees` about the length / crystal-X axis.

Reference:

`https://doc.comsol.com/6.4/doc/com.comsol.help.sme/sme_ug_modeling.05.108.html`

Therefore the crystallographic `c` / `Z` axis is not normal to the plate. Its angle to the plate normal is approximately

```text
54.75 degrees.
```

If one considers, only as a geometric thought experiment, a path strictly parallel to the `c` axis crossing a `335 um` AT-cut plate, then:

```text
path length through the crystal ~ 580 um,
lateral offset between the two faces ~ 474 um.
```

For a `3.35 mm` radius electrode, two equal electrode footprints displaced by `474 um` still overlap by about

```text
91.0% of their area.
```

Thus even if the microscopic c-axis channels were relevant to a deeper substrate response, the geometry would provide **a very large bundle of parallel candidate paths**, not one unique route.

This reinforces the least-resistance guard: repeated equivalent microscopic channels should distribute response broadly unless defects, state dependence, nonlinear opening/closing, or another symmetry-breaking mechanism selects among them.

---

## 8. Two-scale interpretation now allowed

The safest current picture is:

```text
macroscopic electrode boundary
    -> broad field / drive region

microscopic crystal geometry
    -> directional constitutive response

coupled structural mechanics
    -> localization / energy trapping / shear mode if the equations produce it

bounded mode
    -> recurrence frequency.
```

This is compatible with established quartz theory, where electrode geometry, anisotropic elasticity, piezoelectric coupling, and electrode inertia can confine vibration beneath the electrodes even though the applied electrical field is not itself a narrow filament.

Published quartz studies explicitly report energy trapping in which vibration is concentrated in the central/electroded region and decays toward the plate edge; electrode mass and dimensions participate in that confinement.

References:

- `https://digitalcommons.unl.edu/mechengfacpub/223/`
- `https://pubmed.ncbi.nlm.nih.gov/18267672/`

---

## 9. What an ARK channel law would have to add

A neutral generalized form is

```text
J_a = -M(X, geometry, history) grad(Psi_a)
```

with a state variable or state set `X` describing whatever physical structure controls local accessibility / resistance.

A genuine opening-and-closing channel mechanism would require a forward evolution law such as

```text
D_t X = F(X, J_a, deformation, boundaries)
```

and must satisfy all of the following before it can be used predictively:

1. `M` and `F` must be specified from prior ARK constraints or independent material information, not from the target resonance.
2. The homogeneous limit must reduce to a distributed solution rather than arbitrarily generating a filament.
3. Any localization threshold must arise from the equations.
4. The same law must explain why ordinary quartz remains insulating below breakdown while still permitting polarization/piezoelectric deformation.
5. If a temporary path "opens" and restoring structure "closes" it, the energy and momentum ledger must identify where the stored energy goes.
6. Changing electrode geometry or crystal orientation must move/reshape the solved channel before frequency comparison.
7. Above a true conduction/breakdown threshold, the model must distinguish that regime from ordinary resonant piezoelectric operation.

Until such a law is derived, `channel` remains a physical hypothesis / interpretation, not a free fitting variable.

---

## 10. Immediate implication for the quartz benchmark

The next quartz calculation should **not** apply a uniform-field assumption as a hidden physical truth, but neither should it assume a narrow path.

The first admissible full model is the conventional-style coupled anisotropic boundary-value problem:

```text
actual AT-cut tensor orientation
+ actual electrode footprint
+ actual electrode mass/loading
+ free/mounted boundaries
    -> solve phi(x), E(x), u(x), strain(x)
    -> identify active / trapped mode
    -> extract frequency afterward.
```

That solution becomes the calibration surface for any deeper ARK spatial law.

If the conventional coupled solution is broad electrically but localized mechanically, ARK must reproduce that distinction rather than collapsing field flow and mechanical mode shape into one object.

---

## 11. Compact finding

> **The first spatial null test does not produce a narrow channel. With the declared Q5 geometry, a homogeneous linear dielectric solution is broad and nearly uniform beneath most of the electrode, with fringing confined near the electrode edge. Real quartz nevertheless has genuine crystallographic c-axis channels and strong anisotropic electromechanical structure. Because the AT cut places those microscopic channels obliquely through the plate and provides a large bundle of equivalent possible paths, a unique preferred ARK flow channel would require additional state-dependent, heterogeneous, nonlinear, or boundary-driven mechanics. The new non-negotiable rule is therefore: do not prescribe the channel; solve for it.**
