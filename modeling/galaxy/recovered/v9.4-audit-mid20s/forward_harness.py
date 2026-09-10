#!/usr/bin/env python3
"""
ARK Forward-Solver Acceptance Harness (v1)
==========================================
Purpose: score CANDIDATE medium-response functions against synthetic tests
and measured targets. Per Firewall Protocol (record Step 12):
  - This harness contains the TARGETS. The derivation may never cite them.
  - The harness never suggests modifications to a candidate.
  - A candidate is a function R(y): dimensionless response vs y=|grad Phi|/a_c,
    plus at most ONE calibrated scale a_c (claim class ledgered by caller).

FIELD EQUATION (harness working variable):
  div[ R(|grad Phi|/a_c) * grad Phi ] = 4*pi*G*rho      (quasi-static)
  Spherical flux form solved pointwise:  R(y)*y*a_c = g_N(r)
  v_circ^2 = |grad Phi| * r
LEDGER (interface assumptions, pending derivation's own variable choice):
  L1. Corpus mapping Phi = c^2 * theta_c^2 / 2 (Paper I weak field). In
      theta-variables the NEWTONIAN limit is kappa_eff ~ theta (not const);
      the derivation binds to whichever variable it derives, mapping noted.
  L2. Source couples linearly to mass (nonlinearity under test lives in
      the medium response, matching AQUAL / superfluid-DM structure).
  L3. Quasi-static: Lambda=0, time derivatives dropped (documented ARK
      choice, V9.5 record).
TARGETS (measured; scoring only):
  T1. Newtonian identity limit: R(y)->1 as y->inf (high-acceleration
      convergence of the RAR; lab/solar-system Newton).
  T2. Deep-regime flat curves: for exponential-disk synthetics, outer
      v(r) slope -> ~0 (observed flat rotation curves).
  T3. Superposition threshold: additivity violation must be ~0 at low
      local density and switch on above a threshold (record Steps 10-11:
      dose-response, zero below ~decile 5, ramp to ~5%).
  T4. Guard: no manufactured structure (Keplerian point-source input must
      return Keplerian-consistent output in the Newtonian regime).
  T5. Harness self-test: known-wrong candidates MUST fail (F5).
"""
import numpy as np
from scipy.optimize import brentq
from scipy.integrate import cumulative_trapezoid

G = 1.0  # harness units


# ----------------------------------------------------------------------
# Candidate interface
# ----------------------------------------------------------------------
class Candidate:
    """A medium response function R(y), y = |grad Phi| / a_c."""
    def __init__(self, name, R, a_c=1.0, claim_class="UNSET"):
        self.name, self.R, self.a_c, self.claim_class = name, R, a_c, claim_class

    def solve_spherical(self, r, rho):
        """Solve R(y)*y*a_c = g_N pointwise. Returns g=|grad Phi|, v."""
        M = cumulative_trapezoid(4 * np.pi * r**2 * rho, r, initial=0.0)
        g_N = G * M / np.maximum(r, r[0]) ** 2
        g = np.empty_like(g_N)
        for i, s in enumerate(g_N):
            if s <= 0:
                g[i] = 0.0
                continue
            f = lambda y: self.R(y) * y * self.a_c - s
            hi = max(s / self.a_c, 1.0)
            while f(hi) < 0:
                hi *= 4.0
                if hi > 1e12:
                    break
            g[i] = brentq(f, 0.0, hi, maxiter=300) * self.a_c \
                if f(hi) >= 0 else np.nan
        # NOTE: solve returns y*a_c = |grad Phi| directly
        v = np.sqrt(np.maximum(g * r, 0.0))
        return g, v


# Reference candidates — harness VALIDATORS, not ARK proposals.
REFERENCE = {
    # pure Newton: must PASS T1/T4, FAIL T2/T3
    "newton": Candidate("newton", lambda y: 1.0, claim_class="reference"),
    # simple-mu MOND-like: R(y)=y/(1+y) -> passes T1/T2; T3 diagnostic
    "mond_simple": Candidate("mond_simple", lambda y: y / (1.0 + y),
                             claim_class="reference (empirical form)"),
    # known-wrong: response DECREASES with y — must fail T1 (F5 check)
    "inverse_wrong": Candidate("inverse_wrong",
                               lambda y: 1.0 / (1.0 + y),
                               claim_class="deliberately wrong"),
}


# ----------------------------------------------------------------------
# Synthetics
# ----------------------------------------------------------------------
def synth_point(r, M=1.0, eps=0.05):
    rho = np.zeros_like(r)
    core = r < eps
    rho[core] = M / (4.0 / 3.0 * np.pi * eps**3)
    return rho

def synth_expdisk(r, M=1.0, rd=1.0):
    # spherically-averaged exponential proxy (harness-level, ledgered)
    rho = np.exp(-r / rd)
    norm = np.trapezoid(4 * np.pi * r**2 * rho, r)
    return rho * (M / norm)


# ----------------------------------------------------------------------
# Tests
# ----------------------------------------------------------------------
def T1_newton_limit(c, tol=0.02):
    """High-acceleration convergence: g/g_N -> 1 for a compact heavy source."""
    r = np.linspace(0.02, 10, 800)
    rho = synth_point(r, M=1e6)          # deep Newtonian regime everywhere
    g, _ = c.solve_spherical(r, rho)
    M = cumulative_trapezoid(4 * np.pi * r**2 * rho, r, initial=0.0)
    g_N = G * M / r**2
    inner = slice(50, 400)
    dev = np.nanmax(np.abs(g[inner] / g_N[inner] - 1.0))
    return dev < tol, f"max |g/g_N - 1| = {dev:.4f} (tol {tol})"

def T2_flat_curves(c, tol=0.10):
    """Deep regime: outer log-slope of v(r) for a light exp disk -> ~0."""
    r = np.linspace(0.05, 40, 900)
    rho = synth_expdisk(r, M=1e-3, rd=1.0)   # deep low-acceleration regime
    _, v = c.solve_spherical(r, rho)
    outer = slice(-300, None)
    sl = np.polyfit(np.log(r[outer]), np.log(np.maximum(v[outer], 1e-12)), 1)[0]
    return abs(sl) < tol, f"outer dlnv/dlnr = {sl:+.3f} (|.|<{tol}); Newton gives -0.5"

def T3_superposition_threshold(c):
    """Additivity violation vs density: must be ~0 at low rho, rise above
    a threshold. Reports the violation curve; PASS = monotone with a
    low-density floor <0.5% and high-density violation >2x floor."""
    r = np.linspace(0.05, 20, 700)
    out = []
    for scale in [1e-4, 1e-3, 1e-2, 1e-1, 1.0, 10.0]:
        A = synth_expdisk(r, M=scale, rd=1.0)
        B = synth_expdisk(r, M=scale, rd=3.0)
        gA, _ = c.solve_spherical(r, A)
        gB, _ = c.solve_spherical(r, B)
        gAB, _ = c.solve_spherical(r, A + B)
        m = (gA + gB) > 0
        viol = np.nanmedian(np.abs(gAB[m] - (gA + gB)[m]) / (gA + gB)[m])
        out.append((scale, viol * 100))
    floor = out[0][1]; top = out[-1][1]
    mono = all(out[i][1] <= out[i + 1][1] + 1e-9 for i in range(len(out) - 1))
    ok = (floor < 0.5) and (top > max(2 * floor, 1.0)) and mono
    curve = ", ".join(f"{s:g}:{v:.2f}%" for s, v in out)
    return ok, f"violation vs source scale -> {curve}"

def T4_guard_keplerian(c, tol=0.05):
    """Point source in Newtonian regime: v must decline Keplerian (-1/2)."""
    r = np.linspace(0.05, 10, 500)
    rho = synth_point(r, M=1e6, eps=0.15)
    _, v = c.solve_spherical(r, rho)
    sl = np.polyfit(np.log(r[100:]), np.log(np.maximum(v[100:], 1e-12)), 1)[0]
    return abs(sl + 0.5) < tol, f"point-source dlnv/dlnr = {sl:+.3f} (target -0.500)"

TESTS = [("T1 newton-limit", T1_newton_limit),
         ("T2 flat-curves", T2_flat_curves),
         ("T3 superposition-threshold", T3_superposition_threshold),
         ("T4 keplerian-guard", T4_guard_keplerian)]


def score(c):
    print(f"\n=== candidate: {c.name}  [claim class: {c.claim_class}] ===")
    results = {}
    for name, fn in TESTS:
        try:
            ok, msg = fn(c)
        except Exception as e:
            ok, msg = False, f"ERROR {e}"
        results[name] = ok
        print(f"  {name:<28} {'PASS' if ok else 'FAIL'}  {msg}")
    return results


if __name__ == "__main__":
    print("ARK forward harness v1 — self-test (F5: rig must fail wrong candidates)")
    tally = {}
    for c in REFERENCE.values():
        tally[c.name] = score(c)
    print("\nF5 verdict:")
    print("  newton        expected: T1/T4 PASS, T2 FAIL  ->",
          "OK" if (tally['newton']['T1 newton-limit'] and
                   tally['newton']['T4 keplerian-guard'] and
                   not tally['newton']['T2 flat-curves']) else "HARNESS BUG")
    print("  inverse_wrong expected: T1 FAIL              ->",
          "OK" if not tally['inverse_wrong']['T1 newton-limit'] else "HARNESS BUG")
