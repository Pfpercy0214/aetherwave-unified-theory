# WORK_QUEUE — prioritized work list

**Dated:** 2026-09-10  
**Owner:** Paul + Gwok (clerk) / Curie (auditor)  
**Rulebook:** [`EPISTEMIC_DISCIPLINE.md`](EPISTEMIC_DISCIPLINE.md)  
**Claim labels:** [`CLAIM_LEDGER.md`](CLAIM_LEDGER.md)

Paul’s call (2026-09-10): **three-body / full mechanics at the top** — upstream accuracy driver for 2D–3D; regimes that look minimized in reduced descriptions may still set the error floor. Goal is to surface what is currently unaccounted for, **not** to announce that ARK solved the three-body problem.

Curie parallel records (`workspace/curie` → `notes/curie/`):

- `2026-09-10_STUDYING_THE_THREE_BODY_PROBLEM_WITH_ARK.md` — stress-test / program framing
- `2026-09-10_MATTER_SUBSTRATE_FORWARD_COUPLING_FORMALIZATION.md` — **candidate constitutive architecture** (1.0B)
- `RESEARCH_QUEUE.md` — Priority 0 aligned

---

## 1 — Three-body / full matter–substrate mechanics *(TOP)*

**Status:** HIGH-PRIORITY EXPLORATORY / PARAMOUNT framework stress-test  
**Why first:** Shared-substrate multi-source dynamics, geometry/asymmetry, memory, conservation, and chaos meet here — needed before leaning harder on multi-D modeling success.

| # | Task | Notes |
|---|------|-------|
| 1.0A | **Reconcile gravity-map lineage** | `(θᶜ)² = 2\|Φ\|/c²` (later / galaxy) vs `Φ := θᶜ c²` (XXIV). Lineage audit before any paper-grade three-body claim. |
| 1.0B | **Derive matter–substrate constitutive bridge** | Primary formalization: Curie `…_MATTER_SUBSTRATE_FORWARD_COUPLING_FORMALIZATION.md`. Architecture only: `E_ARK = C_matter = C_static + C_reactive + C_dissipative`; uniform-motion null; momentum reciprocity; **no coefficients yet**. Freeze **outside** three-body residuals. First bench: one accelerated extended body. |
| 1.0C | **Sealed forward benchmark harness** | Separate conventional integrator as calibration surface; ARK never receives future trajectory. |
| 1.0D | **Validation ladder** | Uniform translation → one-body acceleration → rigid/raw internal → two-body gravity → figure-eight → hierarchical triples → close encounter / chaos. |
| 1.0E | **Discriminating observable** | Only after coupling law is frozen; sign/scale derived first. |

**Organizing principle (Curie):** substrate responds to **reconfiguration** of the coupled state, not mere motion.

**Guards:** reactive ≠ dissipative; no target-driven memory/stabilizer; preserve chaos; no naive aether drag; rigid-body flip is calibration not substrate evidence; figure-eight = control not novel prediction; no new fluid fundamentals until forced by the five scalars.

**Anchors:** both Curie 2026-09-10 notes above; `ARK_Three_Body_First_Principles_Note.pdf` (provenance); XVIII / XXIV / XXVI lineage; `notes/curie/SUBSTRATE_SCALE_BRIDGE.md`.

---

## 2 — Gravity / inertia constitutive continuity

Same law as §1 must recover weak-field gravity **and** effective inertia (including intermediate-axis / Dzhanibekov as macroscopic limit), with momentum/energy bookkeeping between matter and field. Do not invent a separate “orbital aether.” Action/conservation-first route preferred once 1.0A is reconciled.

---

## 3 — Adversarial legacy reproduction *(Curie Priority 1)*

One clean precision claim (e.g. H 1S–2S) under blind/adversarial protocol. Negative result that maps the real claim boundary counts as success. Prefer before promoting new framework-confirming paper-grade results.

---

## 4 — Legacy claim triage (XV–XXVI)

For each major claim: wording → status label → evidence home → assumptions → external dependence → reproduction state → next falsifier. Promote durable items into [`CLAIM_LEDGER.md`](CLAIM_LEDGER.md).

**Includes:** Paper XX reframing (shared-environment congruency rescue — labeled, not lab perfection).

---

## 5 — Galaxy residual discrimination → multi-D

Do **not** chase RMS first. Discriminate projection/geometry loss vs outside/phase influence; explain `div_partition` ≈ `const_1_2`; move toward 2D/3D baryonic geometry / resolved velocity fields **after** §1 constitutive picture is less underdetermined.

**Labeled homes (do not collapse):** raw V9.4 ~30.55 (`ARK-GAL-1D-9.4`); mid-20s Y-recal / guarded (`recovery/galaxy-artifacts`); V9.5 CLOSED; V5.4 NEGATIVE/CLOSED-for-intent (Zenodo README pending; no rerun).

---

## 6 — Measurement-perturbation thesis (`dSₜ` of observation)

Formalize only with independent sign/magnitude constraints and a directional experiment/null — not as a free discrepancy knob.

---

## 7 — Condition-indexed constants thesis

“Most intrinsic constants are condition-indexed; behavior portable.” Declare conditions before fitting; multi-system; compete against ordinary systematics. Not yet a paper page.

---

## 8 — Office / corpus hygiene *(clerk track)*

| Item | Status |
|------|--------|
| Keep [`CLAIM_LEDGER.md`](CLAIM_LEDGER.md) current when numbers are quoted | Ongoing |
| Verify galaxy branch **Git** ancestry vs semantic diagram | Open |
| V5.4 folder containment (`modeling/galaxy/v5.4/`) | Deferred (needs Contents-write PAT) |
| V5.4 Zenodo result README → lock provisional ~34 / ~30% | Waiting on Paul |
| Optional: same containment tidy for V9.4 package | Later |
| `main` README still old I–VII/Zenodo framing | Later promotion |

---

## How to use

1. Pick from the top unless Paul reorders.
2. Carry status labels from the claim ledger with every number.
3. Curie owns adversarial audit / skeptical ledger; Gwok owns indexing, branch maps, and keeping this queue honest.
4. Exploration can run parallel; **promotion** waits on frozen procedures and discriminating tests.
