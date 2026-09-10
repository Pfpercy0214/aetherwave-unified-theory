# REWRITE_ARCHITECTURE — current-theory reconstruction

**Purpose:** Define how the historical Aetherwave/ARK paper corpus should be transformed into a modern, topic-centered, auditable body of work without erasing its development history.

## Core principle

The old papers are **historical sources**, not the structure of the current theory.

Their value is provenance: they show where ideas first appeared, how terminology evolved, what assumptions were made, which patterns were noticed, and which claims later failed or changed.

The rewritten theory should therefore be organized by **current concepts, mechanisms, relations, domains, and evidence**, not by the order in which papers happened to be written.

A historical paper may feed many modern topics. A modern topic may draw from many historical papers.

## Why this is necessary

Early papers often used cross-domain comparison to expose recurring structure. That was useful for discovery, but prose frequently mixed:

- definition,
- analogy,
- proposed mechanism,
- derived equation,
- numerical estimate,
- empirical comparison,
- ontology,
- and speculation.

In the new architecture these should be separate objects that link to one another.

The cross-domain pattern should not disappear. It should become **more explicit and more testable**.

## Proposed information layers

### 0. Historical source layer

Preserve original papers, drafts, run artifacts, and notes unchanged.

Each extracted item records:

- paper/version,
- page/section,
- date if known,
- exact historical wording when needed,
- branch/path,
- current status.

Historical sources are never silently rewritten into current truth.

### 1. Concept layer

One node per concept whose meaning should remain stable across domains.

Examples:

- causal slope `theta^c`,
- tension memory `tau^c`,
- stiffness `k^c` / `kappa^c`,
- entropy / `dS_t`,
- recursive anchor `omega`,
- containment,
- perturbation,
- equilibrium,
- identity,
- boundary,
- causal pressure.

Each concept page should distinguish:

- current definition,
- historical definitions,
- mathematical role,
- physical interpretation,
- unresolved ambiguity,
- source lineage.

### 2. Relationship / invariant layer

This is the layer that preserves what the old cross-domain writing was trying to expose.

A relation gets its own node instead of being buried inside an example.

Examples of relation types:

- reciprocal/inverse relationships,
- restoring-response relationships,
- slope–tension coupling,
- stiffness-limited deformation,
- memory/hysteresis loops,
- containment vs escape,
- gradient-driven transport,
- recursive stabilization,
- boundary-conditioned response,
- phase / regime transition relationships.

Each relation page should state:

1. the relation in domain-neutral language,
2. mathematical expression if justified,
3. assumptions required,
4. domains where it appears,
5. evidence for each appearance,
6. counterexamples or failed mappings,
7. whether the relation is structural, analogical, empirical, or merely proposed.

**Critical rule:** multiple domain examples can support a relation, but no example becomes part of the relation's definition merely because it is rhetorically convenient.

### 3. Claim layer

Every scientifically meaningful claim should be atomic enough to receive its own epistemic status.

Minimum metadata:

- claim ID,
- claim text,
- status label,
- supporting sources,
- assumptions,
- external calibrations,
- fitted freedoms,
- structural choices,
- numerical regularization,
- evidence,
- null tests,
- competing explanations,
- falsifier,
- reproduction status,
- superseded-by / depends-on links.

This layer should synchronize with the shared `CLAIM_LEDGER.md` for high-value claims.

### 4. Derivation layer

Equations and derivations should live separately from explanatory prose when possible.

A derivation records:

- declared inputs,
- input provenance,
- units,
- assumptions,
- algebraic steps,
- approximation points,
- boundary/initial conditions,
- numerical method if any,
- expected observable,
- whether target information was visible before the procedure was frozen.

A derivation can support multiple domain papers without being copied and mutated independently.

### 5. Evidence / experiment layer

Keep experiments, datasets, modeling runs, calibration surfaces, null tests, and negative results here.

The evidence layer answers: **what happened when the claim touched data?**

It should not be embedded only inside explanatory theory prose.

### 6. Domain layer

Domains organize the theory for human readers without owning the underlying concepts.

Candidate domains:

- foundations / causal geometry,
- thermodynamics and nonequilibrium behavior,
- electromagnetism and radiation,
- atomic / quantum structure,
- gravitation / orbital dynamics,
- cosmology,
- matter / particle identity,
- containment / stability / phase structure,
- information / memory / cognition,
- biological organization,
- galaxy dynamics,
- experiments / engineering applications.

A domain page points to the relevant concepts, relations, claims, derivations, and evidence.

### 7. Modern synthesis / rewrite layer

Only after the underlying nodes are audited do we write modern papers or chapters.

A modern rewrite is a **view over the knowledge graph**, not a new silo.

That means a modern thermodynamics paper can use the same audited hysteresis relation as a materials paper without redefining it differently in each document.

## Proposed eventual repository shape

```text
sources/
  papers/                  # historical originals or pointers to canonical branches
  notes/

knowledge/
  concepts/
  relations/
  claims/
  derivations/
  evidence/
  history/

  domains/
    foundations/
    thermodynamics/
    electromagnetism/
    quantum-atomic/
    gravity-orbits/
    cosmology/
    matter-identity/
    containment/
    information-cognition/
    biology/
    galaxy-dynamics/

rewrites/
  thermodynamics/
  electromagnetism/
  quantum-atomic/
  ...
```

This is a proposed architecture, not yet a mass file move. Existing branches remain provenance homes until deliberately migrated.

## Rewrite workflow for any historical subject

### Pass A — extraction

Read the historical source and extract atomic items without deciding yet that they are correct:

- definitions,
- equations,
- mechanisms,
- predictions,
- analogies,
- examples,
- numerical estimates,
- assumptions,
- references.

### Pass B — classification

Classify each item as:

- survives essentially unchanged,
- survives but needs modern wording,
- useful analogy only,
- incomplete / missing conditions,
- dependent on external theory,
- needs dimensional/unit audit,
- superseded by later ARK understanding,
- unsupported speculation,
- contradicted / closed.

### Pass C — reconciliation

Compare the item against later papers, current framework notes, experiments, and negative results.

Do not force consistency. If two historical statements conflict, preserve the conflict until the mechanism is resolved.

### Pass D — independent audit

For important equations or predictions:

- dimensional check,
- conventional baseline,
- provenance check,
- target-leakage check,
- hidden-articulation count,
- sensitivity / null tests where possible.

### Pass E — synthesis

Only then write the modern subject treatment from the surviving audited pieces.

Historical material can be cited as lineage without being treated as current truth.

## Thermodynamics as the pilot case

Paper VIII is an unusually good stress test because it became much larger than a normal single paper and contains material that now belongs to several conceptual homes.

Initial decomposition should probably separate at least:

1. **Thermal state:** temperature, entropy, equilibrium, state variables.
2. **Transport:** conduction/diffusion, radiation, boundary flux.
3. **Memory and irreversibility:** hysteresis, lag, path dependence, relaxation.
4. **Nonequilibrium dynamics:** forcing, instabilities, cascades, entropy production.
5. **Phase behavior:** transitions, bifurcation, criticality, regime changes.
6. **Mechanical/material response:** shear, torsion, yield, fatigue, plasticity, failure.
7. **Wave/field behavior:** pulses, reflection, refraction, solitons, resonance, propagation.
8. **Containment/collapse:** thresholds, drainout, collapse, persistence, reseeding.

Some of these may remain thermodynamics. Some probably belong primarily to field dynamics, material response, or containment and should only be referenced from thermodynamics.

The goal is **not** to save all 93 sections. The goal is to determine what each section was trying to say, test whether that statement survives, and relocate the surviving content into the correct modern structure.

## Special caution for AI-authored legacy prose

A large amount of fluent explanatory text can create a false sense that the underlying derivation was already validated.

Where legacy sections were substantially drafted by an AI collaborator, treat fluency as **zero evidence** of correctness.

Audit equations, units, physical claims, numerical estimates, and references independently. The fact that Curie or another model wrote a section is provenance, not validation.

## Writing standard for modern rewrites

Modern papers should be smaller and narrower than the historical omnibus papers.

Prefer:

- one central question,
- a small number of declared mechanisms,
- reusable references to shared concepts/relations,
- explicit assumptions,
- current-status labels,
- a dedicated limitations section,
- links to derivations and evidence,
- historical lineage in an appendix rather than mixed into the argument.

Cross-domain examples remain valuable, but they should appear as **comparative evidence for a declared relation**, not as rhetorical proof.

## First concrete action

Use Paper VIII as the pilot extraction/audit project.

Do **not** rewrite it linearly from Section 1 to Section 93.

First build a section-to-topic map and classify each section into the modern domain/relationship structure. Then choose one coherent cluster—probably thermal state + transport + equilibrium—for the first full audit and rewrite.

If this workflow works on Paper VIII, it should scale to the rest of the corpus.
