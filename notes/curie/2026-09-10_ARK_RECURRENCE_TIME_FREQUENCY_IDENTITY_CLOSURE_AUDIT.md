# 2026-09-10 Research — ARK Recurrence, Time, Frequency, and Identity-Closure Audit

**Status:** PARAMOUNT LINEAGE / SEMANTIC-DECOMPOSITION AUDIT — NOT A CANONICAL LAW  
**Research date:** 2026-09-10  
**Primary historical scope:** Papers XV, XVI, XVIII, and XXIV, with Paper XXV included as adjacent lineage because it exposes an important later semantic fork in `omega`.  
**Context:** Companion to `2026-09-10_ARK_MECHANICAL_CORE_MAXWELL_FARADAY_AND_RATE_EMERGENCE.md`, `2026-09-10_MATTER_SUBSTRATE_FORWARD_COUPLING_FORMALIZATION.md`, and `2026-09-10_STUDYING_THE_THREE_BODY_PROBLEM_WITH_ARK.md`.

---

## 1. Purpose

The current mechanical program requires a cleaner answer to a deceptively simple question:

> **What, exactly, is `omega` in ARK?**

Historically, the symbol has carried several jobs at once:

- a recursion-rate anchor,
- an angular rate,
- a clock/frequency-like quantity,
- a convergence/stabilization control,
- a state-derivative ratio,
- and, later, a signed internal–external pressure balance.

Those meanings cannot simply be merged because they do not all have the same dimensional or dynamical role.

This note therefore does **not** choose a new canonical definition by preference. It reconstructs the lineage, identifies contradictions and target-sensitive uses, separates physical recurrence from its numerical representation, and freezes a small set of candidate distinctions that future mechanics must either derive or reject.

The central epistemic rule is:

> **Do not repair historical semantic drift by silently redefining the symbol. Preserve the drift, then determine which physical quantities the mechanics actually require.**

---

## 2. Executive finding

The historical corpus does not currently support treating `omega` as one unambiguous fundamental scalar.

Across the lineage, `omega` appears in at least five materially different roles:

1. **Paper XV:** target-sensitive reciprocal anchor, including `omega = 1/i_obs`, with adaptive `omega` used to steer unstable simulations.
2. **Paper XVI:** recursive/angular rate, including `omega = 2pi/tau_r` and alternatively `omega = d theta^c/dt` at equilibrium; explicitly distinguished from ordinary emitted frequency `f`.
3. **Paper XVIII:** geometric response `omega = 1/cos(theta^c)` or `sqrt(1 + (d tau^c/dt)^2)`, while also being used as angular frequency in `T = 2pi/omega` and as a clocking rate.
4. **Paper XXIV:** local recursion/update rate `omega = partial theta^c / partial tau^c`, with time represented as `Delta t = 1/omega`, while a separate standing-wave calculation again uses angular eigenfrequencies.
5. **Paper XXV:** signed internal–external pressure-balance residual, `omega = P_int - P_ext`, where positive and negative signs indicate different structural tendencies.

Without an explicit normalization/bridge proving equivalence, these are **not the same physical object**.

The strongest immediate conclusion is therefore:

> **Historical `omega` is an overloaded symbol. The current framework should not use it as an independently prescribed fundamental rate until its distinct historical roles are decomposed and re-derived from the mechanical state.**

This conclusion strengthens the Rate-Emergence Principle already recorded in the mechanical-core note.

---

## 3. Historical lineage audit

### 3.1 Paper XV — `omega` as target-sensitive anchor and convergence control

Paper XV contains an important conceptual statement that time is not a fourth geometric axis. It describes time as a derivative behavior of scalar recursion under slope, tension memory, stiffness, and entropy progression.

However, the numerical implementation is not suitable as a modern foundational derivation.

The paper's update system explicitly uses the observed target `t_obs` in the slope update:

```text
theta^c_(t+1) = arccos(tau^c_(t+1) / t_obs)
```

Its initialization protocol then uses

```text
omega = 1 / i_obs
```

for mass-based identities, and asymmetric cases allow an adaptive correction of the form

```text
omega_(r+1)
=
omega_r + epsilon DeltaS_t sign(Delta theta^c).
```

The paper states that this adaptive `omega` allows the system to spiral into the slope band required to match the Higgs identity curve.

#### Modern classification

- **Conceptual ancestry:** useful.
- **Forward derivation of a physical rate:** not established.
- **Target leakage risk:** explicit.
- **Adaptive-rate freedom:** explicit.
- **Modern use:** provenance only unless independently reconstructed.

Paper XV is especially important because it shows why the modern rule must be stricter: a rate that is initialized from the answer or adjusted to achieve convergence cannot later be cited as evidence that the rate emerged from the mechanics.

---

### 3.2 Paper XVI — `omega` as persistence/recursion rate

Paper XVI gives one of the clearest early physical interpretations:

```text
omega = 2pi / tau_r
```

where `tau_r` is the natural recursive tension period.

It also gives the alternative equilibrium expression

```text
omega = d theta^c / dt
```

and explicitly says `omega != f`: the quantities may share frequency-like units, but `omega` is described as the internal recursive lock rather than an externally emitted frequency.

Paper XVI also contains the useful statement:

> **Frequency is a symptom, not a fundamental quantity.**

with the qualitative relation

```text
f proportional to 1 / tau^c.
```

The same paper frames measured temporal passage as a count of completed recursive events.

#### What survives conceptually

The durable idea is not the specific historical formula. It is the causal ordering:

```text
state / persistence / forcing
    -> recurrence behavior
    -> observable frequency
```

rather than

```text
choose frequency
    -> make the state obey it.
```

#### Problems requiring audit

Paper XVI also writes

```text
Perceived time = integral omega(t) dt = cumulative recursion count.
```

If `omega` is an angular rate, this integral is phase/angle, not a duration. If it is ordinary cycle frequency, the integral is cycle count. Either interpretation can be physically useful, but neither is literally elapsed time without a declared calibration convention.

That is an early sign of the semantic conflation this note is intended to separate.

---

### 3.3 Paper XVI — the first `pi` / closure construction

Paper XVI argues that persistent identity naturally recloses into a circular feedback loop in scalar state space and introduces

```text
r = tau^c / k^c
C = theta^c tau^c / omega
pi = C / (2r).
```

It then interprets `pi` as a signature of recursive scalar closure.

The physical idea worth preserving is **closure**.

The historical claim that this derives the numerical value of `pi` is too strong. Once the trajectory is assumed to be circular and the state variable is parameterized angularly, the circumference/radius relation already imports circular geometry.

Modern classification:

- **Closed recurrence as a candidate physical requirement:** retain for testing.
- **Circular geometry as necessarily lowest-energy identity form:** unproven.
- **Derivation of the numerical value of `pi`:** not established.

---

### 3.4 Paper XVIII — recurrence, `2pi`, and inverse time/frequency

Paper XVIII places the recurrence, `pi`, and time/frequency arguments directly beside one another.

For a closed identity cycle it writes

```text
T = 2pi / omega
```

and

```text
omega = d theta^c / dt,
```

so that

```text
integral_0^T omega dt
=
Delta theta^c
=
2pi.
```

This is a correct closure identity **if** `theta^c` is functioning as an angular phase measured in radians and `omega` is its angular rate. But in that case, `2pi` is the radian representation of one complete traversal. It is not itself a new physical ingredient.

A cleaner invariant statement is therefore:

```text
one complete recurrence = one closed traversal.
```

Introduce a normalized phase-in-turns variable `chi` only as audit notation:

```text
closed cycle: integral_cycle d chi = 1.
```

If radians are preferred, define

```text
phi = 2pi chi,
```

so

```text
integral_cycle d phi = 2pi.
```

The physical closure is the same in either representation.

This distinction matters because it separates:

- the **existence of recurrence**, which can be physical,
- from the **coordinate used to label recurrence**, which is conventional.

---

### 3.5 Paper XVIII — `omega = 1/cos(theta^c)` and dimensional ambiguity

Paper XVIII also uses

```text
theta^c = arctan(d tau^c / dt)
```

and then

```text
omega = 1 / cos(theta^c)
      = sqrt(1 + (d tau^c/dt)^2).
```

This construction contains a dimensional/normalization problem unless the derivative has first been rendered dimensionless by a declared scale.

`1/cos(theta^c)` is dimensionless. Yet the same `omega` is elsewhere treated as a frequency/rate.

Therefore this formula cannot be carried into the modern kernel as a physical frequency without recovering the missing normalization map.

The same paper's executable loop reinforces the problem: it uses `Delta t` to calculate `d tau^c/dt`, then computes `omega`, while later saying that `Delta t` itself is emergent from `theta^c` or `omega`.

That can be legitimate only if an independent closure relation determines all quantities simultaneously. As rendered, however, the simulation already supplies the timestep and sometimes terminates at a known physical target. It therefore does not constitute a derivation of time from the rate.

---

### 3.6 Paper XVIII — historical quartz interpretation

Paper XVIII contains an explicit quartz discussion. It proposes that voltage-driven oscillation of `theta^c` creates recurring peaks in

```text
omega = 1 / cos(theta^c)
```

and then relates two peaks to one full vibration cycle.

This is useful as provenance because quartz was already being used as a bridge between mechanical recurrence and timekeeping.

It is **not yet an ARK derivation of quartz resonance**.

The modern opportunity is much better defined:

> Given quartz material state, geometry, electrodes, boundary conditions, and electrical drive, can the frozen ARK constitutive mechanics produce the observed deformation, natural resonances, driven response, and relaxation **without inserting the resonance rate as a primitive input**?

That is a clean calibration problem.

---

### 3.7 Paper XXIV — `omega` shifts toward an emergent state ratio

Paper XXIV changes the definition again.

Its local recursion law is written as

```text
partial theta^c / partial t
=
- omega theta^c + k^c dS_t.
```

It then defines

```text
omega = partial theta^c / partial tau^c
```

and describes `omega` as the local update rate of recursion.

This is conceptually closer to the modern idea that rate should be a relationship among changing state variables rather than an externally prescribed clock.

Paper XXIV also says:

```text
Delta t = 1 / omega.
```

But Paper XVIII used

```text
T = 2pi / omega.
```

These are compatible only if the symbol changes convention between ordinary frequency and angular frequency, or if `Delta t` means a different interval than one complete cycle.

That distinction was not kept explicit historically.

Therefore:

> **The corpus itself demonstrates that `omega` alternated between cycle rate, angular rate, update rate, and state ratio.**

---

### 3.8 Paper XXIV — standing-wave rate emergence

Paper XXIV also contains a more mechanically promising route.

In a closed, approximately uniform domain it writes a separated oscillatory solution with

```text
T_double_dot + Omega^2 T = 0
```

and

```text
Omega^2 = (k^c / tau^c) kappa,
```

with a spatial eigenvalue in the 1-D example

```text
kappa_n = (n pi / L)^2.
```

Thus

```text
omega_n = sqrt(k^c / tau^c) (n pi / L).
```

This is structurally important because the rate is now an **eigenvalue of the mechanical/boundary problem** rather than an independently chosen stabilizer.

However, this historical result is not yet canonical because:

- the dimensional normalization of `k^c` and `tau^c` has not been audited,
- the common action/energy from which the equation follows has not been reconstructed,
- the relation may have been selected to resemble a familiar wave equation,
- and Paper XXIV elsewhere uses `omega` with incompatible meanings.

The modern task is therefore not to accept `omega^2 = k^c/tau^c` by analogy. It is to determine whether an audited action/conservation law forces the same structure.

---

### 3.9 Paper XXIV — energy/persistence ancestry

Paper XXIV H.10 writes the historical energy-like relation

```text
d/dt integral_Omega [
    1/2 k^c (theta^c)^2
    + tau^c (partial_t theta^c)^2
] dV
=
- integral_Omega theta^c omega (partial_t theta^c) dV.
```

This independently preserves two pieces relevant to the current mechanical program:

- deformation-like storage `1/2 k^c (theta^c)^2`,
- and a rate-dependent persistence term proportional to `tau^c (partial_t theta^c)^2`.

But the coefficient, dimensions, and conservation statement remain unaudited.

For current derivation work, use a neutral placeholder if needed:

```text
u_pers
=
1/2 M_theta^c (D theta^c)^2,
```

and ask whether the historical ancestry plus dimensions actually force

```text
M_theta^c = tau^c
```

or some fixed mapping.

Do **not** choose that identification merely because it produces a desirable oscillator frequency.

---

### 3.10 Paper XXV — a decisive semantic fork

Paper XXV makes the overloading of `omega` explicit by assigning it a completely different role:

```text
omega = P_int - P_ext
```

with

```text
P_int proportional to (theta^c)^2 kappa^c
P_ext proportional to DeltaS_t.
```

The paper then uses the **sign** of `omega`:

```text
omega > 0  -> condensation favored
omega < 0  -> expansion or decay favored
omega ~= 0 -> stable identity.
```

It also says `omega` does not propagate independently and is implicit in the coupled evolution of the other scalars.

This is highly relevant to the present discussion because it shows that a signed `omega` did exist in the later lineage. But it also demonstrates why the sign cannot simply be imported into the earlier frequency interpretation:

> A signed pressure-balance residual and a recurrence frequency are not automatically the same dimension or physical observable.

The modern framework should therefore preserve the *idea of signed evolution/balance* while refusing to call it frequency until a bridge is derived.

---

## 4. Candidate modern decomposition — temporary audit notation only

The purpose of the following notation is to prevent semantic collisions while the mechanics are reconstructed. **No new fundamental scalar is being declared.**

### 4.1 Signed state-evolution rate

Use provisionally

```text
Omega_evo^c
```

for the signed rate/orientation of an identity or state trajectory through its relevant state space.

Conceptually:

```text
Omega_evo^c > 0 -> evolution in one local orientation
Omega_evo^c < 0 -> evolution in the opposite local orientation
Omega_evo^c = 0 -> local turning/stationary point in that coordinate.
```

This is the natural home for the current intuition about arrow reversal.

A sign change means **the trajectory through state space reversed direction**. It does not require coordinate time itself to run backward.

### 4.2 Recurrence frequency

Use provisionally

```text
f_rec >= 0
```

for ordinary cycle frequency when a bounded state trajectory closes or nearly closes.

Then

```text
f_rec = 1 / T_rec.
```

If an angular/radian representation is useful, define

```text
omega_rec = 2pi f_rec.
```

The factor `2pi` belongs to the radian representation of one complete cycle, not to a separate physical cause.

### 4.3 Balance residual

The Paper XXV quantity

```text
P_int - P_ext
```

should temporarily be called what it is — a **balance residual** — until its units and dynamical role are independently reconciled with the recurrence mechanics.

Do not assume

```text
balance residual = recurrence frequency = signed evolution rate.
```

Any equality among those quantities must be derived.

---

## 5. Relational time — measurement after change

The current conceptual discussion suggests a more precise formulation of emergent time.

At the most primitive observable level, two systems can change relative to one another without first assigning seconds.

Let `q_A` and `q_B` be state observables of two evolving systems. Introduce an arbitrary monotonic ordering parameter `lambda` only as mathematical bookkeeping:

```text
dq_A / dq_B
=
(dq_A/dlambda) / (dq_B/dlambda).
```

The ratio can be meaningful even if `lambda` itself has no physical clock interpretation.

A clock is then a physical system chosen because some part of its evolution is reproducible enough to serve as a reference.

For recurrence counters:

```text
N_A / N_ref
```

already compares physical evolution before a unit such as the second is assigned.

A conventional time coordinate can then be calibrated from the reference recurrence.

This suggests the hierarchy:

```text
physical state change
    -> repeatable recurrence or another reference evolution
    -> comparison between systems
    -> calibrated clock scale
    -> numerical elapsed time.
```

This is a **candidate ontological interpretation**, not an empirical proof that conventional spacetime descriptions are invalid.

The current ARK question is sharper:

> Can the mechanical PDE determine the relative rates of physical state evolution and clock recurrence from local state and boundary conditions?

If yes, measured time can remain operationally real while being ontologically secondary.

---

## 6. Three different kinds of apparent circularity

The time/frequency discussion requires care because not all circular-looking structures are epistemically equivalent.

### 6.1 Benign definitional reciprocity

For a recurring physical process:

```text
f = 1/T.
```

This does not explain the mechanism that produced `T`; it simply expresses the reciprocal definitions of cycle rate and cycle duration.

Likewise,

```text
omega_rec = 2pi f
```

is a representation conversion between cycles and radians.

No causal claim should be extracted merely from these identities.

### 6.2 Fundamental coupled closure

It remains possible that geometry, persistence, and rate are mutually constraining rather than hierarchically derived one at a time.

A system of the form

```text
C(theta^c, grad theta^c, D theta^c, k^c, tau^c, ...) = 0
```

may determine state and rate simultaneously.

That is not automatically vicious circularity. Fundamental physics can be specified by a coupled closure relation.

### 6.3 Vicious / target-leaking circularity

The unacceptable form is:

```text
insert observed target time or frequency
    -> initialize/steer theta^c or omega
    -> recover the target
    -> claim the target emerged independently.
```

Paper XV contains explicit examples of this problem, and Paper XVIII contains related timestep/known-anchor concerns.

Modern derivations must therefore declare whether `t` in the PDE is:

- a computational integration parameter,
- an externally calibrated laboratory coordinate,
- a measured local clock output,
- or a derived variable.

Those roles cannot be silently exchanged inside one derivation.

---

## 7. Candidate mechanical interpretation of bounded recurrence

The current discussion suggests a testable hypothesis:

> **Oscillation may be one possible expression of continued driven change when permanent identity reconfiguration is bounded by persistence and restoring mechanics.**

Schematic causal chain:

```text
external drive / dS_t-like perturbation
    -> tendency to reconfigure state

persistence / tension memory
    -> resistance to loss of current identity

stiffness / restoring response
    -> bounded deformation

bounded deformation + persistence
    -> possible recurring trajectory
    -> observable recurrence frequency.
```

This is not yet a law.

To avoid selecting the answer, a neutral local mechanical prototype is preferable:

```text
u_def = 1/2 k^c (theta^c)^2

u_pers = 1/2 M_theta^c (D theta^c)^2.
```

If an audited action/conservation principle yields, in a locally constant regime,

```text
M_theta^c D^2 theta^c + k^c theta^c = S_drive,
```

then the source-free natural rate would follow as a solution:

```text
omega_0^2 = k^c / M_theta^c.
```

The critical point is causal order:

```text
mechanics -> natural rate
```

not

```text
chosen rate -> mechanics.
```

Whether `M_theta^c` is actually `tau^c`, a function of `tau^c`, or a different derived coefficient remains an open dimensional/ancestry question.

---

## 8. Quartz as the first recurrence calibration problem

Quartz is a useful first test because it forces the framework to distinguish several things that the historical papers blurred together.

### Required qualitative distinctions

A successful ARK forward model should reproduce, without rate insertion:

1. **Static forcing:** a sustained electrical bias produces a bounded deformation/shift rather than indefinite self-oscillation merely because voltage exists.
2. **Driven forcing:** a time-varying electrical input produces a driven mechanical response.
3. **Natural resonance:** preferred resonant modes arise from material state, geometry, inertia/persistence, stiffness, and boundary conditions.
4. **Drive versus natural rate:** forcing frequency and natural frequency are distinct quantities even when resonance makes them coincide strongly.
5. **Dissipation:** finite damping/quality factor must arise from an explicit energy-loss channel rather than being hidden in a tuned `omega` stabilizer.
6. **Sign versus frequency:** the sign of instantaneous deformation/evolution is not the same thing as the nonnegative cycle frequency.

### Forward test

Inputs should be restricted to independently specified physical state and boundary information:

```text
material composition / state
geometry and orientation
electrode geometry
electrical forcing history
mechanical boundary conditions
environmental conditions
```

The ARK-side constitutive law must then produce a deformation history

```text
theta^c(x,t)
```

or its modern successor.

Only **after** solving the trajectory should a recurrence rate be measured from the solution.

A benchmark should compare:

```text
predicted mode shape
predicted natural frequency
predicted static deformation
predicted driven amplitude/phase
predicted relaxation/damping
```

against conventional piezoelectric/resonator theory and experiment.

A failure to distinguish static deformation from sustained oscillation would falsify the proposed recurrence mechanics in this regime.

---

## 9. Implication for the quantum-arrow discussion

The modern decomposition gives a cleaner interpretation of reversible/reshaped trajectory experiments.

A state trajectory may satisfy

```text
Omega_evo^c > 0
```

then be driven through

```text
Omega_evo^c = 0
```

and later

```text
Omega_evo^c < 0.
```

That would mean the system's local progression through an identified state coordinate has reversed.

It does **not** imply that a global coordinate time variable has reversed direction.

This distinction is consistent with the oldest durable conceptual claim in the corpus: the arrow belongs to the dynamics, not to an independently flowing temporal substance.

However, no present ARK equation yet proves that an experimentally measured trajectory reversal is specifically a substrate/aether flux.

To justify the stronger statement that forcing “squeezes substrate out” of a system, the framework would need an independently defined conserved substrate density/flux, for example schematically

```text
partial_t rho_a + div J_a = source/sink,
```

plus an energy/momentum ledger quantitatively linking the measured excess energy to that flux.

Until then, the substrate-flow interpretation remains a candidate mechanism rather than a derived conclusion.

---

## 10. Constraints this audit places on the forward PDE

Any modern ARK forward equation should now satisfy all of the following.

### 10.1 Rate emergence

A sustained recurrence rate must be measured from the solved state unless an independently demonstrated constitutive relation determines it.

No adaptive `omega` may be used merely to improve convergence.

### 10.2 Sign separation

The variable carrying **direction of state evolution** must be distinguishable from the variable carrying **cycle-frequency magnitude**.

A nonnegative recurrence frequency should not be forced to perform the work of a signed trajectory derivative.

### 10.3 Closure representation

One complete recurrence is the physical invariant.

`1 turn`, `360 degrees`, and `2pi radians` are representations of the same closure. The theory should not treat the selected angular unit as an additional physical mechanism.

### 10.4 Explicit time status

Every derivative with respect to `t` must state what `t` means in that derivation.

At minimum distinguish:

```text
integration parameter
laboratory clock coordinate
local clock observable
derived relational duration.
```

### 10.5 Conservation before interpretation

If reversal, oscillation, or clock-rate change is attributed to substrate reconfiguration, the accompanying energy and momentum must appear in a closed ledger.

### 10.6 No target-derived rate

Known frequencies, periods, lifetimes, or clock readings may be used as comparison targets only after the forward state law and initialization have been frozen.

---

## 11. Proposed modern status of historical claims

### RETAIN AS CONCEPTUAL ANCESTRY

- Time need not be treated ontologically as an independently flowing substance.
- Physical systems undergo local change regardless of whether an observer assigns clock units.
- A clock is a repeatable physical evolution used as a comparison standard.
- Frequency can be an emergent symptom of the state mechanics.
- Persistent/bounded systems may admit closed recurring trajectories.
- Entropy/forcing and persistence can change local evolution rates.
- Direction of state evolution is conceptually distinct from coordinate time.

### RETAIN AS CANDIDATE MECHANICS REQUIRING DERIVATION

- `tau^c` as the coefficient controlling persistence/inertial response.
- `k^c` as restoring stiffness in `1/2 k^c(theta^c)^2`.
- recurrence emerging from persistence plus restoring deformation.
- local clock-rate differences emerging from differing mechanically solved recurrence rates.
- signed evolution reversal under a reversed/feedback-controlled drive.

### DO NOT PROMOTE WITHOUT AUDIT

- `omega = 1/cos(theta^c)` as a physical frequency.
- `omega = sqrt(1+(d tau^c/dt)^2)` without a dimensional normalization map.
- `omega = 2pi/tau_r`, `omega=dtheta^c/dt`, `omega=partial theta^c/partial tau^c`, and `omega=P_int-P_ext` as automatically equivalent.
- `Delta t = 1/omega` and `T=2pi/omega` as the same statement without declaring whether `omega` means cycle frequency or angular frequency.
- adaptive `omega` as evidence of emergent physical rate.
- the claim that ARK derives the numerical value of `pi` merely from circular recursion.
- the historical quartz `1/cos(theta)` spike construction as a derivation of crystal resonance.
- arrow-of-time experiments as direct evidence for a substrate ontology.

---

## 12. Immediate derivation program

The recurrence audit now suggests a concrete order of operations.

1. **Dimensions / normalization audit:** determine the historical units of `theta^c`, `tau^c`, `k^c`, `dS_t`, and every historical `omega` relation.
2. **Action / conservation audit:** test whether the deformation term `1/2 k^c(theta^c)^2` and a persistence term can be derived together consistently.
3. **Temporary symbol split:** during derivation, keep signed state evolution, recurrence frequency, and pressure-balance residual distinct.
4. **Quartz forward benchmark:** derive static, driven, resonant, and dissipative behavior without inserting the natural frequency.
5. **Clock comparison:** once a recurrence solution is obtained, define relational duration by comparing it with a separate reference recurrence rather than assuming a universal physical clock.
6. **Quantum-arrow application:** only after the mechanics are frozen, test whether feedback-induced state-trajectory reversal has a distinctive ARK prediction beyond standard measurement/backaction accounting.
7. **Matter–substrate / one-body solver:** carry the same rate-emergence constraints into translational and inertial dynamics.
8. **Two-/three-body work:** only then allow recurrence/history terms into multi-body forward dynamics.

---

## 13. Working principle after this audit

The cleanest current statement is:

> **Change is physical. Recurrence is a property of some changing systems. Frequency is a measure of recurrence. Measured time is a calibrated comparison among changing systems. The physical rate at which a system evolves should be produced by its mechanics, not inserted merely because our bookkeeping uses a time coordinate.**

This does not prove that ARK is the correct ontology of nature.

It does provide a stricter requirement for any future ARK equation claiming to explain time, frequency, oscillation, or the arrow of evolution:

```text
state + mechanics + boundaries
    -> trajectory
    -> recurrence / signed evolution
    -> clock comparison
```

rather than

```text
prescribed clock/rate
    -> target-compatible trajectory
    -> claim of emergence.
```

That distinction is now a formal research constraint for the project.
