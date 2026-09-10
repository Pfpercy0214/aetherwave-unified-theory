# BRANCH_MAP

**Dated:** 2026-09-10 (updated for `recovery/galaxy-artifacts`)  
**Source:** `list_branches` + `get_file_contents` on tips.

## Summary table

| Branch | Purpose | Parentage | What’s on tip |
|--------|---------|-----------|---------------|
| `main` | Paper dump / messy office | Default | Mid–late PDFs (XII–XIV, XVII, XV–XXVI…), Complete volumes, misc notes, old I–VII README |
| `workspace/gwok` | Office setup + Gwok working memory | Off `main`-like tip | Papers + charter + `notes/` |
| `galaxy-modeling` | Galaxy modeling parent | Off `main` | Theory PDFs + `1d/` + charter |
| `galaxy-1d` | 1D pipeline charter | Off `galaxy-modeling` | Charter (no run package) |
| `ARK-GAL-1D-9.4` | Raw v9.4 SPARC projector package | Off `galaxy-1d` | Script/logs/CSVs/PNGs + inherited PDFs |
| **`recovery/galaxy-artifacts`** | **Recovered mid-20s audit + v9.5 negative result** | Built from workspace-like tip + Curie/Paul recovery | `modeling/galaxy/recovered/{v9.4-audit-mid20s,v9.5-negative-result}/` + notes/ |
| `Papers` | Early ~00–10 set | Older line | Early papers, Complete volume, dual README |

## Lineage

```text
main
 └── galaxy-modeling
      └── galaxy-1d
           └── ARK-GAL-1D-9.4     # raw ~30.55 km/s mixed_slope

workspace/gwok                   # office + notes
recovery/galaxy-artifacts        # provenance for later analysis (not a separate GitHub repo)
  modeling/galaxy/recovered/
    v9.4-audit-mid20s/           # ~24.36 Y-recal; ~23.6 guarded/Stowe-style
    v9.5-negative-result/        # CLOSED negative (viscosity-shape artifact)
```

## Per-branch notes

### `recovery/galaxy-artifacts`
- **Not a separate repository** — branch on `aetherwave-unified-theory`.
- Restores session artifacts **without modifying** raw `ARK-GAL-1D-9.4`.
- Latest commits (2026-09-10): recovery notes, V9.4 audit lineage index, V9.5 negative-result folder, “Finalize exact V9.5 source and negative-result recovery.”
- Two referenced outputs missing from Library (not invented): `stowe_v95_guard_output.txt`, `v95_autopsy_repro.txt`.

### `ARK-GAL-1D-9.4`
- Authoritative for **raw** V9.4 projector metrics only.

### `workspace/gwok`
- Working-memory `notes/` live here; keep galaxy status in sync with recovery findings.

### `Papers`
- Early 00–10 only; paper 10 is `.docx`; `README.md` + `READ ME.md`.

## Tip SHAs (approx., resurvey if stale)

| Branch | Notes |
|--------|--------|
| `recovery/galaxy-artifacts` | tip includes finalize commit `7437edf` |
| `ARK-GAL-1D-9.4` | raw package + charter |
| `workspace/gwok` | advances with notes commits |
| `main` | `f248f28` at last full survey |
