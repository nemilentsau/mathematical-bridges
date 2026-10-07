# An Upper Bound of 9/4 for the Matrix Multiplication Exponent

[All reviews](README.md) · [Quick bridge](../bridges/matrix-multiplication.md) · [Pinned PDF](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/preprints/Matrix-Multiplication-Nine-Fourths-October-2-2026/paper.pdf) · [Current PDF](https://github.com/openai/math/blob/main/preprints/Matrix-Multiplication-Nine-Fourths-October-2-2026/paper.pdf)

- **Provenance:** Reconstructed from the current manuscript introduction and proof overview. The earlier conversation review text was unavailable; this is not a recovered transcript.
- **Compiled:** 2026-10-07. Historical review date not recorded.
- **Proof status:** Manuscript claims summarized; not independently verified.


## What the manuscript claims

The matrix multiplication exponent over $\mathbb C$ satisfies $\omega\le9/4$. In the usual asymptotic interpretation, this yields $O_\varepsilon(n^{9/4+\varepsilon})$ arithmetic operations for every fixed positive $\varepsilon$. It is not a claim of competitive performance at a specified matrix size.

The source recorded here is the October 2 manuscript. The exact revision used in the earlier conversation cannot be recovered.

## The interesting move

Tensor blocks that share variables cannot simply be treated as an independent direct sum. The manuscript proposes to separate blocks that are already independent on two tensor legs but share the third.

Finite Fourier projections label the shared leg. A degeneration weighted by the **square of a label mismatch** is designed to retain exactly the matching blocks. The cost of an auxiliary dot-product factor must then be accounted for on the relevant exponential scale.

The second bridge turns tensor operations into inequalities for numerical characters and a normalized two-parameter profile $P(a,b)$. Direct-sum and tensor-product behavior, interpolation, monotonicity of increments, and a three-sector growth inequality constrain this profile. The proposed lower growth $P(a,a)\ge a^{4/3}$ forces the exponent parameter into the range yielding $9/4$.

## Assessment

The interesting combination is label-based separation followed by an obstruction expressed through a numerical invariant. A constructive tensor manipulation feeds an abstract growth argument. This is related in spirit to the later Fourier-circuit paper's search for impossible invariants, although the invariants and computational models differ.

## What to scrutinize next

- Does the degeneration isolate exactly the advertised summands?
- Is every auxiliary factor included in the asymptotic cost?
- Does the detecting-character argument justify all profile properties used in the final growth step?

## Reading basis

Current manuscript: opening theorem, introduction, and proof outline. The appendix and full character/separation arguments were not independently checked in this reconstruction.
