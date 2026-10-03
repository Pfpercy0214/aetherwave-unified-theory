# Quartz cell scope — 2026-10-03

**Status:** SCOPE LABEL. Not a replacement model. Curie files were not edited.

The 2026-09-14 quartz cell run is a static bulk cell. It is not a resonator. A resonator is a cut, electroded plate driven in shear.

## What stays, as material checks, not device results

- Signed strain flips when the field flips, so a law of `|E|^2` cannot be that response.
- Exact rigid tetrahedra leave a 41.3% strain-tensor residual against the imported control (shear ratio 0.658 against 0.157). That 41.3% is the static strain-tensor miss. It is not the Layer-0 frequency residual and not the Baù miss. Letting the angles move only shows a motion is possible. It is not the motion the forces select.
- The laevo sign-family registration is done. The signed material tensors are still not on the crystallographic atom labels, and no resonator handedness was inferred from that registration.
- Geometry, the rigid-unit rank, and the imported energy control stay separate calculations.
- The permittivity in that energy law is not the project's perturbation epsilon.
- Zero cycle loss means dissipation was left out, not that a Q was measured.

## What this run does not contain

- Bridge angle versus time. The moving Si–O–Si angle is the earlier X-ray observation. It was seen before the tests, and the motion was driven. It is not a prediction from this run, and it is not yet the definition of θ.
- A frequency. No mass is declared. A constant field only shifts the rest state. Two peaks in one return would be twice `f_rec`.
- The AT-cut operation. 35.25° in the run is a field direction inside the uncut periodic cell, with no electrodes and no thickness. On a real AT plate that angle orients the blank, and the drive is through the thickness after the cut. The audit also used other directions, including straight along Z, where the linear control stores dielectric energy and produces no linear strain. The audit is several field directions in the uncut cell, not one AT angle.

The X-ray record of the material in use stays. Walking back the device reading does not remove it.

The replacement use-model is not guessed here. Paul and Curie are setting that.

## Sources (read only)

- `workspace/curie` `notes/curie/2026-09-14_QUARTZ_ATOMIC_GEOMETRY_AND_ENERGY_FIRST_CONSTRUCTION.md`
- `workspace/curie` `notes/curie/experiments/2026-09-14_quartz_cell/CURRENT_STATUS.md`
