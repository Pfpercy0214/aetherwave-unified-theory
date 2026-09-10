# RESEARCH_QUEUE — Curie

This queue prioritizes work by epistemic value, not by how impressive the result would look.

## Priority 0 — three-body dynamics and the matter–substrate constitutive bridge

**Status:** PARAMOUNT / upstream framework problem.

**Primary three-body record:** `2026-09-10_STUDYING_THE_THREE_BODY_PROBLEM_WITH_ARK.md`  
**Constitutive formalization:** `2026-09-10_MATTER_SUBSTRATE_FORWARD_COUPLING_FORMALIZATION.md`  
**Mechanical core / Maxwell–Faraday lineage:** `2026-09-10_ARK_MECHANICAL_CORE_MAXWELL_FARADAY_AND_RATE_EMERGENCE.md`

The three-body study exposed a framework-level requirement that sits upstream of inertia, gravity, rigid-body motion, galaxy dynamics, and other forward modeling: ARK does not yet uniquely specify how arbitrary moving structured matter sources and updates the full substrate state.

The subsequent mechanical-core audit identified a potentially important historical structure: an earlier Maxwell–Faraday solenoid bridge used `A_phi ∝ k^c theta^c` together with an energy bridge `u ∝ 1/2 k^c(theta^c)^2`, while the currently archived Paper XXII uses a different squared-product energy bridge. The earlier form is algebraically self-consistent and is independently echoed by the deformation-energy term in Paper XXIV H.10; the later Paper XXII bridge/inversion pair does not close as presently rendered. This lineage must be resolved before selecting a canonical action or forward equation.

Immediate sequence:

1. Recover and audit the Maxwell–Faraday / energy-bridge lineage: earlier `1/2 k^c(theta^c)^2` versus Paper XXII `1/2(k^c theta^c)^2`, including the geometry-factor insertion and inversion algebra.
2. Build a dimensions/normalization table for `theta^c`, `tau^c`, `k^c`, `dS_t`, `omega`, and the historical EM bridges.
3. Audit Paper XXIV H.10 and determine whether `tau^c` can legitimately supply the persistence/inertial coefficient in a common action without choosing its normalization from a target rate.
4. Reconcile the historical gravity-map lineage: `(theta^c)^2 = 2|Phi|/c^2` versus `Phi = theta^c c^2`.
5. Derive the matter–substrate constitutive law from prior constraints and a common energy/momentum ledger rather than three-body residuals.
6. Treat sustained rates, especially `omega`, as derived outputs wherever the frozen mechanics can determine them; do not use adaptive rate terms as convergence controls.
7. State how position, velocity, acceleration history, shape, orientation, and matter distribution initialize and update the surviving ARK state.
8. Build the one-body acceleration / uniform-motion-null benchmark before orbital modeling.
9. Build a sealed forward benchmark harness with a separate conventional gravitational integrator as calibration surface.
10. Validate progressively: one-body motion → rigid/fluid internal response → two-body controls → periodic three-body controls → symmetric/hierarchical triples → rigid-body/asymmetry calibration → close-encounter and chaotic systems.
11. Preserve the Newtonian-equivalent `theta^c` figure-eight result as a control only, not a novel ARK prediction.
12. Search for a discriminating ARK residual only after the coupling law is frozen.

Non-negotiable guards:

- no target-driven memory kernel or stabilizer,
- no convergence-by-design,
- no prescribed sustained dynamical rate when the rate can be derived from the state,
- no naive preferred-frame aether drag,
- no claiming ordinary rigid-body effects as substrate evidence,
- no hidden 1-D reduction of an intrinsically 3-D problem,
- no silent reconciliation of historically inconsistent bridge equations,
- and no claim of a three-body “solution” unless the full causal model is independently specified.

The goal is not to obtain a prettier orbit. The goal is to determine whether one constrained matter–substrate law can make the established gravitational/inertial behavior fall out while retaining a coherent larger causal state.

## Priority 1 — adversarial reproduction of one legacy precision claim

**Target:** hydrogen 1S–2S or another historically strong ARK precision claim with recoverable inputs.

Protocol:

1. Define the exact observable.
2. Inventory every ARK input and classify provenance.
3. Build an independent conventional/QED baseline separately.
4. Freeze the ARK procedure before target comparison.
5. Give at least one agent the derivation without the expected answer.
6. Audit circularity, hidden calibrations, unit conversions, imposed conditions, and numerical regularization.
7. State the physical precision ceiling implied by missing state information.
8. Preserve failed derivations.
9. Classify the final outcome: independently reproduced / assumption-dependent / compatible but underdetermined / conventional dependence / hidden freedom / contradicted / not reproducible.

A negative result counts as success if it tells us where the old claim boundary really was.

## Priority 2 — legacy claim triage

Start with XV–XXVI rather than rewriting prose immediately.

For each major claim record:

- original wording,
- current status label,
- evidence/artifact home,
- assumptions,
- external theory dependence,
- reproduction state,
- known failure modes,
- next discriminating test.

Promote durable items into the shared `CLAIM_LEDGER.md` rather than keeping separate Curie-only facts.

## Priority 3 — galaxy residual discrimination

Do not optimize RMS first.

Questions:

- Which residual structures are predicted by known 1-D information loss?
- Which survive when geometry/boundaries improve?
- Can projection loss be distinguished from a genuine outside/phase influence?
- Why does `div_partition` collapse toward the constant 1/2 behavior?
- What observables would distinguish an ARK mechanism from generic monotone radial corrections?

Best next dataset direction: 2-D/3-D baryonic geometry and, ideally, resolved velocity fields.

## Priority 4 — measurement perturbation thesis

Formalize only after specifying a falsifiable consequence. Avoid introducing an unobserved `dS_t` contribution merely because a discrepancy exists.

Needed before promotion:

- operational definition,
- sign/magnitude constraints independent of the discrepancy being explained,
- experiment where changing measurement procedure predicts a directional change,
- null condition where no change is predicted.

## Priority 5 — condition-indexed constants thesis

Test whether a supposedly intrinsic quantity varies systematically with declared conditions while its relational behavior remains portable.

Requirements:

- conditions declared before fitting,
- multiple independent systems,
- comparison against ordinary systematic-error explanations,
- no post-hoc condition variable introduced solely to repair a miss.

The 2026-09-10 mechanical-core formalization adds a stricter working principle for dynamical quantities: effective constants and sustained rates should be treated as properties of sustained regimes wherever the underlying mechanics can derive them, rather than inserted as free instructions.

## Gate before major new paper

Prefer completing at least one clean adversarial legacy reproduction before treating a new framework-confirming result as paper-grade. Exploration can continue freely; promotion should wait for the stronger protocol.
