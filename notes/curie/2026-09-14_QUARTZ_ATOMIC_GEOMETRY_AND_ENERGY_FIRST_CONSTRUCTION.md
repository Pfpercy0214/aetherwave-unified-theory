# 2026-09-14 Research — Quartz Atomic Geometry, Field Coupling, and Energy: First Construction

**Status:** TARGET-INFORMED CONSTRUCTION / GEOMETRY AND ENERGY CONSISTENCY CHECKS. NOT AN ARK MICROSCOPIC DERIVATION OR VALIDATION.

**Research date:** 2026-09-14. This is a new calculation, not a backdated modification of the September 10–12 records.

**Researchers:** Paul F. Percy Jr. (framework and research direction), Curie (research, implementation, and audit).

**Starting record:** `2026-09-12_OHMIC_TOPOLOGY_GEOMETRIC_GATING_COLLECTIVE_IDENTITY_AND_STATE_SPACE_COLLAPSE.md`.

**Executed code:** `experiments/2026-09-14_quartz_cell/quartz_cell_audit.py`. Run with Python 3.10+ and NumPy: `python quartz_cell_audit.py --out results`.

## 1. Question and result class

The agreed task was to start below the resonator-frequency level: specify a small quartz lattice, apply an electrical perturbation, and require its field response, deformation, and energy accounting to agree. The guiding hypothesis is that coupled identity geometry constrains the material response, rather than that each atom is an independent valve.

This pass executes three distinct calculations:

1. A periodic nine-atom structural reconstruction and directional field projection.
2. An infinitesimal compatibility calculation in the ideal rigid-SiO4 limit.
3. A coupled, cell-averaged electrical/mechanical energy control using independently published constitutive tensors.

The first two do not supply the constitutive coefficients used by the third. In particular, this is **not** a calculation of atomically resolved electric fields, electron density, substrate flux, or internal atomic displacements from ARK. The signed coordinate mapping between the crystallographic dataset and the material-tensor convention is not yet registered. Their scalar/geometric and energy checks are therefore kept separate rather than silently combined.

No measured resonance frequency, current-versus-voltage curve, damping constant, damage threshold, or channel count was used to fit this construction. Published geometry and elastic/piezoelectric/dielectric coefficients are inputs, not quantities derived here. There are no parameters fitted to a resonance target in this pass; there are explicit model assumptions and imported material parameters.

## 2. Sources and provenance

**S1 — Crystallography:** *Calculating temperature-dependent X-ray structure factors of alpha-quartz with an extensible Python 3 package*, Journal of Applied Crystallography (2022), DOI `10.1107/S1600576722005945`. Tables 2–4 give the 298 K Kihara-derived lattice parameters and the complete dextro z(+) basis.

https://journals.iucr.org/j/issues/2022/04/00/te5094/

**S2 — Atom-motion evidence:** Aoyagi et al., *Atomic motion of resonantly vibrating quartz crystal visualized by time-resolved X-ray diffraction*, Applied Physics Letters 107, 201905 (2015), DOI `10.1063/1.4935591`. The authors' accessible account was read: Aoyagi and Takeda, *Transient Crystal Structure of Oscillating Quartz* (2022), DOI `10.5772/intechopen.107414`.

https://www.intechopen.com/chapters/83792

**S3 — Conventional tensor/energy control:** ANSYS Coupled-Field Analysis Guide, section 2.3.7, Table 2.15 and associated matrix listing; the constants are attributed there to Ballato (2008). Its assumed dielectric-loss values are NOT used.

https://ansyshelp.ansys.com/public/Views/Secured/corp/v261/en/ans_cou/Hlp_G_COU3_piezo.html

**S4 — Convention guard:** COMSOL, *Piezoelectric Material Orientation*. The IRE and IEEE axis definitions change signs and the signed AT-cut angle. This is why basis registration is a substantive step, not cosmetic notation.

https://doc.comsol.com/6.4/doc/com.comsol.help.sme/sme_ug_modeling.05.108.html

**S5 — Next microscopic inputs:** ABINIT's elastic/piezoelectric tutorial distinguishes interatomic force constants, Born effective charges, internal-strain coupling, and clamped-ion versus relaxed-ion tensors.

https://docs.abinit.org/tutorial/elastic/

Accessed 2026-09-14. This research uses the public sources above in addition to the project note; outside evidence is not being represented as an existing ARK derivation.

## 3. Experimental constraint that changes our first microscopic picture

The authors' X-ray account reports that the SiO4 tetrahedra remained comparatively rigid within measurement resolution, while inter-tetrahedron Si–O–Si angles changed during resonant motion. Particularly responsive oxygen bridges were associated with a field direction about 66 degrees to their Si–O–Si planes [S2].

Consequently, the first candidate is not “all atomic envelopes must be squeezed substantially.” A more constrained starting picture is: comparatively stiff structural units connected through more compliant angular arrangements. That supports investigating geometry-dependent collective response; it does not establish aether, literal passageways, a pressure-driven current, or a common origin with gravity.

This evidence was seen before constructing the projection and rigid-unit tests. Those tests are therefore **target-informed structural checks**, not blind predictions of the X-ray result.

## 4. Reconstructed atomic geometry

We generated the periodic P3221 cell using [S1]:

- `a = b = 4.9137 angstrom`, `c = 5.4047 angstrom`;
- lattice vectors `a1=(a,0,0)`, `a2=(-a/2,sqrt(3)a/2,0)`, `a3=(0,0,c)`;
- prototype Si `(0.4697,0,0)`;
- prototype O `(0.4133,0.2672,0.1188)`;
- three Si and six O positions generated by the published screw/twofold operations.

Calculated volume: **113.01068294 angstrom^3**. Each Si has four nearest O neighbors and each O bridges two Si atoms, including neighboring periodic cells. This connectivity is unchanged for the tested distance cutoffs 1.7, 1.8, and 1.9 angstrom; the cutoff is a connectivity-identification choice, not a fitted bond radius.

Calculated Si–O distances are approximately **1.605222 and 1.613385 angstrom**. The Si–O–Si bridge angle is **143.588939 degrees**. These are reconstructions from the supplied coordinates, not new measurements or binding-energy predictions.

## 5. Field direction selects different local geometries

For each oxygen bridge, form the two bond vectors from O to its neighboring Si atoms and calculate the unit normal `n_i` to their plane. For a chosen unit field direction `E_hat`, define

`p_i = n_i dot E_hat`.

For the geometric example use `E_hat=(0,cos(35.25 deg),sin(35.25 deg))` in the explicitly stated crystallographic frame. The angle between the field and the bridge plane is `asin(abs(p_i))`.

| Sites in this code's basis | Field-to-plane angle | Share of the summed squared projection |
|---|---:|---:|
| O1, O4 | 10.8807 degrees | 3.5634% |
| O2, O5 | 21.1880 degrees | 13.0639% |
| O3, O6 | 65.9313 degrees | 83.3726% |

The final column is `(p_i^2+p_j^2)/sum_k p_k^2`. It is a **geometric score only**. It is NOT a fraction of electric current, actual energy, occupied channels, physical displacement, or probability. Interpreting it as a response weighting would additionally assume suitable equal local coupling/compliance and neglect neighbor feedback.

The approximately 66-degree class agrees with the geometric motif discussed in [S2], but atom numbers are local labels: our O3/O6 are NOT asserted to be the same numbered atoms as the authors' O2/O3 without a coordinate crosswalk. Rotation checks and the opposite tilt are retained in the JSON output. Changing direction changes the projection pattern; increasing magnitude alone does not change normalized projection weights.

## 6. A concrete geometric state-space reduction

We then tested the ideal limit in which each SiO4 unit retains its internal shape, while neighboring units share their oxygen positions.

Unknowns are 27 periodic, non-affine Cartesian displacement components plus six homogeneous symmetric cell strains: **33 variables**. Non-affine displacements are scaled by `a` to make the rank test dimensionless. Overall cell rotation is excluded by using symmetric strain; three translations are fixed by a zero-mean displacement gauge.

For each of three SiO4 units, preserve four Si–O lengths and six O–O distances. This gives 30 linearized bond-length rows, some dependent. For a bond vector `b`, the first-order constraint is

`b_hat dot (u_j - u_i + S b) = 0`.

Assembling all shared-neighbor constraints and the translation gauge gives a 33-column matrix. Its numerical rank is **30**, leaving **three compatible infinitesimal deformation directions** in this idealization. The rank remains 30 for relative singular-value cutoffs `1e-8`, `1e-10`, and `1e-12`. A central finite-difference check of the analytic bond-length Jacobian has a maximum discrepancy of about `6.35e-11`. The nullspace residual is near machine precision.

With the cell additionally fixed, no nontrivial zero-cost motion remains at this periodicity. This does NOT mean a fixed-cell real crystal cannot vibrate; finite bond deformation was excluded by the ideal rigid constraints.

This is an executed example of compatibility removing independent motion choices. It is not a count of quartz phonon branches, an eigenfrequency calculation, or a demonstration that quantum probabilities become unique outcomes. It concerns infinitesimal zero-wavevector kinematics and an assumed rigid-unit limit, not a finite-amplitude or general-wavevector theory.

Perfect rigidity is a controlled hypothesis, not an observed infinity. “No bond change resolved by X-rays” does not mean the true bond stiffness is infinite. A later finite-stiffness model must recover this limit and quantify deviations from it.

## 7. One energy law for the averaged field and deformation

A separate conventional control uses engineering strain

`s=(Sxx,Syy,Szz,2Syz,2Sxz,2Sxy)`

and the published tensors [S3]. The field is cell-averaged and homogeneous, appropriate to a long-wavelength interior material-point control. It is imposed, not an atomically resolved solution around nuclei. The cell volume from section 4 is used only for reporting energy per cell, an orientation-invariant conversion.

At fixed electric field, define electric enthalpy density

`H(s,E) = (1/2) s^T C^E s - E^T e s - (1/2) E^T eps_diel^S E`.

Differentiation gives the mutually consistent pair

`sigma = C^E s - e^T E`,

`D = e s + eps_diel^S E`.

Here `D` is electric displacement (charge per area), not a volume flux of a substrate. `eps_diel` denotes dielectric permittivity, NOT the project's resolved perturbation epsilon. The same cross term determines both mechanical drive and electrical back-reaction; independently choosing two unrelated coupling laws would not guarantee this reciprocity.

At zero applied mechanical stress,

`s = (C^E)^(-1) e^T E`.

The material inputs in GPa are `C11=86.74`, `C12=6.99`, `C13=11.91`, `C14=-17.91`, `C33=107.2`, `C44=57.94`, and `C66=(C11-C12)/2=39.875`. Using the exact trigonal relationship rather than the separately rounded 39.88 entry follows the source's alternate matrix listing. Piezoelectric stress coefficients are `e11=0.171`, `e14=-0.0406 C/m^2`. Constant-strain permittivities are `39.21,39.21,41.03 pF/m`.

The code retains the ANSYS matrix convention and signs. It does not silently attach those signed tensors to the IUCr atomic labels; that registration is still required for an atom-specific coupled solve.

For the specified numerical field

`E = 100000 (0,cos(35.25 deg),sin(35.25 deg)) V/m`,

the free-strain control gives:

- `2Sxz = -5.92571092e-8`;
- `2Sxy = -3.76824211e-7`;
- other strain components zero in this linear control;
- `D = (0, 3.26408264e-6, 2.36802671e-6) C/m^2`.

These are static strain components, not displacements of individual oxygen atoms or a mode amplitude at resonance. The field is a numerical normalization, not a recommended operating voltage.

## 8. Energy accounting and guards

The physical internal-energy density is the Legendre transform `U=H+E dot D`. Expressed in independent variables `(s,D)`, it is

`U(s,D) = (1/2)s^T C^E s + (1/2)(D-e s)^T (eps_diel^S)^(-1)(D-e s)`.

It satisfies `dU = sigma dot ds + E dot dD`. At the calculated zero-stress state:

| Quantity | Calculated value, J/m^3 |
|---|---:|
| Elastic storage | 0.002532858759 |
| Dielectric storage | 0.199081178790 |
| Total storage | 0.201614037549 |
| Electrical work, reversible zero-to-field ramp | 0.201614037549 |

The calculated total is **2.27845401e-29 J per crystallographic cell**. This very small driven-energy increment is not the thermal energy of a cell; thermal equilibrium fluctuations were not simulated.

Executed checks:

- Elastic matrix positive definite; smallest eigenvalue approximately 28.85 GPa in the stated engineering-coordinate representation.
- Relative mechanical-balance residual: `3.17e-17`.
- Relative ramp-work/storage discrepancy: `1.38e-16`.
- Closed reversible ramp-up/ramp-down work: `-2.78e-17 J/m^3`, numerical roundoff.
- Reversing the field reverses strain and polarization response; storage is unchanged.
- Doubling field doubles strain and quadruples storage.
- A field along the material Z axis gives zero linear piezoelectric strain but nonzero dielectric response.
- Rotating the field and ALL material tensors together preserves the solution and energy; relative covariance errors are approximately `2e-16`.

These are numerical/analytic consistency checks, not experimental error bars. No independently characterized input covariance has been supplied, so this pass does not establish comparable physical precision.

## 9. What this says about the working interpretation

**Geometry matters in a specific way.** The structural response can be strongly directional without every atom changing identically. Coupled angular changes between relatively rigid units are a better first target than a uniform “atomic squeezing” picture.

**Pressure cannot be represented solely by an unsigned magnitude.** In this linear control, `s(-E)=-s(E)`. A forcing law depending only on `|E|^2` cannot reproduce that odd response. A medium interpretation must preserve polarity, direction, and the material's asymmetric coupling; it cannot substitute one unsigned scalar pressure for the entire electric field. This is a symmetry constraint, not an argument against investigating a medium.

**A changing normalized participation pattern is NOT established.** The geometric projections and the linear energy model scale smoothly with field. Neither creates a voltage threshold, adds channels, saturates their width, or predicts noise. Those remain hypotheses requiring nonlinear response and a spatially resolved coupling law. A rising quartic restoring cost alone does not prove recruitment of neighboring paths.

**Heat is not synonymous with permanent identity loss.** This intentionally reversible model transfers and stores energy with zero cycle loss. An irreversible extension would need independently constrained dissipative or history variables. It cannot label all deformation or stored energy as heat, nor infer defects/plasma from amplitude scaling alone.

**The state-space result is limited but useful.** Actual shared geometry plus declared rigidity constraints reduced 30 nontranslational coordinates to three infinitesimal compatible directions. Whether one is selected, and how rapidly it moves, still requires forces, coupling, inertia, and boundaries.

## 10. ARK scalar consistency retained

The project quantities remain proposed interpretations of state/response, not aliases for the coefficients in section 7:

- theta: geometry/configuration, whose operational projection must be specified;
- kappa: resistance to changing that configuration;
- tau: stored/persistent state, with its conjugate variable and history dependence still to be fixed;
- resolved epsilon: measured/derived perturbation contribution;
- unresolved contribution: explicitly unmeasured environmental state, not a residual fitted to force agreement;
- J: a separate transport observable. No substrate J has been calculated here.

If the proposed path relation is `d tau = kappa_tangent d theta`, then

`tau(t)-tau(t0) = integral kappa_tangent(s) theta_dot(s) ds`.

It is not generally interchangeable with `tau=kappa theta`. Differentiating that product adds `theta d kappa`. A secant coefficient and a tangent coefficient must not be silently identified. Nor does a purely reversible single-valued integral, by itself, supply independent hysteretic memory.

These statements preserve the earlier discussion while avoiding a new numerical closure based merely on rearranging familiar symbols.

## 11. Next construction now specified

The next microscopic energy can be written schematically for internal atomic displacements `u`, homogeneous strain `s`, and electric field `E`:

`H_cell = (1/2)u^T K u + u^T L s + (1/2)s^T C_cell,cl s`

`         - E^T (Z u + e_cell,cl s) - (V0/2) E^T eps_cl E`.

All terms here are energies per cell; `K`, `L`, `Z`, and the cell-scaled tensors must carry corresponding units. Translational zero modes must be removed or constrained. The desired response follows from stationarity in `u,s`, with polarization obtained from the SAME energy derivative.

The necessary microscopic inputs are: force constants `K`, internal-strain coupling `L`, Born effective charges `Z`, and the electronic/clamped-ion contribution. These are precisely the distinct response objects described in [S5]. Static charge populations from a density partition are not automatically Born effective charges and must not be substituted uncritically.

Once those inputs are registered in one crystal convention, solve the oxygen/silicon displacement response, then check whether eliminating internal coordinates recovers the bulk elastic and piezoelectric control. That is a concrete microscopic-to-collective consistency test. A subsequent field-gradient or neighboring-cell problem can test spatial redistribution. No resonance fitting or galaxy-specific correction is needed for this step.

The substrate interpretation must eventually derive or independently constrain these response objects rather than merely rename them. This pass does not claim that has been done.

## 12. Frozen conclusion

We have started with real geometry and executable calculations. The first results are a directional bridge-geometry map, a sharply stated rigid-unit compatibility reduction, and a reciprocal electrical/mechanical energy control with closed work accounting.

**Retain:** geometry-conditioned collective response, the separation of field from flux, reference-state discipline, tangent-versus-secant stiffness, and explicit energy bookkeeping.

**Not established:** literal aether passageways, channel recruitment with voltage, nonlinear fidelity loss, irreversible lattice damage, atomically resolved field flow, quantum outcome selection, an ARK-derived quartz frequency, or a unification with gravity.

**Next:** force-constant/Born-charge/internal-strain coupling in a single registered atomic basis. The equations now specify what information is missing rather than masking it in an adjustable gate function.
