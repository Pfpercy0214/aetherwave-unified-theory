# 2026-09-11 Research — Printed Quartz Device Geometry Follow-Up

**Status:** SOURCE-GEOMETRY FOLLOW-UP / MODEL-CONSTRAINT NOTE — NOT ARK VALIDATION  
**Research date:** 2026-09-11  
**Purpose:** Preserve additional physical geometry recovered after the first overtone comparison, because it materially changes how the held-out printed-coil resonator should be interpreted and strengthens the requirement to model the complete electroded 3-D identity.

Companion records:

- `2026-09-11_QUARTZ_OVERTONE_FIRST_COMPARISON.md`
- `2026-09-11_QUARTZ_3D_EXTENSION_AND_OVERTONE_PRECOMPARISON.md`
- `2026-09-11_QUARTZ_BENCHMARK_METHOD_THEORY_RESULT_FREEZE.md`

---

## 1. Related printed-coil prototype geometry

A related chapter by Ferrari, Demori, Baù, and Ferrari, *Distance-Independent Contactless Interrogation of Quartz Resonator Sensor with Printed-on-Crystal Coil* (DOI `10.1007/978-3-030-37558-4_44`), describes a printed-on-quartz prototype with the following physical geometry:

```text
AT-cut quartz blank diameter:       25.4 mm
AT-cut quartz blank thickness:      330 um
printed top electrode diameter:      5.5 mm
printed bottom electrode diameter:   5.5 mm
printed conductive path thickness:  about 15 um
conductive ink: Novacentrix Metalon HPS-108AE1
```

The top side contains the 5.5-mm electrode plus a planar printed coil. The bottom side contains the matching 5.5-mm electrode. The printed path is cured after deposition.

The same chapter reports a contactless measured resonance of approximately

```text
4.790260 MHz.
```

Source location checked during this audit:

`Ferrari et al., Sensors and Microsystems, Lecture Notes in Electrical Engineering 629 (2020), chapter DOI 10.1007/978-3-030-37558-4_44.`

---

## 2. Sample-identity caution

The dual-harmonic IEEE paper used in the first overtone comparison reports a 330-um AT-cut device with printed electrodes/coil and reference frequencies

```text
f1 = 4.77 MHz
f3 = 14.22 MHz.
```

The related chapter gives the detailed 25.4-mm / 5.5-mm / 15-um geometry and a resonance of `4.790260 MHz`.

These are clearly closely related prototypes from the same research program, but the presently accessible sources do **not** establish that the chapter device and the exact dual-harmonic IEEE device are the same physical sample.

Therefore:

> **Do not combine the chapter geometry with the IEEE third-harmonic value as though exact sample identity had been proven.**

The geometry is useful as a scale and design constraint for this device family, not as a fully verified parameter set for the exact 4.77/14.22 MHz sample.

---

## 3. Why the geometry matters

The earlier Cassiède comparison resonators use thin evaporated electrodes:

```text
10 nm Ti + 100 nm Au
```

for a total nominal metal thickness near

```text
0.11 um.
```

The related printed-coil prototype reports a conductive path thickness near

```text
15 um.
```

The simple thickness ratio is therefore

```text
15 / 0.11 ~ 136.
```

This ratio is **not** a mass-loading ratio because the materials, lateral coverage, coil geometry, density, and modal participation differ. It is only a scale indicator showing that the printed conducting structure is orders of magnitude thicker than the thin-film electrodes in the first benchmark.

That makes it unsurprising that a one-dimensional effective modulus calibrated to/lightly representative of thin-electrode AT-cut resonators fails to transfer to the printed-coil identity at the several-percent level.

---

## 4. Consequence for the behavior-first interpretation

This source geometry strengthens the modeling requirement:

```text
quartz thickness alone
!= complete resonator identity.
```

For a printed/electroded device, the relevant identity includes at minimum

```text
quartz 3-D geometry
+ cut/orientation
+ electrode/coil geometry
+ conductor mass and stiffness
+ electrical boundary conditions
+ active vibrating region
+ mechanical mounting/environment.
```

The frozen Layer-0 equation remains useful as the dominant thickness-mode limit, but the several-percent held-out miss is now understood as evidence that its domain of validity is restricted.

This does not itself support an ARK substrate ontology. It supports the more general current modeling principle:

> **A measured recurrence belongs to the complete bounded identity and is an expression of that identity's solved behavior, not a number assigned to quartz material independently of its actual structure.**

---

## 5. Next non-fitted use of the geometry

The next quantitative extension should not tune an effective modulus to the printed device.

A stronger route is to build a bounded loading calculation using independently sourced conductor geometry/material properties and explicit uncertainty ranges. The goal would be to predict at least the **sign and scale** of the frequency shift caused by adding the printed electrode/coil structure before comparison with the reported resonance.

Because the accessible source specifies conductive-path thickness and lateral electrode scale but not yet all cured-film mechanical properties or a complete coil mass distribution, the first calculation should be an uncertainty-bracketed model rather than a single precision number.

The important discipline is:

```text
source geometry/material bounds
-> predicted loading interval
-> predicted resonance interval
-> compare afterward
```

not

```text
observed resonance
-> choose effective loading until it matches.
```
