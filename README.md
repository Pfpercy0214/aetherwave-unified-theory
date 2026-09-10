# galaxy-modeling

**Dedicated line for galaxy / SPARC modeling work** (Paul + Gwok).

Branched off `main` so this highly specific empirical work stays separate from the broader Aetherwave / ARK paper corpus.

## Purpose

- Hold solvers, inputs, outputs, notes, and write-ups for galaxy rotation / phase-regime modeling
- Keep parameter-free (zero-knob) methodology visible — residuals stay honest, not buried in tuning
- Parent home for dimensional variants (see **1D offshoot** below)

## Relationship to other branches

| Branch | Role |
|--------|------|
| `main` | Paper / theory dump (messy office) |
| `workspace/gwok` | General office-setup / corpus organization |
| **`galaxy-modeling`** | Galaxy modeling home |
| `galaxy-1d` | 1D kinematics → output offshoot (SPARC-focused) |

## Ground rules

1. **No deletes without Paul’s explicit OK.**
2. Prefer adding structure and indexes over discarding runs.
3. Separate hypotheses for residuals (e.g. 3D→1D projection loss vs external influence) — same number, different falsifiers.
4. Do not treat low RMS from knobby models as mechanical completeness.

## Layout (starting point)

```text
1d/           # 1D pipeline notes and drops (also tracked on galaxy-1d)
README.md     # this charter
```

Upload solvers, SPARC-related materials, and run notes here (or onto `galaxy-1d` for 1D-only work). Folder moves of the theory PDFs are out of scope for this branch.

---

*ARK galaxy modeling — kinematics in, predictions out; dark regimes as medium phase behavior, not bolted-on mass.*
