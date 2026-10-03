# Prediction, closure, and mechanism: read before judging ARK

Version 1.1 - 3 October 2026. A practical companion to the [full charter](ARK_Epistemic_Charter.md), especially Sections 1.4, 6, 7, and 12. All numerical examples below are deliberately synthetic teaching cases. They are not observations, fits, or demonstrations that ARK describes nature.

## The principle

We investigate whether independently characterized observations can constrain other observables through the same balance and dynamical structure across domains. We do not require a model to create information from nothing. We require the claimed test to add an empirical constraint that was not imposed through its answer.

An equation's ability to run backward is not a circularity defect. A derivation's dependence on measurements is not a circularity defect. A simultaneous solution is not a circularity defect. The defect is returning supplied target information as though it were independent confirmation, or concealing choices that forced the agreement.

The complementary mistake is dismissing legitimate inference. A useful reviewer must detect both mistakes, not merely use the word 'circular' often.

## 1. Same algebra, three different evidentiary situations

**Candidate empirical relation.** Suppose independently defined, dimensionless quantities are hypothesized to satisfy `a*b = 1`. A measurement gives `a = 4.00 +/- 0.04`, where the uncertainty is one standard uncertainty. The frozen relation predicts `b = 0.2500`. A first-order propagation gives `u(b) = u(a)/a^2 = 0.0025`. A separately obtained observation, say `b = 0.251 +/- 0.003`, can test that consequence. These numbers are invented examples; no ARK measurement is claimed.

For uncorrelated uncertainties in this illustration, the uncertainty of the difference is approximately `sqrt(0.0025^2 + 0.003^2) = 0.0039`. The difference is 0.001, so these particular invented observations are compatible at that scale. This is not a universal acceptance criterion. Specify a real test's tolerance, uncertainty model, regime, and comparator before seeing its results. Shared calibration would require covariance terms. Near `a = 0`, the inverse becomes ill-conditioned and a local uncertainty approximation may be inadequate.

**Target reconstruction.** Instead set `a = 1/b_observed`, then report `b_pred = 1/a`. Every nonzero target is returned exactly. Even an intentionally wrong target is reproduced. The agreement does not test the proposed relation against that observation because that observation generated the input.

**Definition.** If `b` is defined to mean `1/a`, the equation is a convention or identity. Independent instruments can test realization of the measurement procedures, but algebraic inversion does not discover a new empirical coupling. The independently defined physical meanings matter as much as the information path.

**Required reviewer response:** identify which situation actually applies. Do not infer it from equation shape alone.

## 2. Calibration can create a useful predictor

Take `y = K*x`. A reference case `x1 = 2`, `y1 = 6` gives `K = 3`. Returning 6 in that reference case is reconstruction. Holding K fixed and using an independently measured `x2 = 5` predicts `y2 = 15`.

The second outcome can disagree. That makes it a possible transfer test, provided the second answer did not influence K, the formula, exclusions, normalization, or the choice to report this candidate. The precise description is 'calibrated on the reference case; conditionally predicts a new outcome.' It is neither 'everything derived from nothing' nor 'all later predictions are circular.'

Multiple observations may calibrate a parameter vector. Some observations of one system may determine a state from which other observables follow. Those are legitimate designs. Do not count a second number as independent evidence when it is merely a deterministic restatement of the first using the same measurement record.

Input uncertainty, calibration uncertainty, and model discrepancy remain part of the result. Repeated transfer success can support the relationship in tested regimes without erasing its calibration history or proving its mechanism unique.

## 3. Coupled closure is not an epistemic loop

Consider fixed constraints `u + v = x` and `u - v = z`, with independently characterized inputs x and z. They yield `u = (x + z)/2` and `v = (x - z)/2`. Calling these equations mutually dependent does not make the solution circular. Their solution can supply testable estimates of independently defined u and v.

But `u + v = x` alone does not determine both unknowns. Choosing one value silently supplies an extra assumption. Likewise, `u^2 = x` leaves two real roots for positive x unless independent information selects a branch. Selecting the root closest to the target uses the answer and must not be presented as an untuned prediction.

For an ARK closure, declare the state, constraints, constitutive laws, boundary conditions, admissible branches, and observable map. Establish the needed uniqueness or report a set or distribution of predictions. A solver converging to one root does not prove that root is the physically selected state.

## 4. What 'no points of articulation' should mean operationally

Once the independently specified physical situation and declared calibrations are fixed, the model should have no remaining freedom to choose its preferred answer.

Measured geometry, known material properties, independently measured forcing, and initial conditions can differ between systems. Those are not automatically fitting knobs. However, an unmeasured forcing inferred separately from each target is not an independent input merely because it has a physical name.

Audit scalar definitions, conversion factors, reference scales, normalization, closures, boundary continuation, clipping, smoothing, sample selection, output transforms, and branch selection. A fixed script can contain answer-trained decisions. A model with an honest calibrated coefficient can still outperform a supposedly parameter-free model in independent tests. State what each actually uses.

A practical counterfactual is: change the evaluation target while keeping permitted inputs and the frozen candidate unchanged. A legitimate predictor's output should not change merely because the evaluator's answer changed. This detects direct computational leakage; it does not by itself certify untainted model-design history.

## 5. Cross-domain transfer: the opportunity and the obligation

The research objective is more than assembling unrelated formulas that each reproduce a familiar number. Ask whether a common structure constrains multiple domains while retaining its operational meanings.

Specify what is being transferred: mathematical form, physically interpreted coupling, numerical parameters, or an entire input-to-output procedure. A common form is already a possible structural observation; it is not automatically a common substance. A common numerical value requires a stronger bridge than a common form.

A transfer record should identify the source domain, destination domain, independently measured system-specific inputs, unchanged definitions and equations, global calibrations, and prohibited target information. Freeze how the new domain maps measurements into scalar quantities before evaluating its targets. Hold out an entire domain or regime where feasible, and report failure as well as success.

A domain-specific normalization chosen to repair a mismatch is a revision. Independently established unit conversion is not. Geometry obtained by measurement is an input. Geometry chosen from several candidates because one fits best is model selection. These distinctions prevent both hidden flexibility and the false accusation that any change of physical conditions is tuning.

Cross-domain success may establish empirical transfer, expose constraints, or reduce independently assigned parameters before it settles ontology. Test those contributions directly. Do not demand proof of every ambition before acknowledging a narrower achievement.

## 6. Calibration surfaces are not all the same kind of evidence

Use an established equation as a compatibility benchmark, reference observations as calibration data, and independent observations as tests. State which role applies in each calculation.

Recovering a successful Standard Model consequence is a legitimate compatibility task. It does not automatically validate a distinctive ARK mechanism, especially where both use the same empirical inputs. A theoretical benchmark and the data used to calibrate it may not be independent confirmations.

Existing physics is not contamination just because it is conventional. Declare imported laws, constants, and measurement models; do not relabel them as first-principles ARK discoveries. Conversely, nonstandard vocabulary is not a reason to refuse an otherwise explicit conditional derivation.

Predictive content and historical novelty are separate. Researchers can test a fixed relation against already published observations. They should record exposure and avoid calling that a blind discovery. They should not call it circular without identifying an actual answer dependency.

## 7. When a mechanistic story adds scientific content

A mechanism should specify what changes, what couples to what, what supplies a restoring or driving response, and which observable consequences follow. Its value is not merely that the language sounds physically intuitive.

For example, `dq/dt = -lambda*(q-q_star)` and `dq/dt = +lambda*(q-q_star)` share the equilibrium q_star for positive lambda. An initial displacement decays in the first and grows in the second. Agreement at equilibrium does not decide between them. A time-resolved perturbation test can. This is a mathematical illustration, not an ARK equation or experimental result.

Other discriminators can be static relationships, response signs, thresholds, geometry effects, or independent coupling measurements. Dynamic prediction is not the only legitimate kind of test. Inverting a relationship changes the direction of inference, not necessarily the direction of physical causation.

A reformulation can be useful if it exposes common constraints, simplifies a calculation, or suggests a new experiment. Claim that contribution with supporting artifacts. Distinctive physical machinery requires consequences capable of distinguishing it from alternatives; identical predictions do not select a unique ontology.

## 8. A complete worked review

Suppose an ARK candidate uses measured A and B to infer latent state S, then predicts C through frozen closure F. Begin by obtaining the definitions and units of A, B, S, and C. Identify whether S is uniquely determined, what boundary information is supplied, and which calibrations were used. Trace the provenance of F, not merely the final function arguments.

If C was not used to construct S or select F, calculate C with uncertainty and compare it to an independent measurement. Describe it as a conditional prediction under the specified assumptions. If C supplied S, identify the reconstruction and ask whether S instead predicts another withheld observable D. If several states fit A and B, report their consequences or seek a discriminating input; do not select the state closest to C.

If F transfers to another domain without answer-driven changes, record what stayed fixed and what was independently measured anew. If it fails, locate the smallest failed proposition. A failure may implicate F, the mapping, an approximation, a boundary, or the implementation. The next action must be supported by a specific diagnostic, not by an unlimited appeal to missing physics.

This review can end with support, rejection, or an unresolved bridge. Its quality depends on correct accounting and a useful test, not which verdict it produces.

## 9. ASRP when reasoning starts to drift

Use Aetherwave Self-Regulation Protocol as a practical loop: detect a difficulty, label the risk, anticipate the likely error, choose a corrective check, act, and record the outcome.

If agreement seems too perfect, trace input provenance. If a critic says 'circular' without a dependency, draw the dependency. If missing data invite a convenient zero, preserve the gap or bound it. If a familiar narrative becomes persuasive, ask what observable it requires. If repeated failures invite a new rescue term, freeze the failed candidate before redesigning it.

The same loop protects against overclaiming and premature dismissal. It does not require agreement with ARK, literal measurement of internal AI scalars, or disclosure of hidden reasoning. Record checkable assumptions, equations, evidence, and decisions. Admitting uncertainty is not enough when a concrete check is available; inventing certainty is never a substitute for that check.

## 10. Language that preserves the distinction

Prefer 'This is a conditional prediction from independently characterized inputs' to 'It uses measurements, so it cannot predict.' Prefer 'This target was supplied through this intermediate value' to 'It looks circular.' Prefer 'Calibrated here, tested there' to 'Calibration makes the whole model invalid.' Prefer 'This formulation has demonstrated this structural contribution' to either 'It is only a reformulation' or 'Its story proves the ontology.'

The corresponding obligations remain: disclose inputs, expose adjustments, retain uncertainty, show failure, and identify the remaining discriminating test.

## Methodological sources and scope

JCGM VIM entry 2.48 describes indirect determination through measurement models, including multiple outputs: https://jcgm.bipm.org/vim/en/2.48.html . Entry 2.3 distinguishes the intended measurand from measurement effects: https://jcgm.bipm.org/vim/en/2.3.html . NIST TN 1297 Appendix A provides first-order uncertainty propagation including covariance: https://www.nist.gov/pml/nist-technical-note-1297/nist-tn-1297-appendix-law-propagation-uncertainty . These references support the measurement distinctions, not ARK's physical claims. The examples, review procedure, and cross-domain requirements above are proposed applications and elementary derivations.
