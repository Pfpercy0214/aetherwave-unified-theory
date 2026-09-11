# 2026-09-11 Research — Quartz Thickness-Shear First-Pass Benchmark

**Status:** CLEAN STRUCTURAL / CONCEPT BENCHMARK — NOT AN INDEPENDENT VALIDATION OF ARK ONTOLOGY  
**Research date:** 2026-09-11  
**Purpose:** Test the current behavior-first interpretation on a bounded piezoelectric identity without inserting a recurrence rate as an input. The benchmark asks whether a restoring-response law plus persistence/inertia and physical boundaries can produce the observed AT-cut quartz thickness-shear frequency scale and inverse-thickness behavior.

Companion records:

- `2026-09-11_TAU_OMEGA_AS_EXPRESSIONS_OF_BEHAVIOR.md`
- `2026-09-11_INTRINSIC_BEHAVIOR_IDENTITY_BOUNDARIES_AND_EMERGENT_PROPERTIES.md`
- `2026-09-10_ARK_RECURRENCE_TIME_FREQUENCY_IDENTITY_CLOSURE_AUDIT.md`
- `2026-09-10_ARK_MECHANICAL_CORE_MAXWELL_FARADAY_AND_RATE_EMERGENCE.md`

---

## 1. Benchmark question

The narrow question is:

> **Can the observed recurrence scale of a bounded AT-cut quartz resonator emerge from material response and geometry, without assigning a frequency to the identity beforehand?**

This is intentionally weaker than claiming that ARK independently predicts quartz from its deepest scalars.

The present test uses conventional measured material response coefficients as inputs. Therefore it is a test of the **behavior-first / rate-emergence architecture**, not yet a test that ARK derives those coefficients from substrate mechanics.

---

## 2. Experimental comparison set

Cassiède et al., *Journal of Applied Physics* **108**, 034505 (2010), DOI `10.1063/1.3460805`, report five polished AT-cut quartz resonators with the following characteristics:

| Crystal | Nominal fundamental frequency (MHz) | Quartz thickness (um) | Electrode diameter (mm) |
|---|---:|---:|---:|
| Q3 | 2.975 | 561 | 6.7 |
| Q5 | 4.983 | 335 | 6.7 |
| Q6 | 5.997 | 278 | 6.7 |
| Q8 | 7.988 | 209 | 5.1 |
| Q10 | 9.984 | 167 | 5.1 |

The same study describes 13.6 mm diameter blanks and equal electrodes on both faces. A related Cassiède et al. study reports the electrodes as approximately 10 nm Ti plus 100 nm Au.

Reference locations used during this audit:

- `https://doi.org/10.1063/1.3460805`
- `https://www.researchgate.net/publication/234883462_Impedance_analysis_for_characterizing_the_influence_of_hydrostatic_pressure_on_piezoelectric_quartz_crystal_sensors`

The observed products `thickness * frequency` are:

```text
Q3   1668.975 kHz mm
Q5   1669.305 kHz mm
Q6   1667.166 kHz mm
Q8   1669.492 kHz mm
Q10  1667.328 kHz mm
```

Mean:

```text
1668.453 kHz mm
```

Sample standard deviation across the five devices:

```text
1.118 kHz mm = 0.0670%
```

This already shows that the dominant mode is extraordinarily close to inverse-thickness scaling over the 3–10 MHz range.

The 6.7 mm electrode group has mean `t f = 1668.482 kHz mm`; the 5.1 mm group has mean `1668.410 kHz mm`, a difference of only about `0.0043%` in this rounded table. Electrode diameter therefore does not appear to set the leading recurrence scale in this dataset, though it can still affect excitation, energy trapping, mass loading, lateral mode structure, and Q.

---

## 3. Material inputs kept separate from target frequency

For the first reduced-mode calculation use standard AT-cut quartz material values:

```text
rho = 2648 kg/m^3
G_eff = 2.947e10 Pa
```

A representative independent source reporting these standard QCM values is:

- `https://pmc.ncbi.nlm.nih.gov/articles/PMC8070455/`

Other quartz literature reports closely related AT-cut values, including rotated stiffness `c66 ~ 2.901e10 Pa`, piezoelectric coefficient `e26 ~ 0.095 C/m^2`, dielectric permittivity near `3.98e-11 F/m`, and piezoelectrically stiffened/effective shear constants around `2.95e10 Pa`.

Important epistemic qualification: an effective quartz shear modulus may itself have an acoustic/resonance measurement history. Therefore using `G_eff` is legitimate as a **known constitutive input**, but it cannot be cited as proof that ARK independently derived the material response.

---

## 4. Reduced bounded-identity mechanics

Treat the full resonator as a 3-D identity, but isolate the dominant thickness-shear coordinate for the first benchmark.

Let `u(z,t)` be the dominant shear displacement through crystal thickness `h`.

Use the generic energy densities

```text
u_pers = 1/2 rho (partial_t u)^2

u_rest = 1/2 G_eff (partial_z u)^2.
```

These are conventional continuum-mechanics expressions and are used here as a neutral audit scaffold for the current ARK interpretation:

```text
rho      -> effective persistence/inertial expression
G_eff    -> effective restoring-response expression
boundary -> physical identity closure
omega    -> solved recurrence output
```

Varying the action gives

```text
rho partial_tt u = G_eff partial_zz u.
```

For free major faces,

```text
partial_z u = 0 at z = +/- h/2.
```

The lowest nontrivial antisymmetric thickness-shear mode may be written

```text
u(z,t) = Q(t) sin(pi z / h).
```

Substitution yields

```text
Q_double_dot + omega_1^2 Q = 0
```

with

```text
omega_1^2 = (G_eff / rho) (pi / h)^2.
```

Only after solving the bounded mechanics do we define measured recurrence frequency:

```text
f_1 = omega_1 / (2 pi)
    = (1 / 2h) sqrt(G_eff / rho).
```

The important causal ordering is therefore

```text
restoring response + persistence/inertia + thickness boundary
    -> allowed mode
    -> recurrence period
    -> measured frequency.
```

No frequency is inserted into the equation of motion.

---

## 5. Forward result using one material input set for all five crystals

With

```text
G_eff = 2.947e10 Pa
rho   = 2648 kg/m^3
```

the implied shear propagation scale is

```text
sqrt(G_eff / rho) = 3336.039 m/s
```

and the thickness-frequency constant produced by the solved mode is

```text
N_model = 1/2 sqrt(G_eff / rho)
        = 1668.019 kHz mm.
```

No per-device parameter is changed.

| Crystal | Thickness (um) | Observed (MHz) | Model (MHz) | Fractional residual |
|---|---:|---:|---:|---:|
| Q3 | 561 | 2.975 | 2.97330 | -0.0573% |
| Q5 | 335 | 4.983 | 4.97916 | -0.0770% |
| Q6 | 278 | 5.997 | 6.00007 | +0.0512% |
| Q8 | 209 | 7.988 | 7.98095 | -0.0882% |
| Q10 | 167 | 9.984 | 9.98814 | +0.0415% |

Mean absolute fractional residual:

```text
0.0630%
```

Largest absolute residual:

```text
0.0882%
```

The model thickness-frequency constant differs from the five-device observed mean by

```text
-0.0260%
```

or about

```text
0.388 times the observed sample standard deviation of the five t*f values.
```

This `0.388` is a **scatter ratio**, not a formal Gaussian sigma statistic.

---

## 6. Conditional rounding / uncertainty check

The published thicknesses are displayed to the nearest micrometre. If — and only if — those tabulated values are rounded at roughly `+/-0.5 um`, then the implied first-order relative frequency envelope from thickness quantization alone is approximately

```text
(delta f / f)_h ~ 0.5 um / h.
```

That gives approximate envelopes from `0.089%` for Q3 to `0.299%` for Q10.

The absolute model residual divided by that conditional thickness-rounding envelope is:

```text
Q3   0.64
Q5   0.52
Q6   0.28
Q8   0.37
Q10  0.14
```

Thus every residual is smaller than the uncertainty that would arise from half-micrometre thickness rounding alone.

This is **not** a formal uncertainty budget because the source does not state that `+/-0.5 um` is the physical thickness uncertainty. It is only a useful bound showing why the present data cannot support a claim of sub-0.1% physical predictive precision.

A proper uncertainty budget should eventually include:

- actual thickness metrology uncertainty,
- temperature,
- cut-angle tolerance,
- elastic/piezoelectric constant uncertainty,
- electrode mass and geometry,
- finite lateral dimensions,
- mounting/loading,
- mode trapping,
- and environmental loading.

---

## 7. Bare-stiffness control

As a control, using the rotated mechanical stiffness value

```text
c66 = 2.901e10 Pa
rho = 2645 kg/m^3
```

instead of the accepted effective AT-cut shear modulus gives

```text
N_bare = 1655.888 kHz mm
```

and all five predicted frequencies fall low by roughly `0.68%` to `0.81%`.

This nearly common-mode offset is informative. It says that the inverse-thickness geometry is already correct at the reduced mechanical level, while the absolute rate depends on the **effective coupled restoring response** used for the identity.

The five-device mean, if inverted only as an audit diagnostic with `rho = 2648 kg/m^3`, corresponds to an effective modulus of approximately

```text
29.485 GPa,
```

which is close to the independently tabulated AT-cut effective shear modulus near `29.47 GPa`.

This inversion is diagnostic only and must not be fed back into the forward benchmark as a fitted parameter.

---

## 8. What this result does and does not show

### Supported as a concept result

The benchmark cleanly demonstrates that a bounded-mode architecture can reproduce the observed recurrence scale without assigning frequency as a primitive input:

```text
material response
+ inertial/persistence response
+ identity boundary
-> mode
-> frequency.
```

Across five crystals with one material-response pair, the reduced solution reproduces both the inverse-thickness scaling and the reported absolute frequency scale to better than `0.1%` using the standard effective AT-cut shear modulus.

This is directly consistent with the current principle:

> **Frequency is an expression of solved behavior of a bounded identity.**

### Not established

This is not yet evidence that the ARK substrate ontology is correct because:

1. the energy law used here is standard continuum elasticity,
2. the effective material modulus and density are conventional measured inputs,
3. the target frequencies were known before this calculation was formalized, so the test is retrospective rather than blind,
4. the effective modulus may itself have historical acoustic/resonance provenance,
5. electrical/piezoelectric coupling has not yet been derived from ARK scalars,
6. the full 3-D electroded identity has been reduced to its dominant thickness coordinate.

Therefore the correct label is:

> **Strong concept-level reproduction of rate emergence from structure; not independent ARK validation.**

---

## 9. Relevance to the field-flow / channel hypothesis

The result suggests a useful separation.

The electrical geometry does not appear to set the leading frequency directly in this dataset: switching electrode diameter from 6.7 mm to 5.1 mm leaves the `t*f` constant essentially unchanged at the table precision.

A reasonable working interpretation is therefore:

```text
electromagnetic / substrate coupling
    -> selects and drives allowed structural response

material restoring behavior + 3-D identity
    -> determines allowed deformation channels

thickness-shear closure
    -> dominates the fundamental recurrence length

recurrence of that bounded channel
    -> measured frequency.
```

The electric field can remain essential to **coupling and excitation** even when the natural recurrence rate is primarily set by the mechanical closure path.

The bare-stiffness control also warns that the absolute rate cannot be derived accurately by ignoring the effective coupled constitutive response.

---

## 10. Next discriminating step

The next test should be frozen before comparison and should not merely repeat the same frequency-thickness identity.

Preferred directions:

1. **Held-out quartz geometry:** predict resonances for a separate AT-cut dataset with different dimensions/electrode geometry using the same material law.
2. **Overtone structure:** predict `n = 3, 5, ...` mode locations and examine departures from exact integer scaling due to finite geometry/energy trapping.
3. **Electrode loading:** derive the sign and approximate magnitude of the frequency shift caused by known Ti/Au electrode mass without fitting to the measured frequency.
4. **Drive versus natural mode:** include the piezoelectric field explicitly and verify that drive amplitude selects/excites the mode without becoming the source of its natural frequency in the linear regime.
5. **Persistence / Q:** add a declared loss channel and predict ringdown or Q independently of the resonance frequency.

A stronger ARK-specific benchmark will require deriving the effective restoring/persistence coefficients from the surviving scalar mechanics rather than importing `G_eff` and `rho` as terminal constitutive inputs.

---

## 11. Compact finding

> **First pass: one bounded-mode law plus one standard AT-cut material-response pair reproduces five 3–10 MHz quartz resonators with a mean absolute frequency residual of about 0.063% and a maximum of about 0.088%, while frequency remains a solved output rather than an assigned input. This is a strong test of the behavior-first/rate-emergence concept, but it is not yet an independent test of ARK ontology because the constitutive material response is imported from conventional quartz measurements.**
