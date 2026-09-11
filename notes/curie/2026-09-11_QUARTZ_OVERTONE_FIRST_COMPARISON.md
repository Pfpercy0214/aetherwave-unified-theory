# 2026-09-11 Research — Quartz Overtone First Comparison

**Status:** POST-FREEZE COMPARISON / INFORMATIVE STRESS TEST — NOT ARK ONTOLOGY VALIDATION  
**Research date:** 2026-09-11  
**Purpose:** Compare the already-frozen thickness-mode and 3-D overtone predictions against public overtone evidence without altering the pre-comparison model. Preserve both supportive and negative results.

Companion records:

- `2026-09-11_QUARTZ_BENCHMARK_METHOD_THEORY_RESULT_FREEZE.md`
- `2026-09-11_QUARTZ_THICKNESS_SHEAR_FIRST_PASS_BENCHMARK.md`
- `2026-09-11_QUARTZ_3D_EXTENSION_AND_OVERTONE_PRECOMPARISON.md`
- `2026-09-11_TAU_OMEGA_AS_EXPRESSIONS_OF_BEHAVIOR.md`

---

## 1. Frozen predictions being tested

Layer 0 was frozen before this comparison as

```text
rho partial_tt u = G_eff partial_zz u
```

with odd thickness-shear frequencies

```text
f_n^(1D) = n/(2h) sqrt(G_eff/rho).
```

The Layer-1 finite-identity extension was also recorded before extracting comparison values:

```text
omega_n^2
= (G/rho) [ (n pi/h)^2 + k_perp^2 ]
```

or

```text
f_n/n
= 1/(2h) sqrt(G/rho)
  sqrt[1 + (k_perp h/(n pi))^2].
```

Therefore, for fixed lateral structure, the Layer-1 prediction made before comparison is:

```text
finite-lateral correction is positive;
its relative importance is largest at n = 1;
and its weak-correction magnitude falls approximately as 1/n^2.
```

The already sealed Q5 Layer-0 predictions remain untouched:

| n | Sealed prediction (MHz) |
|---:|---:|
| 1 | 4.97916 |
| 3 | 14.93748 |
| 5 | 24.89580 |
| 7 | 34.85412 |
| 9 | 44.81244 |
| 11 | 54.77076 |
| 13 | 64.72908 |
| 15 | 74.68740 |

---

## 2. Source limitation for the originally selected Q5 overtone test

The intended first comparison was the exact overtone spectrum of the Cassiède et al. Q5 resonator used in the five-device fundamental benchmark.

The publicly accessible abstract and related full-text material confirm the relevant qualitative behavior, but the exact individual Q5 vacuum overtone peak frequencies are not exposed in the accessible text. The article itself is not available as public full text through the sources checked in this session.

Therefore:

> **Do not manufacture or digitize approximate Q5 overtone values and present them as exact measurements.**

The sealed Q5 predictions remain available for a later exact comparison if a reliable table/full-text source becomes available.

Primary source:

`M. Cassiède et al., Electrical behaviour of AT-cut quartz crystal resonators as a function of overtone number, Sensors and Actuators A 159 (2010) 174-183, DOI 10.1016/j.sna.2010.03.028.`

The public abstract states that finite surface/energy trapping, piezoelectric stiffening, and boundary conditions perturb real resonators, with the effects significant on the fundamental and smaller on the third and fifth overtones.

---

## 3. Exact conventional structural comparison that is available

A related Cassiède et al. full-text article gives the real-resonator correction explicitly:

```text
f_r,n = n f0
        [1 - 8 e26^2 / ((n pi)^2 epsilon22 mu_q)]^(1/2)
        [1 + 4 (chi h/(n pi d_a,n))^2]^(1/2)
```

with

```text
mu_q = c66 + e26^2/epsilon22.
```

The first factor is electromechanical/piezoelectric; the second is finite lateral size through the active vibrating diameter.

Using the paper's declared AT-cut values

```text
c66       = 2.93e10 Pa
e26       = 9.65e-2 C/m^2
epsilon22 = 3.982e-11 F/m
```

gives

```text
mu_q = 2.953385861e10 Pa.
```

The electromechanical factor alone produces relative shifts of approximately:

| n | Relative electromechanical shift |
|---:|---:|
| 1 | -0.321434% |
| 3 | -0.035664% |
| 5 | -0.012838% |
| 7 | -0.006550% |
| 9 | -0.003962% |
| 11 | -0.002652% |
| 13 | -0.001899% |
| 15 | -0.001426% |

This is an explicit independent confirmation that a real quartz identity contains overtone-dependent corrections concentrated at low overtone order and decreasing approximately as `1/n^2`.

The published finite-size factor has the same structural form as the pre-comparison Layer-1 lateral eigenvalue term:

```text
Layer 1:    sqrt[1 + (k_perp h/(n pi))^2]
Published:  sqrt[1 + 4 (chi h/(n pi d_a,n))^2].
```

At the level of mathematical comparison only,

```text
k_perp <-> 2 chi/d_a,n.
```

This correspondence does not derive `chi`, `d_a,n`, or ARK substrate mechanics.

Source:

`M. Cassiède et al., Impedance analysis for characterizing the influence of hydrostatic pressure on piezoelectric quartz crystal sensors, Journal of Applied Physics 108, 034505 (2010), DOI 10.1063/1.3460805.`

---

## 4. Held-out exact dual-harmonic stress test

Because exact Q5 overtone peaks were unavailable, a separate public experiment was used as a held-out stress test rather than altering the original dataset.

Baù, Ferrari, and Ferrari report a fabricated AT-cut quartz resonator made from a **330 micrometre-thick bare crystal** with aerosol-jet-printed electrodes and an on-crystal conductive coil. The published reference frequencies are:

```text
fundamental:      4.77 MHz
third harmonic:  14.22 MHz
```

Source:

`M. Baù, M. Ferrari, V. Ferrari, Quartz Crystal Resonator Sensor With Printed-on-Crystal Coil for Dual-Harmonic Electromagnetic Contactless Interrogation, IEEE TUFFC 67(4), 883-886 (2020), DOI 10.1109/TUFFC.2019.2956814.`

This device is intentionally **not equivalent** to the lightly electroded Cassiède resonators: the printed electrodes and integrated conductive coil are part of the physical identity and can create substantial loading/coupling changes.

---

## 5. Zero-adjustment Layer-0 transfer to the 330 micrometre device

Using the already frozen first-pass material pair

```text
G_eff = 2.947e10 Pa
rho   = 2648 kg/m^3
```

and only the independently reported thickness

```text
h = 330 um,
```

Layer 0 predicts

```text
f1 = 5.054604 MHz
f3 = 15.163812 MHz.
```

Compared with the reported device values:

| Mode | Layer-0 prediction | Reported | Fractional residual |
|---|---:|---:|---:|
| fundamental | 5.054604 MHz | 4.77 MHz | +5.97% |
| third | 15.163812 MHz | 14.22 MHz | +6.64% |

This is a clear **absolute-transfer failure** of the one-dimensional lightly-electroded effective model on this differently loaded resonator.

That failure is scientifically useful. It demonstrates that thickness plus one imported effective quartz modulus is not sufficient to predict an arbitrary electroded/printed 3-D quartz identity. The electrodes, coil, active region, loading, and/or other device-specific boundary conditions matter at percent scale here.

This result must not be hidden by refitting `G_eff` to the new device.

---

## 6. Overtone-ratio result independent of the absolute scale

The exact-integer Layer-0 prediction requires

```text
f3/(3 f1) = 1.
```

The reported device gives

```text
f3/(3 f1)
= 14.22/(3*4.77)
= 0.9937107.
```

Thus

```text
(f3/(3 f1) - 1) = -0.62893%.
```

Equivalently,

```text
f1       = 4.770 MHz
f3 / 3   = 4.740 MHz.
```

So the fundamental's normalized frequency is higher than the third harmonic's normalized frequency by about `0.63%`.

This falsifies exact integer scaling for this real loaded identity at the sub-percent level.

More importantly for the pre-comparison Layer-1 prediction, the **sign is correct for a positive finite-lateral correction that is strongest at n = 1**:

```text
positive correction ~ 1/n^2
-> normalized fundamental shifted upward more than normalized n=3
-> f3/(3 f1) < 1.
```

This is a structural sign check only. The Layer-1 model did not predict the magnitude because `k_perp` was deliberately left unfit.

---

## 7. Diagnostic inversion only — not a fitted validation

If the observed fundamental/third ratio is attributed *entirely* to the simple Layer-1 lateral term,

```text
f_n/n = F_inf sqrt[1 + x/n^2]
```

with

```text
x = (k_perp h/pi)^2,
```

then the observed ratio implies approximately

```text
x = 0.01431
k_perp h/pi = 0.11962
k_perp h = 0.37579.
```

For `h = 330 um`, this corresponds to

```text
k_perp ~ 1.14e3 m^-1.
```

This inversion is **diagnostic only**. It cannot be cited as a prediction or as evidence for ARK because it was obtained from the observed harmonic ratio and ignores competing electromechanical and mass-loading effects.

Its value is to establish an order of magnitude that a future independently solved lateral boundary problem would have to reproduce or explain.

---

## 8. Important sign competition

The conventional piezoelectric factor from the Cassiède equation is negative at low overtone order:

```text
n=1: about -0.321%
n=3: about -0.0357%.
```

By itself that effect would make the normalized fundamental lower than the normalized third overtone.

The finite-size factor is positive and larger for the fundamental, which acts in the opposite direction.

The Baù device has

```text
f1 > f3/3,
```

so its **net** low-order correction has the sign associated with the positive finite-geometry/loading contribution dominating the relative n=1-to-n=3 comparison.

However, because the device includes printed electrodes and an integrated conductive coil, this observation cannot isolate finite lateral confinement from electrode mass loading, electrical boundary effects, anisotropy, or other structural contributions.

---

## 9. What survived and what failed

### Survived

The pre-comparison structural proposition survived its first overtone sign test:

```text
3-D identity
-> low-order mode corrections
-> strongest relative effect at fundamental
-> decreasing importance toward higher overtone order.
```

The independently published real-resonator equation also contains the same `1/n^2` finite-size structure predicted by adding a lateral eigenvalue to the thickness eigenvalue.

### Failed / incomplete

The frozen one-dimensional absolute-frequency model does **not** transfer to an arbitrarily loaded quartz identity. On the 330 um printed-coil resonator it misses both reported harmonics high by about 6%.

Therefore:

> **The excellent five-crystal Layer-0 fundamental result cannot be generalized as a universal quartz-frequency law. The total identity and its electromechanical/loading geometry must be represented.**

This is exactly the kind of negative result the benchmark was intended to expose.

---

## 10. Next non-tuned prediction

The immediate next task should not be to fit the Baù device.

Instead, derive the lateral/electrical/loading state from independently declared geometry where enough information is public. The cleanest possible next target is a resonator for which the following are all available without using its resonance frequency as an input:

```text
quartz thickness and diameter,
electrode diameter/thickness/material,
cut/orientation,
mounting or free-boundary description,
and at least two measured overtone frequencies.
```

Then:

```text
physical geometry
-> solve active/lateral eigenstructure
-> solve thickness + lateral mode
-> predict f1, f3, f5...
-> compare afterward.
```

Until such a source is available, the exact Q5 predictions remain sealed rather than being compared against approximate values digitized from figures.

---

## 11. Compact finding

> **First overtone comparison: exact Q5 peak values were not publicly recoverable in the checked sources, so they were not invented or digitized. Independent literature nevertheless confirms the predicted low-overtone `1/n^2` correction structure. A separate 330 um AT-cut dual-harmonic resonator provides a useful held-out stress test: the frozen one-dimensional model fails absolute transfer by about 6%, while the observed normalized fundamental-to-third relationship has the sign predicted by a positive low-order finite-geometry correction. The result strengthens the need to treat the whole electroded 3-D identity as the physical system, while leaving the ARK-specific substrate interpretation unvalidated.**
