# Central configurations and vortex relative equilibria: equations, symmetries, certificates

*Draft written on 19 October 2026 by Claude (an AI model by Anthropic) when this repository was set up. Not checked
by a person. Nothing here has been computed yet. Checking and completing Sections 1 to 3 is the first open issue.*

## 1. The equations

Put $n$ bodies in the plane at positions $q_1,\dots,q_n \in \mathbb{R}^2$, with weights $m_i>0$. The weights are
masses for gravity and circulations (the strength and direction of spin) for vortices. This project uses $m_i=1$
throughout. Write $r_{ij}=|q_i-q_j|$, $M=\sum_i m_i$, and $c=\frac1M\sum_i m_iq_i$ for the centre of mass.

Fix an exponent $a\ge 0$ and let

$$U_a(q)=\sum_{i<j} m_im_j\,\varphi_a(r_{ij}),\qquad \varphi_a(r)=\frac{r^{-a}}{a}\ (a>0),\qquad \varphi_0(r)=-\log r .$$

$a=1$ is Newtonian gravity. $a=0$ is the logarithmic interaction of point vortices. For every $a\ge0$,
$\varphi_a'(r)=-r^{-a-1}$, so the forces have the same form for all exponents.

A configuration without collisions is a **central configuration** (for vortices, a **relative equilibrium**) when
there is a number $\lambda$ with

$$F_i(q):=\sum_{j\ne i} m_j\,\frac{q_i-q_j}{r_{ij}^{\,a+2}}-\lambda\,(q_i-c)=0,\qquad i=1,\dots,n. \tag{1}$$

Taking the dot product of (1) with $m_i(q_i-c)$ and summing over $i$ gives

$$\lambda\, I=\sum_{i<j} m_im_j\,r_{ij}^{-a},\qquad I=\sum_i m_i|q_i-c|^2,$$

so $\lambda>0$ for every solution.

**Why (1) gives rigid motion.**

- For gravity ($a=1$), give each body the velocity $\omega J(q_i-c)$, where $J$ turns a vector by 90 degrees and
  $\omega^2=\lambda$. The configuration then rotates rigidly about $c$.
- For vortices ($a=0$), the velocity of vortex $i$ is a fixed multiple of $J\sum_{j\ne i}m_j(q_i-q_j)/r_{ij}^2$.
  By (1) this equals a multiple of $J(q_i-c)$, so the vortices rotate rigidly about $c$.

**As critical points.** The solutions of (1) are the critical points of $U_a$ on the set of configurations with
$c=0$ and $I=1$. This is the usual Lagrange-multiplier argument, and it holds for every $a\ge0$.

## 2. Symmetries and what is counted

If $q$ solves (1), so do:

| symmetry | new solution |
|---|---|
| translation | $q_i+v$ (the centre of mass moves with it) |
| rotation and reflection | $Rq_i$ with $R$ in $O(2)$ |
| scaling | $sq_i$, with $\lambda$ replaced by $s^{-(a+2)}\lambda$ |
| relabelling | $q_{\sigma(i)}$ for a permutation $\sigma$ of bodies with equal weights (here, all of them) |

Published counts use different conventions. Each certificate should give two numbers:

- $N_{\text{classes}}$: solutions up to all four symmetries, counting mirror images and relabellings as the same.
- $N_{\text{labelled}}$: labelled solutions up to translation, rotation and scaling, with mirror images counted
  separately.

Reflection and relabelling together form the group $\mathbb{Z}_2\times S_n$, of order $2\,n!$. It acts on labelled
solutions. The symmetry group (stabiliser) of a solution is the subgroup that maps it to itself, up to translation,
rotation and scaling. All solutions in class $k$ have symmetry groups of the same order $s_k$, and the class
contains $2\,n!/s_k$ labelled solutions, so

$$N_{\text{labelled}}=\sum_{k=1}^{N_{\text{classes}}}\frac{2\,n!}{s_k}.$$

This identity is a consistency check between the two counts. For a regular $n$-gon, $s_k=2n$ and the class holds
$(n-1)!$ labelled solutions. Collinear configurations are planar central configurations too and must be counted.

## 3. The reduced system to certify (to be completed)

The equations (1) satisfy three identities for every configuration, whatever $\lambda$ is:

$$\sum_i m_iF_i=0\quad\text{(two components)},\qquad \sum_i m_i\,q_i\times F_i=0\quad\text{(one component)},$$

where $u\times v=u_1v_2-u_2v_1$. Fix the translation ($c=0$), the scale ($\lambda=1$, or $I=1$) and the rotation.
That leaves $2n-3$ unknowns, and only $2n-3$ of the $2n$ equations are independent, so the reduced system is
square. Its solutions must be isolated and non-degenerate (the derivative is invertible) for the Krawczyk test to
apply.

Open points for the first issue:

1. **Which equations to drop.** Dropping both components of $F_n$ is always safe, because $m_n>0$ in the first
   identity. Combining the two identities then gives $\sum_{i<n} m_i\,(q_i-q_n)\times F_i=0$. Dropping one
   component of some $F_k$ through it is safe only where the other coordinate of $q_k-q_n$ cannot vanish, so that
   coordinate must stay away from zero in the search region.
2. **How to fix the rotation** so that every labelled solution is met exactly once.
3. **A compact search region.** This needs a lower bound on the distance between any two bodies in a solution and
   an upper bound on the size once the scale is fixed, both as functions of $a$. Point-charges met the same problem
   with the convex hull of the charges and a test that one charge dominates the field near its site.
4. **Symmetry reduction for speed.** Searching only part of the region, for example configurations whose labels
   are in a fixed order, cuts the work by up to a factor $2\,n!$. The certificate must then show that the part
   searched meets every class.
5. **The vortex case.** If identical vortices have continuous families of solutions, the Krawczyk test cannot pass
   on them, and boxes along a family will neither be excluded nor certified. Such a family needs a different
   proof, and would itself be a result.

## 4. Certificate format (draft)

Modelled on the certificates of [point-charges](https://github.com/Foundation-0/point-charges): one JSON file per
case in `certificates/`, for example `cc-a1-n5.json` for gravity with 5 equal masses, or `vortex-n5.json`.

| field | content |
|---|---|
| `name` | the case, such as `cc-a1-n5` |
| `claim` | the statement in words, such as "(1) with $a=1$ and five unit weights has exactly $N$ classes of solutions, all non-degenerate" |
| `exponent`, `weights` | exact rationals, written as strings |
| `normalisation` | how translation, rotation and scale are fixed, and which three equations are dropped |
| `region` | the search region, and the bounds that show it contains every solution |
| `reduction` | the part of the region searched, if symmetry is used, and why it meets every class |
| `count_classes`, `count_labelled` | the two counts of Section 2 |
| `solutions` | for each solution: the box, a tight enclosure inside it (a much smaller box known to hold the solution), the order of its symmetry group, and its class |
| `stats` | boxes examined, boxes excluded by each test, boxes passed to the Krawczyk test |
| `tools` | program and library versions, hardware and run time |

**Primary certifier.** Adapted from point-charges' `certify.py` and `ia.py`: float64 intervals rounded outward,
bisection of the region, exclusion of boxes where some equation cannot vanish, and the Krawczyk test on the rest.
For a box $X$ with centre $x_0$, an approximate inverse $C$ of the derivative at $x_0$ and an interval enclosure
$DF(X)$ of the derivative on $X$, the Krawczyk operator is

$$K(X)=x_0-C\,F(x_0)+\bigl(I-C\,DF(X)\bigr)(X-x_0).$$

If $K(X)$ lies inside the interior of $X$, then $X$ holds exactly one solution, and the derivative is invertible
there.

**Independent verifier.** Adapted from point-charges' `verify_arb.py`, sharing no code with the certifier: Arb
balls from python-flint (each number stored as a midpoint and a guaranteed error radius) for the equations and
their derivative, exact rationals for box geometry. It reads only
`exponent`, `weights`, `normalisation`, `region`, `reduction` and the solution boxes, and then:

1. re-proves each solution box with its own Krawczyk test;
2. checks that the tight enclosures are pairwise disjoint, so the solutions are distinct;
3. re-derives the class of each solution and the order of its symmetry group, and checks the identity of Section 2;
4. runs its own bisection of the region and discards every box by its own exclusion tests or by containment in a
   verified solution box. This proves that there are no other solutions.

A count is reported only when both programs accept the certificate.

**Other tools** named in the scouting report: IntervalArithmetic.jl, HomotopyContinuation.jl and the CAPD library.
