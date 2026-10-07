# Finite tensor savings and exact Fourier circuits

[All reviews](README.md) · [Quick bridge](../bridges/tensor-fourier.md) · [Pinned PDF](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/preprints/Finite-tensor-savings-and-exact-Fourier-circuits-September-25-2026/main.pdf) · [Current PDF](https://github.com/openai/math/blob/main/preprints/Finite-tensor-savings-and-exact-Fourier-circuits-September-25-2026/main.pdf)

- **Provenance:** Edited from a retained conversation review. Source identity checked at compilation.
- **Compiled:** 2026-10-07. Historical review date not recorded.
- **Proof status:** Manuscript claims summarized; not independently verified.


## What the manuscript claims

For exact unrestricted complex linear circuits, counting every addition, subtraction, and scalar multiplication, the manuscript claims

$$\liminf_{n\to\infty}\frac{L(n)}{n\log_2 n}=0.$$

The result is along an unbounded sequence of lengths, constructed from products of distinct primes. Coefficients may be arbitrary prechosen complex numbers; producing or representing those coefficients is not charged. This is nonuniform exact arithmetic, with no general stability or bit-complexity guarantee. An all-length result belongs to a separate discussion, not this review.

## Move 1: turn a finite win into an asymptotic improvement

For an invertible nonmonomial $q\times q$ matrix $A$, the intermediate task is to implement $A^{\otimes b}$ with fewer than $bq^{b-1}$ calls to $A$. Permutations and invertible diagonals are free only in this intermediate comparison.

A recursive construction amplifies such a finite saving. After normalization, its cost is controlled by a recurrence with a binomially distributed subproblem size; strict savings permit an exponent $\alpha<1$. The resulting bound has the form $Cq^k(k+1)^\alpha$. The final circuit accounting restores the costs of scalar operations.

Transfer to Fourier transforms uses exact factorization, a fixed call pattern able to realize general invertible matrices with adjustable monomial operations, and prime-factor tensor decompositions. Borrowed coordinates are restored after use, keeping the width exact rather than silently enlarging the problem.

## Move 2: prove a finite win exists without exhibiting it

Assume there is no such saving. Packing finite comparison programs, convex separation, and compactness are then intended to produce a universal numerical price on invertible matrices. It is additive on direct sums, has a dimension-weighted tensor law, is subadditive under composition, and vanishes exactly on monomial matrices.

The proof develops feedback and algebraic-specialization rules for this price; continuity cannot simply be assumed. It then constructs an orthogonal reflection with incompatible price estimates. A structured tensor construction forces a lower price, while a sparse realization of its defining subspace yields a cheaper upper price.

In the review's notation, the comparison is

$$ (d-4)w\le p(R)\le(3d/4+7/2)w,$$

which is contradictory for $d>30$. Therefore the putative universal price cannot exist, so some finite saving must exist.

## Assessment

The title-based expectation of a finite-to-asymptotic amplification mechanism was confirmed by the described proof. The more surprising move is the existence argument: **failure of every shortcut would force a global invariant, and a carefully engineered reflection makes that invariant impossible**.

This does not hand us a concrete fast Fourier implementation. The finite witness is existential, the arithmetic model is permissive, and the length guarantee is a liminf. Those limits matter to the theorem's interpretation but do not diminish the conceptual interest of the bridge.

## What to scrutinize next

- Does the packing/separation argument really yield every asserted price law?
- Are feedback and specialization justified without illicit continuity?
- Do both reflection estimates use exactly the same accounting rules?
- Are intermediate free operations fully charged during amplification and Fourier transfer?

## Reading basis

Retained conversation review: amplification, Fourier transfer, the price axioms, feedback/specialization, and the reflection contradiction. The packing proof and every supporting lemma were not independently audited. This file is an edited review, not a verbatim transcript.
