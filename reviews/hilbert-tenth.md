# Hilbert’s tenth problem over the rational numbers

[All reviews](README.md) · [Quick bridge](../bridges/hilbert-tenth.md) · [Pinned PDF](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/preprints/Hilberts-tenth-problem-over-the-rational-numbers-September-24-2026/main.pdf) · [Current PDF](https://github.com/openai/math/blob/main/preprints/Hilberts-tenth-problem-over-the-rational-numbers-September-24-2026/main.pdf)

- **Provenance:** Edited from a retained conversation review. Source identity checked at compilation.
- **Compiled:** 2026-10-07. Historical review date not recorded.
- **Proof status:** Manuscript claims summarized; not independently verified.


## What the manuscript claims

No algorithm decides whether an integer-coefficient polynomial in an arbitrary number of variables has a rational zero. The manuscript claims Turing degree $0'$ and a degree-at-most-four version with unbounded variable count.

The route does not establish an existential definition of $\mathbb Z$ inside $\mathbb Q$, and the stated reduction should not be silently strengthened to a many-one reduction from the halting problem.

## The interesting move

For an integer polynomial $f$, the construction supplies a computable sequence of finite rational-solvability tests with the proposed property:

$$f\text{ has an integer zero}\quad\Longleftrightarrow\quad\text{every test succeeds}.$$

With a hypothetical rational-solvability oracle, dovetailing an enumeration of integer roots with a search for a failing test would decide integer solvability. The familiar undecidability over the integers would then give a contradiction.

The difficult direction is why passing every test forces an ordinary integer root. Compactness first produces a ring inside a nonstandard rational field. A rank-one elliptic curve supplies integer-like indices through multiples of a point. The index map is additive and injective; multiplicativity is not assumed.

Local elliptic logarithm comparisons and an existential pole-parity condition force high-order congruences at contact primes. A five-point height estimate, together with additive-combinatorial constructions, then turns those local congruences into a global height restriction if the indexed tuple fails to solve $f$.

The contradiction uses two growth rates. The proposed restriction is linear in a size parameter, while elliptic multiples have quadratic canonical-height growth:

$$h(x(nP))=2\widehat h(P)n^2+O(1).$$

Applied across the constructed ring, this is intended to rule out the nonstandard escape route and force an ordinary integer solution.

## Why this stood out in our discussion

It changes what must be encoded. Instead of defining all integers existentially in the rationals, it builds enough finite tests and rigidity to prevent false nonstandard solutions. Geometry and height growth do work that one might initially expect from a direct logical definition.

## Dependencies and limits

The review identified essential reliance on companion claims concerning a pointwise 2-converse for elliptic curves with rational two-torsion and Fontaine–Mazur modularity at the prime 2. These enter the realization of local conditions and the height estimate. They are not automatically validated by reviewing this manuscript. A Goldfeld-style alternative was not treated as a necessary premise of the main route.

## What to scrutinize next

- Exactly which finite tests pass to the compactness model, and how are they effectively enumerated?
- Where does the height estimate obtain constants uniform enough for the contradiction?
- Does the local pole condition produce actual points under precisely the companion hypotheses used?
- Does the argument exclude every nonstandard case without tacitly assuming multiplication is preserved by the index map?

## Reading basis

Retained conversation review: reduction structure, local pole condition, height mechanism, and the final growth contradiction. The height estimate and companion results were not independently certified. This file is an edited review, not a verbatim transcript.
