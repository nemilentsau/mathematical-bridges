# Subpolynomial query complexity for well-conditioned log-concave sampling

[All reviews](README.md) · [Quick bridge](../bridges/sampling.md) · [Pinned PDF](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/preprints/Subpolynomial-query-complexity-for-well-conditioned-log-concave-sampling-September-26-2026/article.pdf) · [Current PDF](https://github.com/openai/math/blob/main/preprints/Subpolynomial-query-complexity-for-well-conditioned-log-concave-sampling-September-26-2026/article.pdf)

- **Provenance:** Reconstructed from the current manuscript introduction and proof overview. The earlier conversation review text was unavailable; this is not a recovered transcript.
- **Compiled:** 2026-10-07. Historical review date not recorded.
- **Proof status:** Manuscript claims summarized; not independently verified.


## What the manuscript claims

For every fixed $\varepsilon>0$, sampling in dimension $d$ takes at most $C_\varepsilon d^\varepsilon$ exact first-order oracle queries on every execution. The target has density proportional to $e^{-V}$, a known minimizer, and $I\preceq\nabla^2 V\preceq2I$; the stated total-variation accuracy is $1/10$. An independent lower bound is $\Omega(\log d)$.

This is a query-complexity result. Arbitrary real computation between queries is outside the cost measure. It does not supply a polylogarithmic query bound or an efficient finite-precision implementation.

## The interesting move

Gaussian conditioning changes the task into sampling a nearly quadratic distribution. The paper then builds **sampling and conditional-mean estimation together**: the velocity of a Gaussian transport is itself a conditional gradient mean, so the two tasks can call each other.

The crucial device is deliberate noise. A pathwise translation identity shifts Gaussian seeds to compensate for an unknown center, and a covariance transformation absorbs noise in that center. This is intended to turn nested, seemingly inaccessible mean evaluations into finitely many actual gradient queries. Noise becomes an ingredient of the computation.

High derivatives come from Gaussian conditioning even though $V$ itself is only $C^2$. Bounds on every matrix flattening of the resulting derivative tensors control the contractions used in high-order approximations. Finally, repeated conditioning removes the added Gaussian noise to reach the original target in total variation.

## Assessment

The compelling bridge is between probability-flow constructions, tensor derivative estimates, and exact transformations of random seeds. The title's promise of low query complexity is supported by a specific proposed mechanism; a claim of immediate practical speed would go beyond it.

## What to scrutinize next

- Does the seed transformation implement every nested call with the required joint law?
- Are both recursion depths bounded before choosing the numerical mesh?
- Do the high-order estimates and final removal of noise preserve the advertised dimension exponent?

## Reading basis

Current manuscript: Theorem 1.1, introduction and proof strategy (§1.3), and the auxiliary sampling formulation in §2. Full technical proofs were not audited in this reconstruction.
