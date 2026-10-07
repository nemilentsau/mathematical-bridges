# The Quasi-Riemann Hypothesis: A Zero-Free Half-Plane Re s > 7/8

[All reviews](README.md) · [Quick bridge](../bridges/quasi-riemann.md) · [Pinned PDF](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/preprints/The-Quasi-Riemann-Hypothesis-September-30-2026/paper.pdf) · [Current PDF](https://github.com/openai/math/blob/main/preprints/The-Quasi-Riemann-Hypothesis-September-30-2026/paper.pdf)

- **Provenance:** Reconstructed from the current manuscript introduction and proof overview. The earlier conversation review text was unavailable; this is not a recovered transcript.
- **Compiled:** 2026-10-07. Historical review date not recorded.
- **Proof status:** Manuscript claims summarized; not independently verified.


## What the manuscript claims

Every finite-order Hecke $L$-function over $\mathbb Q(\sqrt{-3})$, and every Dirichlet $L$-function including $\zeta$, has no zero in $\Re s>7/8$. A principal-character pole at $s=1$ is allowed. The boundary $7/8$ is excluded from the assertion.

This is a fixed zero-free half-plane, not the Riemann hypothesis, which puts nontrivial zeros on $\Re s=1/2$.

## The interesting move

The manuscript constructs a completed cubic-theta sum with two exact descriptions. **Reflection** supplies a direct size bound; **Poisson summation** exposes a principal term containing the reciprocal of the target $L$-function. If the same sum is small while accurately tracking that reciprocal, a Mellin-transform continuation principle can push the reciprocal across a common distance beyond the alleged rightmost zeros.

Completion matters: the full cubic factor is retained, and the target character acts on the complete product. On the Poisson side, nonprincipal rows introduce Hecke twists. Working with a whole family is necessary even if the ultimate target is only $\zeta$.

A balanced first stage claims a boundary of $11/12$. A second stage uses selected prime factors to compensate an unwanted Euler contribution, makes the averaging scales asymmetric, and combines two kinds of zero-detecting polynomial: one with Möbius coefficients and one without. Separate moment recursions control their joint occurrence, giving the stronger $7/8$ margin.

## Assessment

This is an example of designing an auxiliary object so two mathematical transforms make incompatible demands on a hypothetical obstruction. The bridge joins automorphic theta expansions, analytic continuation, large-sieve estimates, and moment recursions. The uniform positive exponent margin across target characters is a central requirement; fixed-character constants alone would not deliver the stated family-wide conclusion.

## What to scrutinize next

- Are principal residues nonzero and all nonunit/ramified restrictions preserved?
- Do transformed exceptional row families remain controlled inside both recursions?
- Are cancellation claims used only for the centered expressions where they hold?
- Are the continuation margins independent of the target character?

## Reading basis

Current manuscript: Theorem 1.1, proof overview, and the common-signal continuation formulation at the start of §2. The 199-page proof was not fully audited in this reconstruction.
