# Open issues

Found while reorganizing (2026-11-01). **Nothing here has been fixed.** The
notebooks' code and outputs are exactly as they were on `main`. This list is
recorded so it isn't lost, for whenever the science gets revisited.

## Does not run on a fresh *Run all*

- `draft_polya` §2 (v2): uses `pabp_footprint` (defined only in §3) and `n`
  (left over from §1's loop). Raises `NameError`.
- `draft_polya` §5: `k_off_intr = ???` is a syntax error; `2*10^-6` is XOR in
  Python, not 2×10⁻⁶.

## Code that probably doesn't do what was meant

- `draft_polya` §1/§2: `G_tot_coated = ... - E_binding_all`, but `E_binding`
  is already negative, so binding is counted as a cost.
- `draft_polya` §1/§2: `h_pabp_polya`, `h_pabp_self`, `h_pap_mpsf` are computed
  but never used; the closing salt loop computes `l_p_*_salt` and discards it.
- `draft_polya` §3: the coated loop uses `e_bend_n` (naked) instead of
  `e_bend_c`; coated linear adds `h_pabp_polya` twice; naked linear includes
  PABP binding.
- `draft_polya` §3: `s_loop > s_lin`, i.e. closing a loop *gains* entropy.
- `main_for_urop` §1: `salt_concs` starts at 0 → divide by zero; axis says M
  but values run 0–300 (mM?); `r` is computed from `A` (the fit constant) and
  unused.

## Parameters to revisit

- `d_nt = 2.6 + 0.34/2` nm per nucleotide. ssRNA contour length is ~0.5–0.7 nm/nt.
- The constants disagree between sections: PABP footprint 12 vs. 11 nt; baseline
  l_p 2, 3, or 8 nm.
- The 250-nt crossing in §1 depends on three hand-set values. Varying one at a
  time (rest as written):

  | change | crossing (nt) |
  |---|---|
  | as written | 250 |
  | `stiff_pabp` 500 / 800 / 1200 / 2000 | 172 / 220 / 279 / 388 |
  | cooperativity coefficient 0 / 50 / 200 | 188 / 219 / 312 |
  | `d_nt` 2.0 / 3.0 nm | 351 / 230 |
  | `d_nt` 0.6–1.0 nm | no crossing |

- Salt: OSF electrostatic persistence length scales with λ_D², not λ_D.

## Repo

- `salt` (repo root) is a file containing only a newline. Left in place.
