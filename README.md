# galaxy-1d

**1D offshoot of `galaxy-modeling`.**

This branch is for the parameter-free **1D kinematics → output** galaxy pipeline (SPARC and related), kept separate because the method and residual story are specific.

## Why 1D has its own line

- Collapse from 3D → 1D throws away structure; that loss shows up in residuals (not in tuning knobs)
- Zero articulation: take kinematics / data in, emit results — no free parameters to absorb “dark” phenomenology or projection loss
- Typical SPARC RMS in recent work ~23–25; residual attribution is an open, disciplined question (mostly projection loss, some external influence)

## Parent / siblings

- Parent conceptual home: [`galaxy-modeling`](https://github.com/Pfpercy0214/aetherwave-unified-theory/tree/galaxy-modeling)
- Folder drop on parent: `1d/` on that branch
- Theory corpus / office setup: `main`, `workspace/gwok`

## Ground rules

1. **No deletes without Paul’s explicit OK.**
2. Keep knobs out of the core method — if something is tuned, label it as calibration or experiment, not silent fit.
3. When discussing residuals, keep **projection loss** and **outside influence** as separate hypotheses with different falsifiers.
4. MOND-style low residuals are not treated as proof of mechanical completeness when knobs can absorb lost 3D structure.

## Drop zone

Upload solvers, run scripts, SPARC inputs/outputs, RMS tables, and notes here. A fuller folder layout can grow once the first materials land.

---

*1D ARK galaxy modeling — honest residuals over pretty knobs.*
