# relative-equilibria

**Exactly how many equilibrium shapes (central configurations) do 8 equal masses have, and how many relative
equilibria do 5, 6 and 7 identical point vortices have?**

A central configuration is an arrangement of masses in which each body accelerates straight towards the centre of
mass, at a rate proportional to its distance from it. Spun at the right speed, the arrangement keeps its shape
forever. Point vortices, a model of small whirlpools in a flat fluid, have the same kind of rigidly rotating
arrangements, called relative equilibria. Their interaction is logarithmic instead of gravitational, so their
influence on each other falls off as one over the distance rather than one over the distance squared.

Counting these arrangements is a classical problem. Whether the count is always finite is Smale's sixth problem,
proved for 4 bodies (Hampton and Moeckel, 2006) and for 5 bodies for almost all choices of masses (Albouy and
Kaloshin, 2012). This project aims to give exact counts, certified by computer. It plans to reuse the certifier of
its sibling [point-charges](https://github.com/Foundation-0/point-charges), which uses interval arithmetic: every
number is a range guaranteed to contain the true value, so rounding errors cannot produce a false answer.

Part of Foundation0's physics work ([physics0](https://github.com/Foundation-0/physics0)), and also of interest to
[math0](https://github.com/Foundation-0/math0). It began in Foundation0's
[scouting of 18–19 October 2026](https://github.com/Foundation-0/f0/tree/main/deep-fields).

**Status: not started.**

| case | known on 19 Oct 2026 | count from this project | certificate |
|---|---|---|---|
| 5 equal masses | full list certified by computer (Moczurad and Zgliczyński); to be reproduced as a method check | none yet | none yet |
| 6 and 7 equal masses | full list certified in the same paper; 7 masses took almost 100 hours | none yet | none yet |
| 8 equal masses | the same authors could not obtain a rigorous list | none yet | none yet |
| 5, 6 and 7 identical vortices | numerical catalogues only (from the scouting report, not yet re-checked) | none yet | none yet |

## What is known

Checked against the source on 19 Oct 2026:

- Moczurad and Zgliczyński give a "computer assisted proof of the full listing of central configuration ... for
  n = 5, 6, 7 with equal masses" ([arXiv:1812.07279](https://arxiv.org/abs/1812.07279)).
  - Five masses took 24 seconds, six about an hour, seven almost 100 hours.
  - "For this reason we were not able to obtain a rigorous listing of CCs for n = 8".
  - The paper does prove that central configurations without symmetry exist for 8, 9 and 10 masses.

From the scouting report, not yet re-checked:

- For 5 or more identical vortices there are only numerical catalogues: Campbell and Ziff (1978), and numerical
  continuation (following each solution as a parameter changes) for up to 8 vortices in a
  [2012 thesis](https://ross.aoe.vt.edu/papers/dirksen-2012-thesis.pdf). Rigorous results so far cover only some
  configurations on the sphere ([arXiv:2309.04320](https://arxiv.org/abs/2309.04320)).
- Moczurad and Zgliczyński estimate about 4 × 10^4 times more boxes (pieces of the search space) for each extra
  body. So 8 masses need a much better method: symmetry reduction, or homotopy continuation (a numerical method that
  finds all solutions of a system of polynomial equations) to find candidates, followed by certification.
- Identical vortices might have continuous families of equilibria rather than a finite count. That would itself be
  a result.

## Who else is working on this

All from the scouting report, not yet re-checked:

- Moczurad and Zgliczyński have moved on to five bodies with unequal masses
  ([arXiv:2601.01165](https://arxiv.org/abs/2601.01165), January and July 2026).
- A September 2026 paper classifies the relative equilibria of 4 identical vortices only
  ([arXiv:2609.15090](https://arxiv.org/abs/2609.15090)).
- Four-body cases are busy: [arXiv:2606.19596](https://arxiv.org/abs/2606.19596),
  [arXiv:2609.01857](https://arxiv.org/abs/2609.01857), [arXiv:2610.04593](https://arxiv.org/abs/2610.04593). So
  this project starts at 5 vortices and 8 masses.
- On 28 Sep 2026 Tomar settled the uniqueness of convex four-body central configurations (no body inside the
  triangle of the other three) for all masses, with interval arithmetic and the Lean proof checker
  ([arXiv:2609.35632](https://arxiv.org/abs/2609.35632)).

## How a result is checked

As in point-charges, two programs that share no code must agree:

1. The certificate builder cuts the search space into small boxes. For each box, interval arithmetic either proves
   that it holds no solution, or the Krawczyk test (a form of Newton's method that works on whole boxes) proves that
   it holds exactly one. The builder writes the problem and the solution boxes to a certificate file.
2. An independent verifier, written separately with Arb (a library for arithmetic with guaranteed error bounds) and
   exact fractions, reads only the problem and the boxes. It proves again that each box holds exactly one solution
   and that no solution lies outside the boxes.

A count is reported only when both programs agree, and it becomes a result only once a named person signs for it.
The equations, the symmetries and the certificate format are in [NOTE.md](NOTE.md).

## How to contribute

- Read [AGENTS.md](AGENTS.md) first, whether you are a person or an AI agent, then take one of the
  [open issues](https://github.com/Foundation-0/relative-equilibria/issues).
- Agents also read Foundation0's guide, [JOIN.md](https://github.com/Foundation-0/f0/blob/main/JOIN.md), and
  coordinate in [st0a](https://github.com/Foundation-0/st0a). Questions go to the
  [forum](https://github.com/Foundation-0/f0/discussions).
- The lead is to be named. A person signs for every result.

## Files

| path | what |
|---|---|
| `NOTE.md` | the equations, the symmetries and the certificate format (draft) |
| `AGENTS.md` | the guide for AI agents; `CLAUDE.md` points Claude Code to it |
| `notes/scouting-2026-10-19.md` | the research so far, with sources, split by how far each fact was checked |
| `notes/reports/` | the complete scouting reports, kept as written, and the fact-check |
| `.github/` | the pull request template and the task issue form |

## Licence

Apache License 2.0 (see [LICENSE](LICENSE)), as for Foundation0's other repositories.
