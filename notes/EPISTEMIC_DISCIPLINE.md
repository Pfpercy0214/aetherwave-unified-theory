# EPISTEMIC_DISCIPLINE

**Dated:** 2026-09-10

This note exists so future work does not inherit the confidence of earlier ARK/Aetherwave papers without also inheriting the lessons learned from their failures.

The earlier corpus is not being disowned. Much of it was genuine exploration and often useful. But some claims were stated more strongly than the evidence justified. The goal going forward is to preserve the useful structure while making the epistemic status of every step explicit.

## Where we went wrong

### 1. We sometimes treated an idealized calculation as though it reproduced the real experiment

Several earlier derivations were carried out under clean or effectively perfect conditions. The mathematics could be internally consistent under those imposed conditions, but the papers did not always make the imposed conditions, omitted microstates, contaminants, environmental effects, apparatus effects, or geometry explicit enough.

A precise result under an idealized model is not automatically a precise prediction of the measured system.

### 2. Numerical agreement was sometimes allowed to carry too much ontological weight

Agreement with an accepted value can show compatibility. It does not by itself establish that ARK's proposed mechanism is the mechanism nature uses.

Conventional physics and experiment should be treated as calibration surfaces and comparison targets, not answer keys from which ARK is reconstructed backward.

### 3. We did not always separate constraints, assumptions, implications, and observations

These categories must remain distinct:

- **Constraint:** something externally established that the model must respect.
- **Assumption:** something introduced to make the calculation possible but not independently established.
- **Implication:** something that follows from the framework plus declared assumptions.
- **Observation:** something measured independently of the model.

An implication must never quietly become a constraint simply because it was useful in a previous derivation.

### 4. We sometimes undercounted articulation

"Zero fitted parameters" is not the same as "zero modeling choices."

Every analysis should separately record:

1. **Fitted degrees of freedom** — quantities adjusted against the target data.
2. **External calibrations** — measured or conventionally adopted quantities inserted without fitting them in the present analysis.
3. **Structural assumptions** — geometry, boundary conditions, functional forms, dimensional reductions, normalization choices, etc.
4. **Numerical regularization** — smoothing, clipping, interpolation, extrapolation, tolerances, priors, or stabilizers.

A model may legitimately have zero fitted DoF while still containing fixed structural and numerical choices. Report both facts.

### 5. Dimensional reduction was sometimes treated as though no information had been lost

The galaxy work made this especially clear. A 1-D radial representation cannot contain all of the directional and geometric information present in a real 2-D/3-D system.

When information is removed from the representation, residual error can come from the representation itself. It must not automatically be interpreted as missing physics, nor tuned away until the fit looks attractive.

### 6. Residuals were too easy to narrate after the fact

A residual pattern is evidence that the current model is incomplete under its declared conditions. It is not evidence for a specific explanation unless competing explanations have been tested.

Every residual story should come with a falsifier or discriminating test.

### 7. Provenance was not always preserved well enough

Results such as the SPARC RMS values became difficult to reconstruct later because raw runs, later recalibrations, bridge tests, and audit results were discussed across sessions without a durable versioned ledger.

Going forward, every quoted result should be traceable to a specific branch/file/run and should state whether it is raw, calibrated, corrected, cross-validated, exploratory, or rejected.

## Operating rules going forward

### Freeze before comparison

For any claimed prediction, declare the inputs, assumptions, equations, constants, geometry, boundary conditions, and numerical procedure **before** comparing the result to the target observable whenever feasible.

Do not start from the desired answer and solve backward unless the task is explicitly labeled as an inverse problem. An inverse result is not an independent prediction.

### Separate predictor information from audit information

If information is intentionally sealed from the predictor and used only afterward for evaluation, state that clearly. Likewise, do not describe an entire experiment as "velocity-only" if only the predictor is velocity-only while the scoring target contains photometric or baryonic information.

### Count every kind of freedom

For each model/run, report fitted DoF, external calibrations, structural assumptions, and numerical regularization separately.

### Carry uncertainty honestly

If the physical state is incompletely specified, the claimed precision must reflect that. Do not report more physical precision than the known inputs and representation can support merely because the arithmetic returns many digits.

### Treat conventional theory as a calibration surface

ARK should produce its observable from declared inputs independently where possible. Only afterward should it be compared with the conventional prediction and experiment.

Agreement means compatibility. Disagreement identifies something to investigate. Neither result, by itself, proves or disproves ontology.

### Prefer falsifiers over rescue terms

When a result fails, first ask what observation or null test would distinguish:

- incorrect mechanism,
- incorrect boundary condition,
- missing geometry,
- omitted environmental state,
- numerical artifact,
- or ordinary measurement/model uncertainty.

Do not add a discrepancy-driven correction and then continue calling the result parameter-free. A correction introduced because of the residual is a new hypothesis and must be labeled as such.

### Preserve negative results

A clean failure is useful information. Keep failed derivations, null tests, autopsies, and rejected hypotheses in the corpus with their verdicts attached.

Do not quietly remove or overwrite them when a newer route works better.

### Distinguish compatibility from identification

If several different functional forms or mechanisms produce essentially the same improvement, then the data have not identified the mechanism. Report the degeneracy rather than choosing the most appealing interpretation.

### Do not confuse procedural precision with intrinsic universality

A highly reproducible procedure can yield a highly precise number without proving that the number is a universal property of nature. Where relevant, ask whether a reported "constant" is intrinsic, condition-indexed, apparatus-dependent, environment-dependent, or simply a precise output of a particular procedure.

## Required result label

Every important numerical or conceptual result should carry a short status label such as:

- **RAW RESULT**
- **CALIBRATED RESULT**
- **CROSS-VALIDATED RESULT**
- **EXPLORATORY HYPOTHESIS**
- **COMPATIBLE BUT UNDERDETERMINED**
- **DEPENDENT ON EXTERNAL THEORY/INPUT**
- **NEGATIVE RESULT / CLOSED ROUTE**
- **REPRODUCED**
- **NOT YET REPRODUCED**

The label should travel with the number or claim when it is summarized elsewhere.

## Standard for strong claims

Before promoting a result into a paper-level claim, we should be able to answer:

1. What exactly was predicted?
2. What information entered the predictor?
3. Which inputs were measured, derived, assumed, calibrated, or fitted?
4. What geometry and boundary conditions were imposed?
5. What numerical regularization was used?
6. What information was missing from the representation?
7. What null tests were run?
8. What competing explanations survive?
9. What would falsify the proposed interpretation?
10. Can another agent reproduce the result from the recorded artifacts without being told the desired answer?

If those questions cannot yet be answered, the work can still be valuable — but its claim status must remain provisional.

## The core rule

**Correct accounting of what we know is more important than obtaining the number we hoped to see.**

A worse residual with honest assumptions is more scientifically useful than a spectacular fit whose information sources, degrees of freedom, or missing conditions are unclear.

The purpose of these rules is not to make ARK harder to explore. It is to make successful results worth believing when they survive.
