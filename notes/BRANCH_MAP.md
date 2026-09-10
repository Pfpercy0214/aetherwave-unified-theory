# BRANCH_MAP

**Dated:** 2026-09-10 (updated after Curie trio exploration)  
**Source:** `list_branches` + `get_file_contents` on tips.

## Summary table

| Branch | Purpose | Parentage | What’s on tip |
|--------|---------|-----------|---------------|
| `main` | Paper dump / messy office | Default | Mid–late PDFs; root `Maxwell–Faraday in ARK form` |
| `workspace/gwok` | Gwok notes + active work | Off main-like tip | Papers + `notes/` (WORK_QUEUE, CLAIM_LEDGER, exploration note, …) |
| **`workspace/curie`** | **Curie office** | Cut from gwok-like tip | Shared notes + **`notes/curie/`** |
| `galaxy-modeling` | Galaxy modeling parent (semantic) | Off `main` | Theory PDFs + `1d/` + charter |
| `galaxy-1d` | 1D pipeline charter | Conceptual child; **verify Git ancestry** | Charter |
| `ARK-GAL-1D-9.4` | Raw v9.4 package | Off `galaxy-1d` tip | Script/logs/CSVs/PNGs + inherited PDFs |
| `ARK-GAL-1D-5.4` | V5.4 inverse package | Version offshoot | Package + inherited PDFs (containment deferred) |
| `recovery/galaxy-artifacts` | Mid-20s audit + closed v9.5 | Workspace-like + recovery | `modeling/galaxy/recovered/` |
| `Papers` | Early ~00–10 | Older line | Early papers; **no** XXII / Maxwell root file |

## Agent offices

```text
workspace/gwok     → notes/              (shared-facing clerk + claim ledger)
workspace/curie    → notes/curie/        (skeptical auditor layer; READ-ONLY from Gwok)
```

### Curie `notes/curie/` (selected)

| File | Role |
|------|------|
| `2026-09-10_STUDYING_THE_THREE_BODY_PROBLEM_WITH_ARK.md` | Three-body stress-test |
| `2026-09-10_MATTER_SUBSTRATE_FORWARD_COUPLING_FORMALIZATION.md` | Constitutive architecture |
| `2026-09-10_ARK_MECHANICAL_CORE_MAXWELL_FARADAY_AND_RATE_EMERGENCE.md` | Mechanical core / EM lineage |
| `RESEARCH_QUEUE.md` | Priority 0 maps the trio |
| `SUBSTRATE_SCALE_BRIDGE.md` | Cross-scale parent |
| `SESSION_BOOT.md`, `HANDOFFS.md`, `EPISTEMIC_LEDGER.md`, `README.md` | Office |
| `THERMODYNAMICS_PILOT.md`, `REWRITE_ARCHITECTURE.md` | Pilots |
| `galaxy/XXVI_V5_4_LEGACY_AUDIT.md` | V5.4 provenance |
| `relations/TIME_FREQUENCY_RECIPROCITY.md` | ω / τ reciprocity ancestry |

### Gwok exploration

[`notes/2026-09-10_EXPLORATION_CURIE_TRIO_MECHANICAL_CORE_AND_RATE_EMERGENCE.md`](2026-09-10_EXPLORATION_CURIE_TRIO_MECHANICAL_CORE_AND_RATE_EMERGENCE.md) — clerk cross-check of the trio against repo artifacts (Curie files untouched).

## Lineage (galaxy — semantic)

```text
main
 └── galaxy-modeling
      └── galaxy-1d
           └── ARK-GAL-1D-9.4

recovery/galaxy-artifacts
```

## Notes

- Do not treat branch diagrams as literal Git history without merge-base check.
- Promote durable facts into shared notes on `workspace/gwok`; never silently edit Curie’s private layer.
