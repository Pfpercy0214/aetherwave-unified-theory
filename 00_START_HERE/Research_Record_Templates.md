# ARK Research Record Templates

Version 1.1 - 3 October 2026. Extracted from Appendix B of the full charter.

These templates are proposed operational extensions. Replace every placeholder with a concrete entry or an explicit “unknown / not applicable.” An empty field must not be interpreted as a passed check.

### B1. Claim record

```text
Claim ID and version:
Exact proposition:
System, scale, and domain:
Claim type:
Evaluation status:
Origin and source location:
Definitions and units version:
Essential assumptions:
Input-to-output dependency chain:
Inputs and calibration sources:
Target and prior exposure:
Evidence or run artifacts:
Strongest alternative explanation:
Failed or passed discriminators:
Uncertainty and unresolved dependence:
What would change the verdict:
Downstream claims affected:
Owner, date, and next action:
```

### B2. Pre-run specification

```text
Run ID / candidate ID / code version:
Question and inference direction:
Exploratory or confirmation mode:
Equations and observable mapping:
System boundary and layer manifest:
Units, normalizations, reference state:
Required inputs and provenance:
Sealed targets and data-access roles:
Global calibrations and training sample:
Per-object parameters, if any:
Other consequential choices:
Boundary and initial conditions:
Numerical method and tolerances:
Missing-input handling:
Known-valid and deliberately wrong controls:
Nulls, baselines, and expected behavior:
Primary metric, uncertainty, and failure criteria:
Split unit, random seed, and prior exposure:
Planned secondary analyses:
Execution environment and artifact locations:
Freeze timestamp and content hash:
```

### B3. Negative-result or downgrade record

```text
Original claim and frozen candidate:
Why it initially looked promising:
Test that challenged it:
Observed failure and uncertainty:
Implementation / evaluator checks:
Diagnostic trace or counterexample:
Smallest claim rejected:
Statements that still survive:
Alternatives not yet excluded:
Any wording in the old record now too strong:
Permitted conditions for reopening:
Artifacts and affected dependencies:
Date and reviewers:
```

### B4. Epistemic drift entry

```text
Symbol, value, or claim:
Original definition and provenance:
Later use:
What changed: notation / units / meaning / evidence class:
Was the change explicit at the time?
Consequences for equations and comparisons:
Current ruling or unresolved alternatives:
Required bridge or test:
References to original and corrected versions:
```

### B5. Session handoff

```text
Question and model version used:
Files actually read:
Calculations actually executed:
New results and exact artifacts:
Failures, exclusions, and surprises:
Current claim statuses:
Assumptions changed and why:
New target exposure or contamination:
Unresolved terminology or measurement gaps:
Closed routes that must not be silently revived:
Next discriminating action:
```

### B6. Measured-input and cross-domain transfer record

```text
Candidate, version, and inference direction:
Quantity being predicted and its independent comparison path:
Measured / derived / calibrated inputs and provenance:
Operational scalar definitions, units, and reference conditions:
Which observations calibrated which quantities:
Prior exposure to target outcomes and design effects:
Full input -> state -> output dependency chain:
Coupled constraints, rank / identifiability, admissible branches:
Branch-selection rule and independent justification:
Any target-equivalent encoding actually imported:
Shared uncertainties and covariance treatment:
Could the target disagree while inputs and choices remain fixed?
Definition, reconstruction, calibration, or conditional prediction:
Source domain and held-out domain / regime:
What is shared: form / physical meanings / numerical parameters:
System-specific measured inputs versus answer-selecting choices:
Comparator and equivalent information access:
Primary metric, tolerances, coverage, and failure criteria:
Structural contribution demonstrated independently of ontology:
Mechanism-specific discriminating consequence still needed:
Result, limitations, and next test:
```

### B7. ASRP intervention record

```text
Trigger: ambiguity / unexpected agreement / failure / narrative pressure:
Specific risk identified:
Corrective check chosen and why:
Artifacts or calculations actually inspected:
What changed in the claim or next action:
What remains unknown:
```

These fields request an audit trail, not private internal chain-of-thought.

