# What the box method delivers for 8, 9 and 10 equal masses

Dated 15 November 2026. Head read: `bf1e1ce` (status: not started). Verdict word for these results: **REPRODUCED**. Two programs were written
together and agree. The exact-rational verifier was re-run by a reviewer for 8 and 9 bodies. No third proof was written.
Marks: **[F]** fact checked by the programs in [`results/cc-equal-masses`](../results/cc-equal-masses/README.md), **[I]** inference.
Related issues: #1 (equations), #2 (certifier), #5 (literature), #6 (tell the Kraków group first).

## What is and is not proved

[F] For 8, 9 and 10 equal masses in the plane, at least 20, 42 and 67 classes of central configurations exist. Classes are counted up to rotation,
scaling, reflection and relabelling. Each class is proved to exist, to be the only solution in its box and to be non-degenerate. The classes are proved
different from one another. The Morse index and the exact order of the symmetry group of each class are proved too.

**Not proved: completeness, for any number of bodies above 7.** These are lower bounds. The lists match counts that were already published as numerical
results (Ferrario 2002 and Doicu, Zhao and Doicu 2022), so no new count is claimed. A complete proved list exists only for 5, 6 and 7 bodies
(Moczurad and Zgliczyński 2019).

| bodies | classes proved to exist | with no symmetry (order 1) | labelled count, up to rotation |
|---|---|---|---|
| 8 | at least 20 | 2 | 676,080 |
| 9 | at least 42 | 3 | 13,905,360 |
| 10 | at least 67 | 12 | 246,556,800 |

## The Morse identity

[F] With the proved indices h and symmetry orders s, the sum over classes of (-1)^h 2/s equals (-1)^n/(n(n-1)) exactly: 1/56 for 8 bodies,
-1/72 for 9 and 1/90 for 10. This is a check on each list. It cannot detect a missing pair of classes whose terms cancel.

## Match with Hampton's conjecture

[F] The counts of labelled solutions by Morse index equal Hampton's conjectured polynomials for 8 and 9 bodies (arXiv:1810.13011, Conjecture 5), term by term.
For 8 bodies the counts by index 0 to 6 are 5760, 40320, 161280, 216720, 151200, 80640 and 20160, which is 720(8 + 56t + 224t^2 + 301t^3 + 210t^4 + 112t^5 + 28t^6).
For 9 bodies they equal 5040(81 + 216t + 384t^2 + 732t^3 + 746t^4 + 396t^5 + 168t^6 + 36t^7).

[I] What follows. Every proved class is non-degenerate, and the counts already equal the conjectured polynomial. Any further non-degenerate class
would add a positive term to one coefficient. So for 8 bodies the conjecture holds exactly when the list of 20 is complete, and for 9 bodies exactly when the list of 42 is complete.
This turns a check on the lists into a statement about them. It does not prove either list complete.

## Three corrections to published tables

[F] Found by comparing the certificates with the tables of Ferrario 2002 (`compare_lit.py`). Each is "no earlier report found".

1. **9 bodies, one symmetry order.** The class with P = 89.80039 has symmetry order 2 in the certificate. Ferrario's table gives isotropy 1/2, which is order 1.
   Hampton had suspected this entry (arXiv:1810.13011).
2. **10 bodies, the regular decagon.** The entry of the 2002 table that is called the regular decagon (P = 122.14138716, isotropy 10) is a different
   configuration with symmetry order 4. The true regular decagon, with order 20 and Morse index 7, is a separate class at P = 122.14139026. It is missing from the table.
   One more class near it (P = 122.14138733, order 4) is missing too.
3. **10 bodies, classes with no symmetry.** The certificates give 12. Doicu, Zhao and Doicu say 11, and so does the appendix of Moczurad and Zgliczyński 2019.
   The twelfth, at P = 119.28941, is not in the 2002 table. [I] The count of 11 is probably a slip.

## A caution from 10 bodies

[F] About 1.1 million random starts never found the regular decagon. Only a search started near the regular polygon found it. A census that has stopped finding
new classes can still be missing one. The numerical census gave candidates. The proofs are the certificates.

## What a complete list would cost

[I] The published method needed 8.5 million CPU-seconds for 7 bodies, and its cost grows by about 200 times per added body. For 8 bodies that is 27 to 54 CPU-years
in the authors' compiled code. It was not attempted. Three things could lower it: ruling out clustered regions by formula (most boxes die there), larger boxes
(uniqueness holds here at radius 2^-12), and mirror symmetry inside the search.

## Sources, with the date they were read (15 November 2026)

* Moczurad and Zgliczyński, arXiv:1812.07279 (Celestial Mechanics and Dynamical Astronomy 131, 2019): complete proved lists for 5, 6 and 7 bodies, and the sentence that they could not obtain a rigorous list for 8.
* Ferrario, arXiv:math/0204198 (2002): numerical tables for 8, 9 and 10 bodies. Read from text extracted from the paper.
* Doicu, Zhao and Doicu, arXiv:2010.15358 (Celestial Mechanics and Dynamical Astronomy 134, 2022): numerical lists of 20, 42, 67, 114 and 191 classes for 8 to 12 bodies.
* Hampton, arXiv:1810.13011: Morse polynomials, Conjecture 5.

## Not verified

* Completeness, for any number of bodies above 7.
* The step that turns the Morse index of the potential into the number of positive eigenvalues of the reduced Jacobian is the reviewers' own derivation.
  It reproduces the published indices for 3 to 9 bodies. The Krawczyk theorem and Weyl's inequality are used as published, not re-proved.
* The literature counts were read from text extracted from the papers.

## For the Kraków group (issue #6)

Nothing in this repository is to be published as a count before a named person has written to Moczurad and Zgliczyński. This note and the folder are a branch for review.
