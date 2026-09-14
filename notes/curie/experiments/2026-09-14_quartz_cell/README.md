# Quartz cell — verified research checkpoint and next-step ledger

**Record date:** 2026-09-14  
**Branch:** `workspace/curie`  
**Purpose:** Verify Paul's uploaded package against the supplied files, index the recent discussion and completed first construction, and record the next agreed step before further modeling. This is a documentation and artifact-integrity check, not a new physical result or a new numerical run.

## 1. Files verified

The live folder contained the standalone script, the uploaded research-note copy, and the uploaded ZIP. Git content hashes computed from the supplied local files match the live repository entries:

| File | Git blob SHA | Verification |
|---|---|---|
| `quartz_cell_audit.py` | `510ddb0d2f1151d70974b8c77a260abb3c022942` | Matches the script inside the supplied ZIP |
| `2026-09-14_QUARTZ_ATOMIC_GEOMETRY_AND_ENERGY_FIRST_CONSTRUCTION.md` | `3ad4f445b8d3618095c78f17e838f6257921b023` | Matches the supplied note, ZIP copy, and existing note under `notes/curie/` |
| `ARK_Quartz_First_Construction_2026-09-14.zip` | `93d9f4e497fa8f72419a0cb1c3e82c8124487dcb` | Matches the supplied 22,416-byte archive |

The branch tip observed during verification, before adding this README, was `fac62b04f33fadfd6a3dfd2eef34ae7efcc9c09b`.

The ZIP passed its CRC integrity test. All seven entries listed in its `SHA256SUMS.txt` matched their contents. The `code_sha256` embedded in `results/results.json` matches the packaged and repository script:

```text
593b2f441a3f6c0c8e71e06b81138a50be8687f1538bbde66466393cc39d44f5
```

The archive SHA-256 is:

```text
fa9258893dc14f0394eace673958e2a4e499025ffedd6bbdbad2f32ef258434f
```

The original code and research-note commits were `07c4ae88404bb89f5db1a1c50dcc668a3a344df1` and `6edbc5d5b8ce916a5142c989f139af47f4e503a6`, respectively. Paul's upload additionally preserves the supplied package with the stored output files.

No existing script, result, uploaded archive, or historical note was changed by this verification. Matching artifacts establishes file identity and integrity; it does not independently validate their physical claims.

## 2. Where the records live

- [September 12 discussion record: Ohmic topology, geometric gating, collective identity, and state-space reduction](../../2026-09-12_OHMIC_TOPOLOGY_GEOMETRIC_GATING_COLLECTIVE_IDENTITY_AND_STATE_SPACE_COLLAPSE.md).
- [September 14 primary research note](../../2026-09-14_QUARTZ_ATOMIC_GEOMETRY_AND_ENERGY_FIRST_CONSTRUCTION.md).
- [Identical uploaded copy of the September 14 note](./2026-09-14_QUARTZ_ATOMIC_GEOMETRY_AND_ENERGY_FIRST_CONSTRUCTION.md).
- [Executable calculation](./quartz_cell_audit.py).
- [Frozen supplied package, including results and checksums](./ARK_Quartz_First_Construction_2026-09-14.zip).

The two standalone September 14 notes are identical at this checkpoint. Treat the experiment-folder copy and ZIP as the supplied snapshot; record later changes explicitly rather than silently allowing duplicate notes to diverge. The script path printed in the primary note is relative to `notes/curie/`; from this experiment folder the script is simply `./quartz_cell_audit.py`.

The ZIP contains one top-level directory, `ark_quartz_cell_2026-09-14/`, with:

```text
README.md
quartz_cell_audit.py
2026-09-14_QUARTZ_ATOMIC_GEOMETRY_AND_ENERGY_FIRST_CONSTRUCTION.md
RESULT_SUMMARY.json
results/atomic_positions.csv
results/bridge_geometry.csv
results/results.json
SHA256SUMS.txt
```

The output JSON and CSV files are preserved inside the ZIP, not currently unpacked as separate repository files. The ZIP's packaged README is the original package guide; this repository README is a separate, later checkpoint index.

To rerun, use Python 3.10+ with NumPy and execute `python quartz_cell_audit.py --out results`. To inspect the frozen outputs without rerunning, unpack the archive. Do not treat a future regenerated output as the historical run without recording that distinction.

## 3. Coverage of the recent findings

| Topic | Where recorded | Status at this checkpoint |
|---|---|---|
| Ohm's-law resemblance, rejection of literal variable identification, external perturbation distinct from internal tension memory, and separate flux `J` | September 12, sections 1–4 | Working interpretation, not a transport derivation |
| Coupled neighboring identities, geometric gating, binding/gravity continuity hypothesis, and geometry restricting admissible configurations | September 12, sections 5–9 | Hypotheses and intended tests, not established unification or deterministic quantum-outcome results |
| V9.4 ratio-closure concern and V5.4 answer-forcing safeguards | September 12, sections 3 and 10; September 14, section 10 | Preserve the distinction between a justified constitutive relation and a target-supplying closure |
| Tangent versus secant stiffness and the `theta d kappa` product-rule distinction | September 14, section 10 | Mathematical consistency requirement; a reversible integral alone is not independent hysteretic memory |
| Nine-atom structure, bridge orientations, and geometry-only projection scores | September 14, sections 3–5; packaged results | Completed construction using published inputs; not inferred substrate flux |
| Three surviving infinitesimal deformation directions in the declared periodic rigid-unit approximation | September 14, section 6; packaged results | Completed compatibility calculation; not all phonon modes or all physical possibilities |
| Reciprocal averaged electrical/mechanical control, work/storage accounting, polarity and coordinate checks | September 14, sections 7–8; packaged results | Completed consistency control using imported tensors, not an ARK-derived atomistic field solution |
| Voltage-dependent recruitment, nonlinear fidelity changes, dissipation, and persistent damage | September 14, section 9; clarification below | Not established by the linear calculation |
| Coordinate registration and microscopic force/electrical coupling inputs | September 14, section 11; next-step ledger below | Pending |

The scope is the recent Ohmic/gating-to-quartz discussion and the supplied first-construction package. This check does not certify every historical paper, repository branch, or older solver.

## 4. Preserve the post-discussion hypotheses without promoting them to findings

Paul's proposed refinement is that a connected region may reach a point where further opening becomes more costly than deforming the next compatible region. Greater applied drive could then change spatial participation; still greater sustained drive could alter the restoring response, spectral behavior, or recoverability. This is not a demonstrated hard channel-size cap, a measured activation threshold, or a computed recruitment law. The previous quartic-potential illustration did not establish those consequences.

The intended use of "identity decay" in this discussion is loss or reorganization of an organized configuration, not automatically radioactive decay. The discussion distinguishes reversible distortion, energy leaving a coherent mode, and persistent structural alteration. Proposed plasma or more extensive breakdown regimes remain outside the current calculation. Heat, distortion, deterministic harmonics, and permanent damage must not be silently equated.

The working idea remains a coupled loop between perturbation, collective geometry, restoring/persistent response, and possible transport redistribution. Literal medium passageways, atomic-envelope squeezing, and a common origin for bonding and gravity have not been inferred from the three calculations in the package. The first-construction note refines the immediate microscopic target toward relatively rigid units and angular changes at their connections.

Target-informed construction is permitted: known behavior can help develop the candidate. The record must say which observations selected a constraint or coefficient. A match to those construction inputs is not an independent prediction; portability tests must freeze the relationship and distinguish new evidence from reused calibration.

## 5. Immediate next step — agreed, not executed

The newest discussion adds an explicit compatibility-first checkpoint before acquiring or adjusting more microscopic coefficients:

1. **Register conventions.** Put the atomic basis and material tensors into the same axes, handedness, atom labeling, and electric-field convention.
2. **Check the permitted strain space.** Determine whether a combination of the three rigid-unit-compatible directions can represent the bulk-control shear in that common convention. No result of this test has yet been recorded. A mismatch could expose a convention error or the limits of the rigid-unit approximation; do not force a match by changing coefficients.
3. **Acquire consistent microscopic response inputs.** Interatomic force constants `K`, internal-strain coupling `L`, Born effective charges `Z`, and the clamped-ion contributions must belong to a registered structure and consistent units. Their numerical dataset has not yet been supplied or validated for this model.
4. **Solve the coupled atomic/cell response from one energy.** The proposed zero-mechanical-stress stationarity equations are:

```text
K u + L s = Z^T E
L^T u + C_cell,cl s = e_cell,cl^T E
```

These are the block equations from section 11 of the primary note, not new solved results. Remove translational zero modes consistently. Obtain polarization from the same energy derivative.

5. **Compare microscopic and collective responses.** Record atomic displacement vectors, bridge-angle changes, cell strain, polarization, and work/storage accounting. Recovering bulk behavior is independent evidence only where the microscopic coefficients were not fitted to that same bulk behavior.

A changing geometry is not by itself demonstrated transport. Spatial field redistribution, a substrate flux law, nonlinear recruitment, dissipation, and resonance remain subsequent tasks. No new numerical experiment was run during this documentation check.

## Checkpoint conclusion

The supplied artifacts and stored results are present and consistent, the earlier discussion record remains available, and the newest compatibility-first plan is now explicit. Continue from the registered-coordinate compatibility check, not from a claim that atomically resolved ARK field flow or resonance has already been solved.
