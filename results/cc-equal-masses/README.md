# Equal masses in the plane: 8, 9 and 10 bodies, existence certificates

Status of every result here: **claimed**, with the verdict word REPRODUCED. Two programs were written together and agree. The
exact-rational verifier was re-run by a reviewer for 8 and 9 bodies. No third proof was written.

This is a set of existence results for lists that were already published as numerical results (Ferrario 2002, Doicu, Zhao and Doicu 2022).
**It claims no new count.** Completeness is not proved for any number of bodies above 7.

## What is and is not proved

Proved, for 8, 9 and 10 equal masses, with the equations of `NOTE.md` Section 3 (exponent a = 1):

* the lists have at least 20, 42 and 67 classes (up to rotation, scaling, reflection and relabelling);
* each class exists, is the only solution in its box, and is non-degenerate (the Jacobian of the reduced system is invertible);
* the classes are pairwise different (the enclosures of the moment of inertia are disjoint);
* the Morse index and the exact order of the symmetry group of each class.

With these, the lists satisfy the Morse identity exactly: the sum over classes of (-1)^h 2/s equals (-1)^n/(n(n-1)), that is 1/56, -1/72 and 1/90.

Not proved: that there are no further classes, for any n above 7. The number of boxes a complete search needs for 8 bodies is
estimated, not run (see `notes/box-method-2026-11-15.md`).

## Files

| path | what |
|---|---|
| `../../certificates/cc-a1-n8.json`, `cc-a1-n9.json`, `cc-a1-n10.json` | the certificates. Named as in `NOTE.md` Section 4. The fields are those of the certifier, listed below. |
| `cert_arb.py` | certifier: Krawczyk test in Arb ball arithmetic (`python-flint`), Morse index, symmetry order, distinctness |
| `verify_rational.py` | separate verifier: exact rational interval arithmetic, standard `fractions` plus `numpy` for the preconditioner. Shares no code with `cert_arb.py`. |
| `census.py`, `merge_census.py`, `census_stats.py` | floating-point census of candidates (finds candidates only, proves nothing) |
| `candidates/merged_n{8,9,10}.json` | the merged candidate lists that `cert_arb.py` reads |
| `compare_lit.py` | compares a certificate with a table of Ferrario 2002 (arXiv math/0204198). The table is not stored here. Save the paper text yourself and pass its path. |
| `spot_cc.py` | high-precision numerical spot check of the equations (not a proof) |
| `corrupt_tests.sh`, `run_all.sh` | the corruption tests and the replay of stages 2 to 4 |
| `outputs/` | saved outputs of every command below, and `merge_n*.out` (which census runs found each candidate) |
| `SHA256SUMS` | checksums of every file in this folder and of the three certificates |

Certificate fields: `n`, `lambda`, `masses`, `normalisation`, `coordinate_order`, `centre_scale_exp2`, `box_radius_exp2`, `labelled_count`,
`morse_sum`, and for each class `pinned_body`, `centre_num` (the box centre, as integers over 2^centre_scale_exp2), `I_enclosure`, `P_enclosure`,
`morse_index`, `sym_order` and `uniqueness_radius_exp2`. The verifier reads only `n`, the two exponents, the pinned body and the centre of each class.
Mapping to `NOTE.md` Section 4: `count_classes` is the number of entries in `classes`, and `count_labelled` is `labelled_count`.
The fields `region`, `reduction` and `stats` of that draft do not exist, because nothing was searched: the certificates prove existence only.

## Check it yourself

From the repository root. Python 3.13 with numpy 2.3 and python-flint 0.9 was used.

```
python3 -I -O results/cc-equal-masses/verify_rational.py certificates/cc-a1-n8.json     # a few seconds
python3 -I -O results/cc-equal-masses/verify_rational.py certificates/cc-a1-n9.json
python3 -I -O results/cc-equal-masses/verify_rational.py certificates/cc-a1-n10.json
sh results/cc-equal-masses/run_all.sh          # rebuilds each certificate with Arb, compares byte for byte, runs the verifier, the spot check
sh results/cc-equal-masses/corrupt_tests.sh    # 15 corrupted inputs, each must print FAIL or REJECT, also under -O
shasum -a 256 -c results/cc-equal-masses/SHA256SUMS      # from inside results/cc-equal-masses
```

Each verifier run ends with `ACCEPT: n = ...` or `REJECT: ...` and an exit code. A rejection raises an error. There is no bare `assert`
in any proof step, so `-O` changes nothing. Saved outputs: `outputs/verify_rational_n{8,9,10}.out` and `outputs/verify_rational_n{8,9,10}_O.out`,
`outputs/cert_arb_n{8,9,10}.out`, `outputs/corrupt_tests.out`, `outputs/spot_cc.out`.

## How it is checked, in short

The reduced system is the one in `NOTE.md` Section 3.1. For each candidate the certifier builds a box of radius 2^-30 around a dyadic centre.
The Krawczyk operator K(X) = x0 - C G(x0) + (I - C DG(X))(X - x0) must lie strictly inside X. Then X holds exactly one zero of G and
DG is invertible on X. The verifier repeats this in exact rational arithmetic with its own preconditioner and its own outward-rounded bound for r^-1.
The Morse index is the number of positive eigenvalues of DG at the zero (a congruence and Gershgorin discs in Arb, an exact LDL^T inertia
and Weyl's inequality in the rational program). The symmetry order is proved by testing every permutation and reflection that survives a
distance test: an image that lands in the box is a symmetry, an image outside the tight enclosure is not, and an undecided case is a failure.

## What the numerical census does not show

For 8 and 9 bodies every census run found the same 20 and 42 classes. For 10 bodies about 1.1 million random starts never found the regular
decagon. Only a search started near the regular polygon found it. A census that stops finding new classes can still miss one. It is evidence, not proof.
