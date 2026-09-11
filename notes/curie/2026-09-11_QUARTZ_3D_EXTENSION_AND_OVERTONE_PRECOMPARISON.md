# 2026-09-11 Research — Quartz 3-D Extension and Overtone Pre-Comparison

**Status:** LAYER-1 STRUCTURAL EXTENSION / PRE-COMPARISON PREDICTION RECORD — NOT ARK ONTOLOGY VALIDATION  
**Research date:** 2026-09-11  
**Purpose:** Continue the frozen quartz benchmark without modifying Layer 0. Extend the same behavior-first mechanics to a finite 3-D identity, derive how lateral confinement can perturb thickness harmonics, record zero-adjustment overtone predictions before extracting exact measured overtone values, and compare the structure only afterward against published real-resonator behavior.

Companion records:

- `2026-09-11_QUARTZ_BENCHMARK_METHOD_THEORY_RESULT_FREEZE.md`
- `2026-09-11_QUARTZ_THICKNESS_SHEAR_FIRST_PASS_BENCHMARK.md`
- `2026-09-11_TAU_OMEGA_AS_EXPRESSIONS_OF_BEHAVIOR.md`
- `2026-09-11_INTRINSIC_BEHAVIOR_IDENTITY_BOUNDARIES_AND_EMERGENT_PROPERTIES.md`

---

## 1. Frozen starting point

Layer 0 remains unchanged:

```text
rho partial_tt u = G_eff partial_zz u
```

with

```text
f_n^(1D) = n/(2h) sqrt(G_eff/rho)
```

for allowed odd thickness-shear overtones under the electroded AT-cut excitation symmetry.

The first-pass common material pair remains

```text
rho   = 2648 kg/m^3
G_eff = 2.947e10 Pa
```

and no later correction is allowed to rewrite that historical result.

---

## 2. Why 3-D is now required

The resonator identity is not a one-dimensional slab. It is a finite disk with:

- finite blank diameter,
- finite electrode diameter,
- a cut/orientation-dependent anisotropic lattice,
- spatially nonuniform electric coupling,
- lateral energy trapping,
- mounting/boundary conditions,
- and multiple allowed collective modes.

The first-pass observation that `h*f` is nearly constant shows that thickness dominates the leading mode. It does **not** imply that lateral geometry is physically absent.

The next question is therefore:

> **If the full identity is 3-D, does a generic bounded-mode treatment naturally produce a dominant thickness term plus a smaller lateral correction whose importance falls with overtone number?**

---

## 3. Minimal 3-D extension of the same mechanics

Replace the one-dimensional restoring term by the corresponding scalar 3-D gradient form:

```text
u_rest = 1/2 G |grad u|^2

u_pers = 1/2 rho (partial_t u)^2.
```

Variation gives the neutral 3-D wave scaffold

```text
rho partial_tt u = G laplacian(u).
```

This is conventional continuum mechanics used as an audit scaffold, not yet an ARK-specific field law.

Separate the bounded mode as

```text
u(x,y,z,t) = Phi(x,y) Z_n(z) Q_n(t).
```

Define the lateral eigenvalue by

```text
-laplacian_perp Phi = k_perp^2 Phi
```

and the thickness mode by

```text
-Z_n_double_prime = k_z,n^2 Z_n
```

with

```text
k_z,n = n pi / h.
```

The temporal equation is then

```text
Q_n_double_dot + omega_n^2 Q_n = 0
```

with

```text
omega_n^2
= (G/rho) [ (n pi/h)^2 + k_perp^2 ].
```

Therefore

```text
f_n
= n/(2h) sqrt(G/rho)
  sqrt[1 + (k_perp h/(n pi))^2].
```

This is the key Layer-1 structural result.

---

## 4. Immediate consequence: why thickness dominates but 3-D still matters

The normalized frequency is

```text
f_n/n
= 1/(2h) sqrt(G/rho)
  sqrt[1 + (k_perp h/(n pi))^2].
```

For weak lateral correction,

```text
f_n/n
approximately
1/(2h) sqrt(G/rho)
[1 + 1/2 (k_perp h/(n pi))^2].
```

Thus:

```text
leading term      -> thickness closure
3-D correction    -> lateral confinement / active-region geometry
relative strength -> approximately 1/n^2 for fixed k_perp.
```

This means a real 3-D identity can look almost perfectly one-dimensional in its dominant frequency scaling while still carrying finite lateral structure.

It also predicts a qualitative overtone pattern **before using measured overtone frequencies**:

> **Finite lateral confinement should perturb the fundamental most strongly and should matter progressively less at higher thickness overtones.**

---

## 5. Relation to electrode geometry

The electric field does not need to set the leading natural frequency directly in order for electrode size to matter.

The electrode geometry can help determine:

- the spatial region strongly driven by the field,
- the effective active vibrating region,
- lateral mode confinement,
- electrode mass loading,
- energy trapping,
- and which modes couple strongly enough to be observed.

In Layer-1 notation, those effects can enter through the lateral eigenstructure `Phi(x,y)` and therefore through `k_perp`.

A generic circular active region would have a relation of the form

```text
k_perp ~ alpha / R_active
```

where `alpha` is a boundary/mode eigenvalue determined by the actual lateral boundary problem. No value of `alpha` is frozen here; selecting one merely to improve agreement would be target fitting.

This is the mechanically precise version of the current field-channel intuition:

```text
field geometry
-> selects/couples to allowed structural pathways
-> bounded 3-D identity determines mode geometry
-> recurrence rate is the solved expression of that mode.
```

---

## 6. Sealed Layer-0 overtone predictions before exact overtone extraction

Using the already frozen Q5 Layer-0 forward fundamental

```text
f1_model = 4.97916 MHz
```

the untouched 1-D model predicts the odd thickness harmonics:

| Overtone n | Sealed Layer-0 prediction (MHz) |
|---:|---:|
| 1 | 4.97916 |
| 3 | 14.93748 |
| 5 | 24.89580 |
| 7 | 34.85412 |
| 9 | 44.81244 |
| 11 | 54.77076 |
| 13 | 64.72908 |
| 15 | 74.68740 |

These values are now recorded **before transcribing exact measured Q5 overtone frequencies from the comparison literature**.

The purpose of sealing them is not to expect perfect integer scaling from a real finite resonator. It is to preserve what the Layer-0 model actually predicts so later 3-D/electrical corrections cannot be retroactively hidden inside the original calculation.

---

## 7. Published comparison structure found after the Layer-0 freeze

Cassiède et al., *Sensors and Actuators A: Physical* 159 (2010) 174-183, DOI `10.1016/j.sna.2010.03.028`, explicitly studied AT-cut resonators from roughly 3 to 10 MHz over multiple overtones.

The paper reports that:

- ideal infinite-plate theory gives frequencies proportional to odd overtone number,
- real finite crystals deviate because of boundary conditions, piezoelectric stiffening, energy trapping, and anharmonic resonances,
- these perturbations are significant on the fundamental and smaller on the third and fifth overtones,
- high overtone behavior tends toward the ideal odd-multiple limit,
- and finite active vibrating area is important to the real resonator response.

Reference:

`https://doi.org/10.1016/j.sna.2010.03.028`

This qualitative behavior is exactly the direction predicted by the generic 3-D correction above:

```text
finite lateral contribution / thickness contribution
~ 1/n^2.
```

That agreement is structural, not an independent ARK validation, because both calculations are continuum-mode mechanics.

---

## 8. Published electromechanical correction as a separate comparison surface

The related Cassiède et al. *Journal of Applied Physics* paper, DOI `10.1063/1.3460805`, gives for real finite AT-cut quartz a conventional form containing two corrections to the ideal thickness frequency:

```text
f_r,n
= n f0
  [1 - 8 e26^2 / ((n pi)^2 epsilon22 mu_q)]^(1/2)
  [1 + 4 (chi h_q/(n pi d_a,n))^2]^(1/2).
```

with

```text
mu_q = c66 + e26^2/epsilon22.
```

The first factor is an electromechanical/piezoelectric correction. The second represents finite lateral size through an active vibrating diameter `d_a,n` and an empirical crystal parameter `chi`.

The authors list representative AT-cut values at 20 C:

```text
rho_q     = 2.65e3 kg/m^3
c66       = 2.93e10 Pa
e26       = 9.65e-2 C/m^2
epsilon22 = 3.982e-11 F/m.
```

From those values,

```text
mu_q = 2.95339e10 Pa.
```

The purely electromechanical factor changes the ideal rate by approximately:

| n | Piezoelectric factor | Relative shift |
|---:|---:|---:|
| 1 | 0.996785659 | -0.321434% |
| 3 | 0.999643361 | -0.035664% |
| 5 | 0.999871625 | -0.012838% |
| 7 | 0.999934504 | -0.006550% |
| 9 | 0.999960380 | -0.003962% |
| 11 | 0.999973478 | -0.002652% |
| 13 | 0.999981011 | -0.001899% |
| 15 | 0.999985737 | -0.001426% |

So conventional electromechanical coupling itself has the same important qualitative feature:

```text
largest correction at fundamental
-> rapidly diminishing correction at higher n.
```

This supports the earlier discussion that the electric geometry/coupling can alter the precise recurrence without being the main source of the thickness scaling.

---

## 9. Structural correspondence of the 3-D term

The generic Layer-1 finite-identity factor derived here is

```text
sqrt[1 + (k_perp h/(n pi))^2].
```

The published finite-size factor is

```text
sqrt[1 + 4 (chi h/(n pi d_a,n))^2].
```

These have the same mathematical structure if one identifies, only at the level of comparison,

```text
k_perp <-> 2 chi / d_a,n.
```

This is useful because it shows that the empirical active-diameter correction used for real quartz has the form expected from adding a lateral eigenvalue to a thickness eigenvalue in a finite 3-D bounded system.

It does **not** prove the ARK interpretation, and it does not derive `chi` or the active diameter from first principles.

The next mechanical task is therefore clear:

> **Determine the lateral mode/active region from the declared 3-D identity and field coupling rather than fitting an empirical finite-size parameter.**

---

## 10. Important reinterpretation of the excellent Layer-0 match

The first-pass use of one effective modulus `G_eff = 29.47 GPa` reproduced the five fundamentals extremely well.

The 3-D/electromechanical comparison now shows why that numerical success must be interpreted cautiously.

A real fundamental resonance contains multiple effects with partially competing signs:

```text
thickness shear scale
+/- electromechanical correction
+ finite lateral confinement
+ energy trapping
+ electrode loading
+ anisotropy/boundary details.
```

A single imported `G_eff` can absorb some of those effects into one effective coefficient.

Therefore the Layer-0 result remains a clean demonstration of **rate emergence from bounded mechanics**, but its `0.063%` mean residual must not be interpreted as evidence that the reduced one-dimensional physical model is complete.

This strengthens rather than weakens the modeling discipline: the next layers should unpack the effective coefficient instead of celebrating the residual.

---

## 11. Current physical picture after continuation

The working interpretation is now:

```text
3-D material identity
+ anisotropic constitutive behavior
+ electrical field/coupling geometry
+ physical boundaries
    -> allowed spatial response channels / mode shapes

mode shape + restoring/persistence behavior
    -> recurrence

recurrence
    -> observed omega / frequency.
```

For the dominant AT-cut mode:

```text
thickness determines the leading closure scale;
lateral/electrode geometry perturbs and confines the mode;
electromechanical coupling modifies the restoring response;
higher overtones increasingly suppress the relative importance of fixed lateral corrections.
```

This is consistent with the present behavior-first principle and with the measured qualitative behavior of real quartz resonators.

---

## 12. Next discriminating move

The strongest next step is **not** to fit `chi` or an effective active diameter to the known resonances.

Instead:

1. obtain exact measured overtone frequencies for one of the already-declared resonators,
2. keep the sealed Layer-0 overtone predictions above untouched,
3. quantify the overtone residual pattern,
4. test whether the residual falls approximately with the `1/n^2` structure predicted by finite 3-D/electromechanical corrections,
5. then attempt a non-target-fitted lateral boundary model using physical blank/electrode geometry,
6. and only afterward address Q/ringdown as the persistence-side observable.

If the residual pattern has the wrong sign, wrong overtone dependence, or requires an arbitrary per-overtone parameter, that should count against the current simplified channel picture rather than being tuned away.
