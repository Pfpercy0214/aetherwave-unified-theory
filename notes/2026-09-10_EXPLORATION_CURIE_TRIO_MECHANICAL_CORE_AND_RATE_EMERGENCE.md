# 2026-09-10 Exploration — Curie trio vs repository (Gwok)

**Status:** CLERK EXPLORATION MAP / NOT A NEW LAW  
**Dated:** 2026-09-10  
**Branch:** `workspace/gwok`  
**Rule:** Cite Curie notes read-only — **do not edit** `notes/curie/*`.

This note records an independent repo sweep against Curie’s three 2026-09-10 research notes. Method: direct file/PDF fetch + text extract (GitHub `search_code` returned empty for this private repo; path-known reads used instead).

---

## 1. The trio (roles)

| Curie path (`workspace/curie`) | Role |
|--------------------------------|------|
| `notes/curie/2026-09-10_STUDYING_THE_THREE_BODY_PROBLEM_WITH_ARK.md` | Stress-test / program framing; gravity-map open issue; control ≠ prediction |
| `notes/curie/2026-09-10_MATTER_SUBSTRATE_FORWARD_COUPLING_FORMALIZATION.md` | Candidate constitutive architecture `E_ARK = C_static + C_reactive + C_dissipative` |
| `notes/curie/2026-09-10_ARK_MECHANICAL_CORE_MAXWELL_FARADAY_AND_RATE_EMERGENCE.md` | Mechanical core; EM bridge lineage; Rate-Emergence; Condition-Sustained Constancy |

**Causal stack (as Curie frames it):**

```text
SUBSTRATE_SCALE_BRIDGE (cross-scale hypothesis)
        ↓
matter–substrate constitutive architecture (C_matter)
        ↓
mechanical core / energy / Lᶜ / EM lineage audit
        ↓
one-body acceleration + no-drag benchmark
        ↓
three-body as integration test (not the place laws are invented)
```

---

## 2. Verdict matrix (repo vs Curie)

| Claim | Repo fact | Verdict |
|-------|-----------|---------|
| Earlier solenoid bridges close; separate `k` and `θ` | Root file `Maxwell–Faraday in ARK form` on `main` / `workspace/gwok` / `workspace/curie` | **CONFIRMED** |
| XXII uses `½(κθ)²` + `A = ΛA G (κθ)`; inversions fail unless `G²=1`; both constrain product `X` | XXII PDF (2025-09-05), §II + §V | **CONFIRMED** (+ §V.2 omits `G` while §II/V.3 keep it) |
| XXII: `ω` emergent when causal pressures balanced | Exact author note in XXII ~p.3 | **CONFIRMED** |
| XXIV H.10 = `½ k θ² + τ (∂tθ)²`, RHS ~ `θ ω ∂tθ` | XXIV PDF H.10 | **CONFIRMED** (ancestry for earlier energy form, not XXII product) |
| Gravity map: galaxy `(θ)² = 2\|Φ\|/c²` vs XXIV `Φ := θ c²` | XXVI + V9.4 logs vs XXIV §4/H.2 | **CONFIRMED real conflict** |
| Historical PDE with `dS_t` + `Λ(θ,ω)` | XXIV, XXVI | **CONFIRMED** as historical wording |
| Three-body PDF = first-principles sketch | `ARK_Three_Body_First_Principles_Note.pdf` (2025-12-21) | **Provenance**; Curie is stricter (control / not prediction) |
| Earlier bridge “not yet identified as searchable text” (Curie mechanical-core §2.1) | File is searchable at repo root | **UPDATE Curie note:** artifact **found** — `Maxwell–Faraday in ARK form` |

---

## 3. Maxwell–Faraday lineage (load-bearing)

### 3.1 Earlier form (closes)

From `Maxwell–Faraday in ARK form`:

```text
Aφ = ΛA · kᶜ θᶜ
B²/(2μ₀) = Λu · ½ kᶜ θᶜ²

θᶜ = (ΛA/Λu) · (B²/μ₀) / Aφ
kᶜ = (Λu/ΛA²) · (Aφ² μ₀ / B²)
```

Independent powers of `θ` ⇒ unique split of `k` and `θ`. Back-substitution closes.  
**Label:** COMPATIBILITY / INVERSION STRUCTURE — not an independent derivation of Maxwell–Faraday from ARK.

### 3.2 Archived XXII form (does not close)

```text
B²/(2μ₀) = Λu · ½ (κᶜ θᶜ)²
A_comp = ΛA · G · (κᶜ θᶜ)
```

With `X := κθ`, both equations constrain only `X`. Printed inversions yield `ΛA G (κθ) = A/G²`, equal to `A` only if `G² = 1`.  
**Label:** OPEN LINEAGE / ALGEBRAIC NON-CLOSURE.

### 3.3 Cross-check with XXIV

XXIV deformation energy `u = ½ kᶜ θᶜ²` and H.10 echo the **earlier** linear-`k` form, not XXII’s squared product. Spatial operator `∇·(k ∇θ)` still suggests possible `|∇θ|²` storage — **do not merge** `θ²` and `|∇θ|²` casually (Curie §15; agree).

---

## 4. Gravity-map fork (Priority 0A)

| Source | Map | Implied `g` |
|--------|-----|-------------|
| XXIV macroscopic | `Φ := θᶜ c²` | `g = c² \|∇θᶜ\|` |
| XXVI / V9.4 galaxy | `(θᶜ)² = 2\|Φ\|/c²` | `g = c² θᶜ \|∇θᶜ\|` |

These are incompatible without a documented normalization/regime change.  
**Label:** OPEN LINEAGE / AUDIT ISSUE — freeze before action claims or three-body “predictions.”

---

## 5. Principles to keep labeled (not laws)

| Principle | Home | Label |
|-----------|------|-------|
| Reactive ≠ dissipative; uniform-motion null | Coupling formalization | CANDIDATE ARCHITECTURE |
| Substrate responds to **reconfiguration**, not mere motion | Coupling + mechanical core | ORGANIZING PRINCIPLE |
| **Condition-Sustained Constancy** — constants as solutions of sustained conditions | Mechanical core §7 | EXPLORATORY PRINCIPLE |
| **Rate-Emergence** — sustained rates from mechanics; `ω` as output not knob | Mechanical core §8; XXII author note | EXPLORATORY PRINCIPLE |
| `Lᶜ := kᶜ θᶜ` load shorthand (not a new fundamental) | Mechanical core §5 | STRUCTURAL SHORTHAND |
| `M_θᶜ` temporary persistence modulus (audit whether `= τᶜ`) | Mechanical core §11–12 | AUDIT PLACEHOLDER |

Paul’s method reminder: architecture = **constraint surface** where laws are found; arbitrary structure multiplies underdetermination. Mechanics first, then math.

---

## 6. Historical three-body PDF vs Curie

`ARK_Three_Body_First_Principles_Note.pdf` (2025-12-21): Hilbert-not-required; kᶜ saturation vs singularity; weak-field `∇²θ = λρ`, `r̈ = −C∇θ`; toy resonance protocol.

Curie 2026-09-10 note **extends and disciplines** this: Newtonian-equivalent θ map = compatibility only; figure-eight = reproduced control; constitutive bridge required before any novel claim.

---

## 7. Related Curie files (not edited)

| File | Relation |
|------|----------|
| `notes/curie/RESEARCH_QUEUE.md` | Priority 0 fully maps the trio |
| `notes/curie/SUBSTRATE_SCALE_BRIDGE.md` | Cross-scale parent hypothesis |
| `notes/curie/relations/TIME_FREQUENCY_RECIPROCITY.md` | ω / τᶜ reciprocity ancestry |
| `notes/curie/HANDOFFS.md`, `SESSION_BOOT.md` | Not yet updated to cite the trio (as of this sweep) |
| `notes/curie/galaxy/XXVI_V5_4_LEGACY_AUDIT.md` | Separate galaxy provenance |

---

## 8. Provenance anchors (paths only)

- `Maxwell–Faraday in ARK form` — earlier closing bridges  
- `XXII-Electromagnetism in Scalar Geometry.pdf` — later non-closing product bridges + emergent-ω note  
- `XXIV The Scalar Origin of Quantum Gravity.pdf` — H.10, `Φ:=θc²`, historical PDE  
- `XXVI Disciplined Cognition Under Entropy.pdf` — galaxy quadratic map + PDE  
- `ARK_Three_Body_First_Principles_Note.pdf` — historical three-body sketch  
- `ARK-GAL-1D-9.4` / `ark_v94_scalar_geom.txt` — operational `(θ)²=2\|Φ\|/c²`

---

## 9. Open audit list (exploration order)

1. Document that `Maxwell–Faraday in ARK form` **is** the searchable earlier artifact (patch Curie §2.1 via handoff, don’t edit her file from here).  
2. Git blame / history: when XXII adopted `(κθ)²` and `G`.  
3. Re-derive XXII inversions from stated bridges without using printed answers.  
4. Dimensions table: `θ, k/κ, τ, dS_t, ω, ΛA, Λu` across Maxwell note / XXII / XXIV H.10.  
5. Reconcile `½kθ²` vs `½k\|∇θ\|²` vs PDE operator.  
6. Gravity-map canonicalize / supersession note.  
7. Freeze energy/momentum ledger → matter exchange → one-body bench → three-body ladder.  
8. Optional: Paper V EM topology on `Papers` branch for earlier curl/radiation ancestry.

---

## 10. Non-claims

- No established constitutive law.  
- No independent derivation of Maxwell, inertia, or gravity from ARK.  
- No solved three-body problem.  
- No new fluid fundamentals (`ρ_a`, etc.).  
- No free drag `F = −γv`.  
- No coefficient chosen from a target trajectory.

---

## 11. Index debt (Gwok clerk)

After this note: update `WORK_QUEUE.md` (cite mechanical-core as third parallel record; add XXII / Rate-Emergence tasks), `CLAIM_LEDGER.md` (new rows), `BRANCH_MAP.md` (Curie file list), optionally `FRAMEWORK.md` / `SESSION_BOOT.md` pointers.
