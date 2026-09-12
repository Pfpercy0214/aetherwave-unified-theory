# XXV_SYMBOL_FREEZE — temporary audit names (Thrust 1)

**Status:** DRAFT FREEZE TABLE / AUDIT SCAFFOLD — NOT CANONICAL LAW  
**Dated:** 2026-09-12  
**Source paper:** XXV Disciplined Containment in a Scalar Medium (2026-01-28), esp. App A  
**Historical ω audit (cite-only):** Curie `2026-09-10_ARK_RECURRENCE_TIME_FREQUENCY_IDENTITY_CLOSURE_AUDIT.md`  
**Parent plan:** [`2026-09-12_POST_XXV_RESEARCH_THRUST_ORDER.md`](2026-09-12_POST_XXV_RESEARCH_THRUST_ORDER.md)  
**Rule:** Do not use one symbol for two roles without an explicit bridge row.

---

## One-page rule: XXV ω ≠ recurrence ω

| Audit name | Meaning | Sign / range | Dimensional status |
|------------|---------|--------------|--------------------|
| `B_ω` | XXV `ω = P_int − P_ext` — signed **pressure-balance residual** | signed; ≈0 at stable identity | Same family as pressures: `P_int ∝ (θᶜ)² κᶜ`, `P_ext ∝ ΔSₜ` — **SI not frozen** (XXV App A is operational, not unit-closed) |
| `f_rec` / `ω_rec` | Nonnegative **solved recurrence** of a declared bounded identity | `f_rec ≥ 0`; `ω_rec = 2π f_rec` | Frequency / angular frequency (Hz / rad·s⁻¹) |
| `Ω_evo` | Exploratory **signed evolution / rate-tilt** marker | signed | Rate-like over a declared state coordinate — **not** identified with `B_ω` or `f_rec` without a bridge |

**Non-identification:** `B_ω ≠ ω_rec ≠ Ω_evo` unless a derived bridge earns the identification.  
Paul’s balance-flip picture and the PRX 2026 rate-tilt read attach to `B_ω` / `Ω_evo`, **not** to resonator `f_rec`.

---

## Identity-side scalars (XXV App A)

| Symbol | XXV operational role | Dim / equivalence notes (App A) | Temporary audit flags |
|--------|----------------------|----------------------------------|------------------------|
| `θᶜ` | Causal geometry / outward expression | App A: `arccos(Δτ/Δt)`; weak-field `≈√(2GM/c²r)`; also `≡\|∇Φᶜ\|/c²` — **three routes claimed equivalent**; treat as **dimensionally open until one route is chosen per claim** | Gravity-map fork still open |
| `κᶜ` / `kᶜ` | Resistance to reconfiguration (stiffness) | App A: ∝ `E_eff`, ∝ `ρ/ρ_ref`, ∝ `1/ℓ_ph` — **cross-route consistency required**; notation `κ`/`k` varies across papers | Do not free-tune |
| `τᶜ` | Boundary memory / persistence | App A: `∫_∂Ω σᶜ · dA` — tension-memory-like; **may also appear action-like elsewhere** | Do **not** assume `M_θᶜ = τᶜ` |
| `B_ω` | Audit name for XXV `ω` | See one-page rule | Does **not** propagate as an independent wave |

---

## Environment / bookkeeping

| Symbol | Role | Notes |
|--------|------|-------|
| `ΔSₜ` | Unresolved external causality (contained entropy) | External to identity; not a free fit knob |
| `ε_created` | Apparatus-injected contribution to ΔSₜ | Measurement channel |
| `ΔΠ` | Imbalance driving response rates (`Π_ext − Π_int`) | Rates emerge only under imbalance (XXV) |

---

## Historical `ω` overload (must stay decomposed)

Cite Curie RECURRENCE §3 — **do not merge**:

| Paper | Historical use of `ω` | Map to |
|-------|----------------------|--------|
| XV | Target-sensitive reciprocal / adaptive control (`1/i_obs`, update under `ΔSₜ`) | **Control artifact** — not a portable law object |
| XVI | Recursive/angular rate (`2π/τ_r` or `dθᶜ/dt`); `ω ≠ f` | Rate lineage — audit before reuse |
| XVIII | Geometric `1/cos(θᶜ)` **and** `T=2π/ω` clocking — **dimensional collision** | Split or reject dual use |
| XXIV | `∂θᶜ/∂τᶜ` update rate **and** standing-wave eigenfrequencies | Split: update vs `ω_rec` |
| XXV | `P_int − P_ext` signed balance | → **`B_ω`** |

Standing-wave / quartz recurrence → **`f_rec` / `ω_rec`**.  
Signed arrow / balance-flip → **`Ω_evo`** and/or **`B_ω`**, never silently `f_rec`.

---

## Energy / load ancestry (do not merge casually)

| Form | Where | Status |
|------|-------|--------|
| `½ κᶜ \|∇θᶜ\|²` (+ U) | XXV App E | Gradient storage |
| `½ kᶜ (θᶜ)²` | Maxwell–Faraday root; XXIV H.10 | Local deformation-like; earlier EM bridge |
| `Lᶜ := kᶜ θᶜ` | Curie mechanical-core shorthand | Load conjugate at fixed k — not a new fundamental |
| `½ (κθ)²` | Archived XXII | **Algebraic non-closure** with printed inversions |

---

## Identity boundary bookkeeping

For every claim, declare:

```text
Ω_I   = identity region / body under consideration
∂Ω_I  = interface where ΔSₜ / coupling / measurement act
```

Quartz Layer-0 used a reduced coordinate `u(z,t)` inside a 3-D identity — valid as reduction, not as “identity is 1-D.”

---

## Work-queue tagging (allowed symbols)

| Task | May use | Must not conflate |
|------|---------|-------------------|
| Gravity-map audit | `θᶜ`, Φ maps, `κᶜ` | Recurrence `ω_rec` |
| Quartz / rate-emergence | `f_rec`, `G_eff`, `ρ`, geometry | `B_ω` as frequency |
| Signed-ω / PRX read | `B_ω`, `Ω_evo`, `ΔΠ` | Resonator `f_rec` |
| Constitutive bridge | full identity set + `ΔSₜ` | Trajectory-fitted knobs |
| Three-body ladder | frozen law only | Adaptive XV-style `ω` |

---

## Open before promotion

1. **SI / unit closure** for App A routes (especially κᶜ cross-domain and τᶜ tension vs action).  
2. Which Φ↔θ map is live for each claim (`√(2Φ/c²)` family vs `Φ:=θc²`).  
3. Bridge, if any, from `B_ω` dynamics to `Ω_evo` / apparent arrow reversal.  
4. Reconcile `½κ\|∇θ\|²` vs `½kθ²` without double-counting.  
5. Do **not** promote XXV’s five-scalar list as already dimensionally invariant.
