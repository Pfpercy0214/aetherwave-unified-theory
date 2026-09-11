# 2026-09-11 Research — Quartz Benchmark Method, Applied Theory, and Result Freeze

**Status:** FROZEN BENCHMARK RECORD / PROVENANCE CHECKPOINT — NOT AN INDEPENDENT VALIDATION OF ARK ONTOLOGY  
**Research date:** 2026-09-11  
**Purpose:** Freeze the exact method, applied theory, inputs, exclusions, comparison protocol, and first-pass result before extending the quartz study into 3-D, overtone, electrode, or persistence/Q modeling.

Companion records:

- `2026-09-11_QUARTZ_THICKNESS_SHEAR_FIRST_PASS_BENCHMARK.md`
- `2026-09-11_TAU_OMEGA_AS_EXPRESSIONS_OF_BEHAVIOR.md`
- `2026-09-11_INTRINSIC_BEHAVIOR_IDENTITY_BOUNDARIES_AND_EMERGENT_PROPERTIES.md`
- `2026-09-10_ARK_RECURRENCE_TIME_FREQUENCY_IDENTITY_CLOSURE_AUDIT.md`

---

## 1. Frozen benchmark claim

The first quartz calculation tested only the following proposition:

> **A recurrence rate can emerge as a solved property of a bounded identity from restoring response, persistence/inertia, and physical boundaries, rather than being inserted as a primitive frequency instruction.**

It did **not** test whether ARK independently derives quartz elasticity, piezoelectric coefficients, density, or the substrate ontology.

The result is therefore classified as:

> **Strong concept-level reproduction of rate emergence from structure; not independent ARK validation.**

---

## 2. Identity and reduction used

The physical identity is the full AT-cut quartz resonator, including its finite 3-D body and electrodes.

The first pass deliberately reduced that 3-D identity to the dominant thickness-shear coordinate:

```text
u = u(z,t)
```

where `z` is the thickness direction and `h` is the quartz thickness.

This reduction was used because the benchmark dataset itself shows a nearly constant `h*f` product over five resonators from about 3 MHz to 10 MHz.

The reduction does **not** assert that the real identity is one-dimensional. It asserts only that the leading observed mode can be approximated by one dominant coordinate for the first structural test.

---

## 3. Applied theory frozen for the first pass

The neutral continuum audit scaffold was:

```text
u_pers = 1/2 rho (partial_t u)^2

u_rest = 1/2 G_eff (partial_z u)^2.
```

Here:

```text
rho   = measured material density / inertial expression
G_eff = measured effective AT-cut shear restoring response
h     = physical identity boundary in the thickness direction
omega = output, not input.
```

Varying the corresponding action gives

```text
rho partial_tt u = G_eff partial_zz u.
```

For free major faces:

```text
partial_z u = 0 at z = +/- h/2.
```

The lowest nontrivial antisymmetric thickness-shear mode was written

```text
u(z,t) = Q(t) sin(pi z / h).
```

which gives

```text
Q_double_dot + omega_1^2 Q = 0
```

with

```text
omega_1^2 = (G_eff/rho) (pi/h)^2.
```

Only after the bounded mode is solved is ordinary frequency defined:

```text
f_1 = omega_1/(2 pi)
    = (1/(2h)) sqrt(G_eff/rho).
```

This is the complete first-pass applied theory. No additional ARK scalar equation was inserted into this calculation.

---

## 4. Frozen inputs

One common material-response pair was used for all five resonators:

```text
rho   = 2648 kg/m^3
G_eff = 2.947e10 Pa.
```

These were treated as independently known conventional constitutive inputs.

The benchmark geometries were taken from Cassiède et al., *Journal of Applied Physics* 108, 034505 (2010), DOI `10.1063/1.3460805`:

| Crystal | Thickness (um) | Electrode diameter (mm) | Reported fundamental (MHz) |
|---|---:|---:|---:|
| Q3 | 561 | 6.7 | 2.975 |
| Q5 | 335 | 6.7 | 4.983 |
| Q6 | 278 | 6.7 | 5.997 |
| Q8 | 209 | 5.1 | 7.988 |
| Q10 | 167 | 5.1 | 9.984 |

The electrode diameters were recorded as part of the physical identity but were **not** used to tune the first-pass frequency law.

---

## 5. Explicit non-inputs / anti-leakage guard

The following quantities were not used to determine the model frequency:

- the reported resonance frequency of any individual crystal,
- a fitted per-crystal stiffness,
- a fitted per-crystal density,
- a fitted `omega`,
- a fitted persistence time,
- electrode-diameter corrections,
- active vibrating diameter,
- finite-size fitting parameters,
- measured overtone locations,
- target-dependent correction factors.

The reported resonances were used only after the forward values were generated for comparison.

The effective modulus itself remains an imported constitutive quantity and may contain prior acoustic/piezoelectric measurement history. This prevents the result from being classified as a fully independent first-principles prediction.

---

## 6. Frozen first-pass result

The common material pair gives

```text
sqrt(G_eff/rho) = 3336.039 m/s
```

and therefore

```text
h*f = 1668.019 kHz mm.
```

Forward predictions:

| Crystal | Observed (MHz) | Forward model (MHz) | Fractional residual |
|---|---:|---:|---:|
| Q3 | 2.975 | 2.97330 | -0.0573% |
| Q5 | 4.983 | 4.97916 | -0.0770% |
| Q6 | 5.997 | 6.00007 | +0.0512% |
| Q8 | 7.988 | 7.98095 | -0.0882% |
| Q10 | 9.984 | 9.98814 | +0.0415% |

Summary:

```text
mean absolute fractional residual = 0.0630%
maximum absolute residual         = 0.0882%
model h*f versus sample mean      = -0.0260%
```

The sample mean of the five observed `h*f` products is

```text
1668.453 kHz mm
```

with sample standard deviation

```text
1.118 kHz mm = 0.0670%.
```

The model/sample-mean offset is about `0.388` times that sample standard deviation. This is a scatter ratio, not a formal Gaussian sigma statement.

---

## 7. Uncertainty discipline frozen with the result

The tabulated thicknesses are reported only to whole micrometres. If they are rounded to roughly `+/-0.5 um`, then thickness quantization alone would imply a first-order frequency envelope of roughly

```text
(delta f/f)_h ~ 0.5 um / h.
```

All five first-pass residuals are smaller than that conditional envelope.

This does **not** establish a formal sub-0.1% predictive uncertainty. A proper uncertainty budget must eventually include thickness metrology, cut-angle tolerance, temperature, material-constant uncertainty, electrode loading, finite lateral geometry, mounting, mode trapping, and environmental loading.

Therefore the numerical match must not be advertised as demonstrated sub-0.1% ARK precision.

---

## 8. Interpretation frozen before extension

The allowed interpretation is:

```text
restoring behavior
+ persistence/inertia
+ bounded geometry
-> allowed mode
-> recurrence
-> measured frequency.
```

This supports the current behavior-first principle:

> **Frequency can be an expression of solved behavior of a bounded identity.**

The result does not establish:

- that the ARK substrate exists,
- that `rho` is the final ARK persistence variable,
- that `G_eff` is the final ARK `k^c` mapping,
- that the real quartz identity is one-dimensional,
- or that electrical/piezoelectric coupling is unnecessary.

The first pass is now frozen. Later refinements must be recorded as additional model layers rather than silently changing this benchmark after seeing residuals.

---

## 9. Extension rule

All subsequent quartz work must preserve this first-pass result unchanged and add clearly labeled layers such as:

```text
Layer 0: 1-D thickness-shear structural benchmark  [frozen here]
Layer 1: finite 3-D identity / lateral confinement
Layer 2: explicit piezoelectric/electrical coupling
Layer 3: electrode mass/loading and active-region geometry
Layer 4: dissipation / persistence / Q
Layer 5: ARK-specific derivation of effective constitutive behavior.
```

A later model may outperform or supersede Layer 0 physically, but it must not erase the provenance of the original test.
