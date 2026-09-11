# 2026-09-11 Research — Pre-ARK Scalar Ancestry Audit

**Status:** PARAMOUNT LINEAGE / FOUNDATIONAL SEMANTIC AUDIT — NOT AN ESTABLISHED LAW  
**Research date:** 2026-09-11  
**Primary historical scope:** Papers VI, VII, and VIII reviewed directly from the preserved combined early corpus; Paper I artifact presence verified in the `Papers` branch, but its exact text was not independently machine-extracted in this pass. Paper XVI is used only as a later retrospective witness where explicitly labeled.  
**Purpose:** Test whether the current behavior-first mechanical interpretation of `theta^c`, `tau^c`, `k^c`, and forcing is genuinely ancestral to the pre-ARK framework or was imposed retroactively after Papers XV–XXV.

Companion current records:

- `2026-09-11_INTRINSIC_BEHAVIOR_IDENTITY_BOUNDARIES_AND_EMERGENT_PROPERTIES.md`
- `2026-09-10_ARK_RECURRENCE_TIME_FREQUENCY_IDENTITY_CLOSURE_AUDIT.md`
- `2026-09-10_ARK_MECHANICAL_CORE_MAXWELL_FARADAY_AND_RATE_EMERGENCE.md`
- `2026-09-10_MATTER_SUBSTRATE_FORWARD_COUPLING_FORMALIZATION.md`

---

## 1. Research question

The current reconstruction has converged on a behavioral hierarchy:

```text
intrinsic causal behavior
    -> identity + state + geometry + boundaries + environment
    -> effective properties / modes
    -> measured numerical values.
```

That interpretation is scientifically useful only if it is either:

1. genuinely supported by the historical ancestry of the framework, or
2. explicitly acknowledged as a new reconstruction rather than falsely projected backward.

The specific questions for this audit were therefore:

```text
Was theta^c originally a state/deformation variable or merely a time-derived measurement?

Was tau^c originally persistence/history, or was that meaning added later?

Was k^c originally a constitutive resistance/restoring behavior, or merely a fitted coefficient?

Was the later dS_t concept already present as external forcing in the thermodynamic work?

Did identity boundaries and mode selection matter before ARK?

Did recurrence rate already appear as an output of mechanics before omega became a five-scalar 'anchor'?
```

The answer is mixed, but highly informative.

---

## 2. Executive finding

The current behavior-first interpretation is **not merely a late reinterpretation**. A substantial mechanical core is already explicit in Papers VI–VIII:

```text
theta^c  -> slope/configuration/deformation state
k^c      -> resistance to changing that state
tau^c    -> persistence / relaxation / history of that state
boundary forcing -> external drive of that state
```

Paper VI describes identity as a persistent bounded/topological configuration whose deformation energy is repeatedly written as

```text
u_def ~ 1/2 k^c (theta^c)^2.
```

Paper VII continues that structure and explicitly treats `k^c Delta theta^c` as tension-like response, while using `tau^c` to govern memory loss and persistence.

Paper VIII then gives a particularly important pre-ARK dynamical skeleton:

```text
partial_t theta
=
D laplacian(theta)
- theta/tau
+ F_boundary.
```

This already separates:

- spatial redistribution,
- persistence/relaxation,
- and external forcing.

It also treats boundary conditions as physically active and capable of selecting standing/oscillatory behavior.

However, the audit exposes three major semantic problems that the modern reconstruction must not conceal:

1. **`tau^c` underwent severe dimensional drift.** In Papers VI–VIII it is predominantly a relaxation/persistence time with units of seconds. Later Paper XVI also gives an action-like `E × t` interpretation with units `J s`. Those are not the same quantity without a derived normalization/bridge.
2. **`theta^c` was historically calibrated through time ratios.** The early framework's operational definition ties causal slope to proper-time versus coordinate-time behavior. If the modern ontology treats measured time as emergent from change, that historical definition cannot simultaneously serve as a time-independent primitive without additional reconstruction.
3. **The later `dS_t` causal-pressure scalar does not appear to be the same object as Paper VIII entropy.** In the reviewed Paper VIII corpus, entropy `S^c` is largely an output/measure of configuration complexity and irreversible slope evolution, while external drive is a separate forcing term `F_u`. The later ARK move that names external causal pressure `Delta S_t` / `dS_t` appears to fuse roles that were previously separate.

The strongest current conclusion is therefore:

> **The durable ancestry is behavioral, not symbolic. The pre-ARK corpus strongly supports deformation, resistance, persistence/history, boundary forcing, and bounded identity as recurring mechanical roles. It does not yet justify assuming that the later symbols `theta^c`, `tau^c`, `k^c`, `dS_t`, and `omega` each remained one dimensionally invariant fundamental scalar across the lineage.**

---

## 3. Source scope and limitation

### 3.1 Directly reviewed source layers

The preserved combined early corpus contains direct text for:

- Paper VI — *Particle Identity and Topological Emergence in the Aetheron Framework*,
- Paper VII — *Quantum Curvature and the Causal Geometry of Substrat Identity*,
- Paper VIII — *Thermodynamic Flow and Substrat Equilibrium* and its extended continuation.

The repository `Papers` branch independently confirms separate archived PDF artifacts for Papers I, VI, VII, and VIII.

### 3.2 Paper I limitation

The archived Paper I artifact is present in the repository as:

```text
01 Aetherwave_Temporal_Geometry_Revision_4.pdf
```

but its exact body text was not independently extracted into the current parsed-library source set during this audit.

Therefore this note does **not** claim a direct line-by-line Paper I audit.

Paper XVI's appendix later describes Paper I ancestry using relations such as

```text
theta^c = arctan(d tau_proper / dt_coordinate),
```

and retrospectively characterizes `theta^c` as a scalar angle of causal progression. That is useful lineage evidence, but it is a later witness and must not be substituted for the original Paper I artifact.

A future provenance pass should extract Paper I directly and compare its exact notation to these later summaries.

---

## 4. `theta^c` ancestry — durable geometric role, unresolved primitive status

### 4.1 Paper VI

Paper VI describes `theta^c(x,t)` as the causal slope and the directional gradient of causal advancement. Particle identity is defined as persistence of a topological configuration in this slope field.

That is already much closer to a **state/configuration variable** than to a mere fitted output.

The paper repeatedly treats local or distributed `theta^c` as something that can:

```text
be deformed,
form gradients,
form knots,
relax,
interfere,
carry boundary conditions,
and store energy through its magnitude.
```

This supports the current provisional interpretation:

```text
theta^c -> generalized configuration/deformation coordinate.
```

### 4.2 But the historical observable map is time-derived

The early and later retrospective definitions also tie `theta^c` to proper-time versus coordinate-time ratios.

That creates an important reconstruction problem.

If the modern framework says:

```text
mechanics / state evolution
    -> recurrence
    -> clock comparison
    -> measured time,
```

then it is circular to declare a `theta^c` derived from measured time dilation to be the independent pre-temporal cause of the same measured time behavior unless a separate closure relation is supplied.

This does not require discarding the historical time-dilation mapping. It suggests reclassifying it as an **observable/calibration projection** of a deeper state variable unless the original geometry independently determines `theta^c`.

### 4.3 Current status

Retain:

```text
theta-like state/configuration/deformation behavior.
```

Do not yet assume:

```text
theta^c = arctan(d tau_proper/dt)
```

is the fundamental definition at the deepest layer.

The historical formula may remain a valid measurement map in a regime where clock rates are already defined.

---

## 5. `tau^c` ancestry — persistence is real; the scalar's units are not stable

### 5.1 Paper VI: explicit persistence / relaxation time

Paper VI is unusually clear about the physical role.

It calls `tau^c` tension memory and describes it as resistance of the substrate to changes in slope. Identity survives when deformation persists rather than immediately relaxing.

The characteristic decay law appears repeatedly as

```text
partial_t theta^c = -theta^c/tau^c,
```

with

```text
theta^c(t) = theta^c_0 exp(-t/tau^c).
```

In this formulation, `tau^c` is plainly a **relaxation/persistence timescale**.

Paper VI even calibrates neutron `tau^c` from the measured neutron lifetime, converting the half-life-like value into an effective exponential persistence time. This is important epistemically:

> The historical interpretation of `tau^c` as persistence is strong, but the neutron numerical value is measurement-derived calibration, not an independent prediction of the persistence law.

### 5.2 Paper VII: memory remains a timescale

Paper VII continues the same role:

```text
tau^c -> slope-field memory / persistence time.
```

Its recaps explicitly assign seconds to `tau^c`, and its collapse/decoherence equations again use `-theta^c/tau^c`.

The paper also introduces memory-conditioned histories, barriers, and delayed response. This strengthens the interpretation of `tau^c` as a parameter controlling how strongly prior state remains dynamically relevant.

### 5.3 Paper VIII: memory becomes an actual response kernel concept

Paper VIII develops this substantially.

The field equation is written schematically as

```text
partial_t theta
=
D laplacian(theta)
- theta/tau
+ F.
```

It later introduces a history-dependent response of the form

```text
theta(t)
=
integral M(t,t') F(t') dt',
```

and says the width of the memory kernel is controlled by `tau`.

Most importantly, Paper VIII explicitly says that `tau` is not merely a passive decay constant but represents the geometric persistence of the causal fabric.

This is very strong ancestry for the modern role:

> **Previous configuration constrains present response.**

### 5.4 The dimensional break in later ARK

Paper XVI later gives `tau^c` an alternative construction such as

```text
tau^c = E times t
```

with units of action (`J s`), and also an integrated stiffness/rate expression.

That is not dimensionally equivalent to the Paper VI–VIII relaxation-time `tau^c` measured in seconds.

Therefore the modern framework must not silently average these meanings together.

There are at least two possibilities:

```text
A. one historical symbol was reused for distinct physical quantities,

B. an omitted normalization/conversion map was intended but never established.
```

Until that is resolved, the current mechanical derivation should preserve the **behavioral role of persistence/history** while using neutral coefficients where dimensional precision matters.

---

## 6. `k^c` ancestry — restoring resistance is old; its numerical values were often calibrated

### 6.1 Paper VI

Paper VI directly defines `k^c` as stiffness: how much force is required to deform the causal slope.

The local/deformation energy structure appears repeatedly as

```text
u_def = 1/2 k^c (theta^c)^2.
```

This is strong ancestry for the modern candidate interpretation:

```text
k^c -> constitutive resistance to deformation.
```

If `k^c` is locally fixed during a variation, this also gives the conjugate load form

```text
partial u_def / partial theta^c
=
k^c theta^c,
```

which is the same mechanical object that later became important in the Maxwell–Faraday lineage audit.

### 6.2 Paper VII

Paper VII preserves the same quadratic energy and explicitly uses relations of the form

```text
T_AB = k^c Delta theta^c
```

and

```text
E_link = 1/2 k^c (Delta theta^c)^2.
```

Again, this is behaviorally elastic/restoring.

Paper VII also makes `k^c` state-dependent in some sections, for example through a gradient-dependent amplification law. That is historically important because it means **conditional/effective stiffness is not a purely modern addition**.

### 6.3 Calibration warning

The same papers frequently choose very large numerical `k^c` values from known nuclear, binding-energy, or other target scales and then use those values to reproduce known energies.

Therefore:

- the **role** `k^c -> resistance/restoring response` has strong ancestry,
- the **specific historical numerical values** do not automatically constitute first-principles derivations,
- and the exact dimensions/normalization of `k^c` must be reconstructed per formulation.

This directly supports the modern behavior-first rule:

> The constitutive response is the candidate intrinsic content; a particular effective stiffness value can be a solution conditioned on state and scale.

---

## 7. The most important semantic split: Paper VIII entropy versus external forcing

This is the strongest new finding of this audit.

### 7.1 Paper VIII does not use the later `dS_t` scalar in the reviewed thermodynamic corpus

Across the preserved Paper VIII section reviewed here, the later ARK symbols

```text
dS_t
Delta S_t
```

were not found as the governing external-drive scalar.

Instead, Paper VIII keeps two jobs conceptually separate.

### 7.2 Entropy `S^c`

Paper VIII defines entropy in terms of configuration degeneracy / complexity and its evolution under slope redistribution, memory decay, diffusion, and irreversibility.

Schematically:

```text
S^c = k_B ln(Omega_theta)
```

with `Omega_theta` built from slope gradients and persistence.

Entropy is therefore primarily a **state measure / result of evolution** in this formulation.

### 7.3 External forcing `F_u`

Paper VIII separately introduces a forcing term:

```text
partial_t theta
=
D laplacian(theta)
- theta/tau
+ F_u.
```

`F_u` is explicitly described as external or boundary-driven forcing: a geometric push injected where the environment/boundary no longer aligns with the internal state.

That is strikingly close to the **mechanical role currently being assigned to `dS_t`**:

```text
external imbalance / drive
    -> state reconfiguration.
```

### 7.4 Later semantic fusion

By Paper XVI and later ARK work, `Delta S_t` / `dS_t` is redefined as a causal-pressure gradient or external perturbation acting on the identity.

That means the later notation appears to combine concepts that Paper VIII had kept more distinct:

```text
Paper VIII:
    entropy S^c         -> state/irreversibility/configuration measure
    external forcing F  -> drive/source

later ARK:
    dS_t / Delta S_t    -> 'entropy' + external causal pressure / drive.
```

This may be a genuine conceptual advance, but it may also be a semantic conflation.

The modern reconstruction should **not assume the fusion is correct merely because the symbol persisted into ARK**.

### 7.5 Current implication

For the forward mechanical derivation, use neutral source notation until the lineage is resolved:

```text
S_drive or F_ext
```

for independently specified external forcing.

Treat thermodynamic entropy as a separate observable/accounting quantity unless a derivation proves that the source variable and entropy variable are the same physical object.

This prevents us from rebuilding the constitutive law around a historical naming choice.

---

## 8. Identity boundaries are not a late addition

The current viewpoint emphasizes that a collective property depends on which bounded physical structure is being treated as the identity.

This has clear pre-ARK ancestry.

### 8.1 Paper VI

Paper VI defines particle identities as localized, persistent slope configurations over a finite domain and explicitly gives boundary conditions for the field.

It also contains a dedicated identity-boundary / energy-transfer treatment in which incompatible overlapping configurations can remain distinct, bind, deflect, merge, or rupture depending on the energy difference relative to a stiffness-controlled threshold.

### 8.2 Paper VIII

Paper VIII goes further and makes the **boundary an active dynamical source**.

When the boundary is driven, it writes

```text
partial_t theta
=
D laplacian(theta)
- theta/tau
+ F_boundary.
```

The text then states that coherent boundary forcing can sustain standing curvature modes or persistent oscillations.

This is almost exactly the structural idea behind the current recurrence discussion:

```text
same underlying response behavior
+ different identity domain / boundary conditions
-> different collective modes and measured frequencies.
```

Therefore the modern emphasis on identity boundaries is not being imposed retroactively. It is a cleanup and strengthening of an already present pre-ARK concept.

---

## 9. Pre-ARK rate emergence exists — but the old formula is not dimensionally trustworthy

Paper VII contains an explicit oscillatory relation in which a mode frequency is written schematically as

```text
omega ~ sqrt(k^c/tau^c) times theta_0.
```

The conceptual ordering is important:

```text
stiffness + memory + state
    -> recurrence rate.
```

That is recognizably ancestral to the modern Rate-Emergence Principle.

But with the same paper also listing

```text
k^c : N rad^-2

tau^c : seconds,
```

the printed frequency relation does not have an obviously correct frequency dimension without another normalization factor.

Therefore the historical formula should be classified as:

**CONCEPTUAL ANCESTRY FOR RATE EMERGENCE — NOT A VALIDATED MODERN DISPERSION/OSCILLATOR LAW.**

Paper VIII also sometimes simply assumes

```text
omega approximately 1/tau^c
```

for thermal fluctuations. That is another example of a prescribed rate relation that should not be carried forward without derivation.

The durable result is the direction of explanation:

```text
mechanical state + boundaries
    -> recurrence
    -> measured rate.
```

---

## 10. A pre-ARK dynamical skeleton worth preserving for audit

The richest early equation is not the later five-scalar ARK update loop. It is the Paper VIII driven-relaxation form:

```text
partial_t theta
=
D laplacian(theta)
- theta/tau
+ F.
```

Do **not** promote this equation directly to a fundamental law.

It contains several phenomenological assumptions that require audit:

- `t` is already a coordinate parameter,
- `D` is supplied as a diffusion coefficient,
- `tau` is supplied as a relaxation time,
- the equation is first-order/dissipative rather than obviously conservative,
- and the source `F` is not derived from a common matter-field action.

But as an ancestry map, it is extremely useful because it separates the physical jobs cleanly:

```text
D laplacian(theta) -> spatial redistribution / coupling
-theta/tau        -> persistence loss / relaxation
F                  -> external drive / boundary perturbation.
```

A modern conservative theory may replace every mathematical term while preserving these **behavioral constraints**.

---

## 11. Local energy versus spatial-gradient energy already diverged before ARK

The current mechanical-core audit noted a tension between

```text
1/2 k^c (theta^c)^2
```

and a possible spatial energy

```text
1/2 k^c |grad theta^c|^2.
```

That ambiguity already exists in the pre-ARK corpus.

Papers VI and VII repeatedly use local quadratic slope energy:

```text
1/2 k^c (theta^c)^2.
```

Paper VII later proposes an action containing a gradient-energy term schematically like

```text
1/2 k^c |grad theta^c|^2
```

plus a memory-related term.

Those need not be mutually exclusive if `theta^c` itself is already a slope variable, but neither should they be silently identified.

The action/energy audit must determine whether the surviving theory contains:

```text
local deformation storage,
spatial deformation-gradient storage,
or both,
```

and what physical level each represents.

---

## 12. Dimensional drift table — preliminary

| Historical role | Papers VI–VIII | Later ARK drift / issue | Current audit posture |
|---|---|---|---|
| `theta^c` | angular/state slope, often radians; time-dilation mapping | also treated as generic state/deformation coordinate | retain state role; audit whether time ratio is measurement map rather than primitive definition |
| `tau^c` | relaxation/persistence time, commonly seconds | later also `E t` / action-like `J s` | preserve persistence behavior; split/normalize quantities until equivalence is derived |
| `k^c` | stiffness/resistance, often `N rad^-2` | sometimes state-dependent, sometimes domain-calibrated | preserve constitutive role; re-derive units/value per regime |
| entropy `S^c` | configuration/irreversibility measure | later `dS_t` becomes external causal pressure | keep entropy and drive separate pending derivation |
| external `F` | explicit boundary/environmental forcing | later role partly absorbed into `dS_t` | use neutral source notation in forward derivation |
| `omega` / rate | occasional derived/assumed recurrence relation | later promoted to independent five-scalar anchor, then overloaded | measure/derive rate after solving state where possible |

This is preliminary and should be expanded into a source-by-source dimensional ledger before a canonical action is chosen.

---

## 13. What appears genuinely ancestral

The following ideas survive this audit as recurring pre-ARK structure, though not as experimentally established laws of nature:

### A. Identity is a bounded persistent configuration

The papers repeatedly define identity by persistence of field geometry rather than by an intrinsic list of immutable particle properties.

### B. Deformation storage is quadratic in a state variable

The relation

```text
1/2 k^c (theta^c)^2
```

appears early and repeatedly.

### C. Stiffness is behavior, not merely a number

`k^c` is consistently described by what it does: resistance/restoring response to deformation.

### D. Memory is historical dependence

`tau^c` consistently carries the idea that prior configuration changes present response, even though its mathematical representation and units drift.

### E. Boundary conditions select collective behavior

The early corpus explicitly gives identity boundaries, driven boundaries, standing modes, hysteresis, and persistent configurations.

### F. Rate can be downstream of mechanics

Early oscillatory expressions already attempted to derive recurrence from stiffness/memory rather than make frequency the sole primitive.

These points strongly support the present behavior-first reconstruction as a recovery of an old structural thread rather than a wholly new overlay.

---

## 14. What should *not* be inherited automatically

The following historical features should remain provenance until reconstructed:

- the exact `theta^c` mapping from measured proper-time ratios as a deepest-level definition,
- numerical `k^c` values inferred from known target energies,
- neutron or particle `tau^c` values inferred directly from observed lifetimes and then treated as predictive inputs,
- `tau^c` being simultaneously a time and an action without a bridge,
- `omega = sqrt(k^c/tau^c) theta_0` with the printed historical dimensions,
- `omega approximately 1/tau^c` merely because a fluctuation needs a rate,
- phenomenological diffusion/memory coefficients inserted before a conservation derivation,
- the claim that entropy and external causal forcing are necessarily the same scalar,
- and the many domain-specific precision/ontology claims surrounding these equations.

---

## 15. A cleaner modern reconstruction suggested by the ancestry

This audit suggests that the safest primitive layer may initially be described by **roles rather than inherited scalar names**:

```text
q              -> local configuration/deformation state
R[q,state]     -> constitutive restoring/resistance behavior
H[history]     -> persistence/history dependence
S_ext          -> external matter/boundary source or drive
B              -> boundary/identity conditions.
```

Then derive:

```text
state evolution
    -> stable / unstable / relaxing / recurring solutions
    -> effective stiffnesses, memory times, eigenmodes, recurrence rates
    -> clock/thermodynamic/field observables.
```

Only after the dimensional and ancestry audits close should those objects be mapped back onto

```text
theta^c,
k^c,
tau^c,
dS_t,
omega.
```

This prevents historical notation from deciding the ontology before the mechanics do.

---

## 16. Implication for the current `dS_t` program

The immediate forward-modeling rule should change slightly.

Previously we have often written schematically:

```text
dS_t -> external forcing / causal pressure.
```

After this audit, the stricter form should be:

```text
S_ext / F_ext -> independently specified external drive
```

with the question

```text
Does the modern derivation force S_ext = dS_t ?
```

left open.

Likewise, a thermodynamic entropy functional should be derived from the solved state and energy/flux ledger rather than assumed identical to the source term.

If those two eventually become related by a conservation law, that relationship becomes a result.

If they remain distinct, the modern framework will have corrected a historical semantic fusion.

---

## 17. Implication for `tau^c` and the common action

The action audit must now explicitly test two historical `tau` families:

```text
Family A:
    tau_time
    -> relaxation / persistence timescale [s]

Family B:
    tau_action
    -> integrated tension / action-like quantity [J s or equivalent].
```

Do not set

```text
tau_time = tau_action
```

by symbol identity.

A constitutive relation may eventually connect them, for example through an independently derived energy scale, but that relation must be forced by mechanics/dimensions rather than notation.

This also means the temporary persistence coefficient

```text
M_theta^c
```

in the mechanical-core note remains necessary until the correct mapping is established.

---

## 18. Implication for time and `theta^c`

The earliest observable interpretation of causal slope uses relative clock behavior.

The modern emergent-time program therefore needs to distinguish:

```text
theta_obs
    -> a slope inferred from clock comparison / relativistic observable
```

from a possible deeper

```text
q_geom
    -> physical geometric/configurational state that exists before a clock convention is assigned.
```

They may ultimately be the same quantity under a measurement bridge.

But using the clock-derived expression as the primitive definition and then claiming to derive clocks from it would be target leakage at the ontological level.

The correct research question is:

> **Can the mechanical geometry independently determine the state whose observable projection reproduces the historical `theta^c` time-dilation map?**

---

## 19. Immediate research sequence after this audit

1. **Build a lineage-aware dimensions table, not a single-value table.** Record each historical definition of `theta^c`, `tau^c`, `k^c`, entropy/forcing, and `omega` with its source, role, units, and whether the quantity was measured, calibrated, assumed, or derived.
2. **Split entropy from source during derivation.** Use neutral `S_ext` / `F_ext` for external drive and a separate entropy functional/flux until a relation is proven.
3. **Split relaxation-time memory from action-like memory.** Do not use one `tau^c` symbol in the common action until dimensional closure identifies the correct object.
4. **Audit Paper I directly.** Recover the exact original causal-slope definition and determine whether later summaries accurately preserve it.
5. **Reconstruct the minimal boundary-value problem.** Start from configuration, restoring behavior, history/persistence, and boundary/source terms; derive whether bounded recurring modes exist without prescribing a rate.
6. **Use quartz as the first material calibration.** A frozen constitutive law must distinguish static deformation, transient relaxation, driven response, resonance, and dissipation from the same behavior set.
7. **Only then map the surviving mechanics back into ARK notation.** The symbols should label derived roles, not dictate them.

---

## 20. Core conclusion

The pre-ARK corpus contains more of the present mechanical intuition than expected.

The deep thread is already visible:

```text
bounded identity
    + deformable geometric state
    + resistance to deformation
    + memory of prior configuration
    + external/boundary forcing
    -> evolving response
    -> possible persistence, relaxation, rupture, or recurrence.
```

What changed later was largely **compression into a five-scalar language**.

That compression was useful, but it also appears to have merged quantities that the earlier papers sometimes kept distinct — most notably:

```text
entropy vs external forcing,
relaxation time vs action-like memory,
and measured temporal slope vs deeper configuration state.
```

Therefore the current project should not ask:

> “Which old five-scalar equation should we choose?”

It should ask:

> **“Which behavioral constraints survive the entire ancestry, and what is the smallest dimensionally coherent mechanics that makes those behaviors emerge?”**

That is now the preferred reconstruction path.
