# BRANCH_MAP

**Dated:** 2026-09-10  
**Source:** `list_branches` + `get_file_contents` on each tip.  
**Confirmed branches (6):** `ARK-GAL-1D-9.4`, `Papers`, `galaxy-1d`, `galaxy-modeling`, `main`, `workspace/gwok`.

## Summary table

| Branch | Purpose | Parentage (from charters / commits) | What’s on tip |
|--------|---------|--------------------------------------|---------------|
| `main` | Paper dump / messy office | Default / public tip | Mid–late PDFs (XII–XIV, XVII, XV–XXVI…), Complete volumes, misc notes, old I–VII-framed README |
| `workspace/gwok` | Office setup + Gwok notes home | Cut from `main`-like tip; charter README rewritten 2026-09-10 | Same paper dump as `main` at creation + **workspace charter README** + **`notes/`** (this area) |
| `galaxy-modeling` | Galaxy / SPARC modeling parent | Branched off `main` | Inherited theory PDFs + `1d/` drop zone + galaxy charter README |
| `galaxy-1d` | 1D kinematics→output pipeline charter | Offshoot of `galaxy-modeling` | Inherited theory PDFs + 1D charter README (no v9.4 run package) |
| `ARK-GAL-1D-9.4` | v9.4 SPARC modeling artifacts | Offshoot of `galaxy-1d` | Inherited theory PDFs **plus** v9.4 script/logs/CSVs/PNGs/summaries |
| `Papers` | Early paper set ~00–10 | Older line (May 2025 uploads) | `00`–`10` early papers, Complete volume, LICENSE, dual README / `READ ME.md` |

## Lineage (galaxy)

```text
main
 └── galaxy-modeling
      └── galaxy-1d
           └── ARK-GAL-1D-9.4   (v9.4)
                └── (expected) ARK-GAL-1D-9.5  — not present yet
```

Sibling office line: `workspace/gwok`. Early corpus: `Papers`.

## Per-branch detail

### `main`
- **Role:** Holding dump for theory PDFs and misc files.
- **Notable:** Includes **XXV** (containment) and **XXVI** (cognition under entropy).
- **README:** Still describes early Papers I–VII / Zenodo framing — stale vs current tip contents.

### `workspace/gwok`
- **Role:** Collaborative office; indexes and notes without treating `main` as sacred forever.
- **Ground rule:** No deletes without explicit OK; structure proposed here first.
- **Intended layout (not done):** `papers/`, `notes/`, `modeling/`, `index/`.
- **This notes area:** `notes/` (created 2026-09-10).

### `galaxy-modeling`
- **Role:** Dedicated galaxy modeling home; zero-knob methodology.
- **Extra vs main:** `1d/README.md` drop-zone stub pointing at `galaxy-1d`.

### `galaxy-1d`
- **Role:** Parameter-free 1D SPARC pipeline charter; residual discipline.
- **Version policy:** New versions → named offshoots (e.g. `ARK-GAL-1D-9.5`), not nested under existing refs.

### `ARK-GAL-1D-9.4`
- **Role:** Versioned v9.4 run package.
- **Modeling files:** `ark_v94_scalar_geom.txt`, `ark_v94_scalar_geom_stdout.txt`, `v94_summary.txt`, `model_comparison.csv`, six `*_galaxy_info.csv` + six `*_scatter.png`.
- **Note:** Root still carries inherited theory PDFs; they are not the branch purpose.

### `Papers`
- **Role:** Early ~00–10 set (and Complete volume).
- **Surprise:** Paper `10` is `.docx` (PDF was deleted historically per commits); both `README.md` and `READ ME.md` exist.

## Tip SHAs (as of survey)

| Branch | SHA (short) |
|--------|-------------|
| `ARK-GAL-1D-9.4` | `f0b462d` |
| `Papers` | `d2d43e5` |
| `galaxy-1d` | `cf6e55d` |
| `galaxy-modeling` | `c04a78c` |
| `main` | `f248f28` |
| `workspace/gwok` | advances with notes commits |
