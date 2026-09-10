# galaxy-1d

**1D offshoot of [`galaxy-modeling`](https://github.com/Pfpercy0214/aetherwave-unified-theory/tree/galaxy-modeling).**

This branch is for the parameter-free **1D kinematics → output** galaxy pipeline (SPARC and related), kept separate because the method and residual story are specific.

## Version offshoots

| Branch | What it is |
|--------|------------|
| [`ARK-GAL-1D-9.4`](https://github.com/Pfpercy0214/aetherwave-unified-theory/tree/ARK-GAL-1D-9.4) | **v9.4** projector runs, CSVs, scatter plots, summaries |

New versions: branch off `galaxy-1d` (or off the latest version branch) and name clearly, e.g. `ARK-GAL-1D-9.5`. Avoid nesting names under an existing branch ref (Git collision).

## Why 1D has its own line

- Collapse from 3D → 1D throws away structure; that loss shows up in residuals (not in tuning knobs)
- Zero articulation: take kinematics / data in, emit results — no free parameters to absorb “dark” phenomenology or projection loss
- Typical SPARC RMS in recent discussion ~23–25; v9.4 dump summary shows ~30–33 km/s global RMS depending on projector — keep numbers tied to the specific run files
- Residual attribution remains an open, disciplined question (projection loss vs external influence)

## Parent / siblings

- Parent: [`galaxy-modeling`](https://github.com/Pfpercy0214/aetherwave-unified-theory/tree/galaxy-modeling) (`1d/` folder drop zone there too)
- Theory corpus: `main`, [`workspace/gwok`](https://github.com/Pfpercy0214/aetherwave-unified-theory/tree/workspace/gwok)
- Early papers set: [`Papers`](https://github.com/Pfpercy0214/aetherwave-unified-theory/tree/Papers)

## Ground rules

1. **No deletes without Paul’s explicit OK.**
2. Keep knobs out of the core method — if something is tuned, label it as calibration or experiment, not silent fit.
3. When discussing residuals, keep **projection loss** and **outside influence** as separate hypotheses with different falsifiers.
4. MOND-style low residuals are not treated as proof of mechanical completeness when knobs can absorb lost 3D structure.

## Drop zone

- Shared 1D notes / tools → this branch or `galaxy-modeling/1d/`
- Versioned run packages → their own offshoot (like `ARK-GAL-1D-9.4`)

---

*1D ARK galaxy modeling — honest residuals over pretty knobs.*
