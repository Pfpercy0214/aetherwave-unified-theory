# BRANCH_MAP

**Dated:** 2026-09-10 (updated for `workspace/curie`)  
**Source:** `list_branches` + `get_file_contents` on tips.

## Summary table

| Branch | Purpose | Parentage | What’s on tip |
|--------|---------|-----------|---------------|
| `main` | Paper dump / messy office | Default | Mid–late PDFs, Complete volumes, old I–VII README |
| `workspace/gwok` | Gwok notes + active work | Off main-like tip | Papers + `notes/` (ACTIVE_WORK, CLAIM_LEDGER, …) |
| **`workspace/curie`** | **Curie office** | Cut from gwok-like tip | Shared notes copy + **`notes/curie/`** (her layer) |
| `galaxy-modeling` | Galaxy modeling parent (semantic) | Off `main` | Theory PDFs + `1d/` + charter |
| `galaxy-1d` | 1D pipeline charter (semantic offshoot) | Conceptual child of galaxy-modeling; **verify Git ancestry before rebase** | Charter |
| `ARK-GAL-1D-9.4` | Raw v9.4 package | Off `galaxy-1d` tip | Script/logs/CSVs/PNGs + inherited PDFs |
| `recovery/galaxy-artifacts` | Mid-20s audit + closed v9.5 | Workspace-like + recovery | `modeling/galaxy/recovered/` |
| `Papers` | Early ~00–10 | Older line | Early papers, Complete volume |

## Agent offices

```text
workspace/gwok     → notes/              (shared-facing clerk + claim ledger)
workspace/curie    → notes/curie/        (skeptical auditor layer; points at shared notes)
```

Curie unique files: `SESSION_BOOT.md`, `EPISTEMIC_LEDGER.md`, `RESEARCH_QUEUE.md`, `HANDOFFS.md`, `README.md` under `notes/curie/`.

## Lineage (galaxy — semantic)

```text
main
 └── galaxy-modeling
      └── galaxy-1d          # conceptual; Curie flags literal ancestry may share main merge-base
           └── ARK-GAL-1D-9.4

recovery/galaxy-artifacts     # audit + negative-result provenance
```

## Notes

- Do not treat branch diagrams as literal Git history without `git log --graph` / merge-base check.
- Promote durable facts into shared notes on `workspace/gwok` (CLAIM_LEDGER, etc.), not only agent-private folders.
