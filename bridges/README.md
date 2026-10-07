# Mathematical bridges

[Home](../README.md) · [Review index](../reviews/README.md)

These cards focus on the move that changes what must be proved or computed. “Bridge” describes our reading of a manuscript strategy; it does not establish novelty, correctness, or the model’s internal discovery process.

| Move | Areas connected | Paper review |
| --- | --- | --- |
| [Make noise part of the evaluator](sampling.md) | probability · analysis · oracle algorithms | [Subpolynomial query complexity for well-conditioned log-concave sampling](../reviews/sampling.md) |
| [Compress the history, then enumerate states](scheduling.md) | combinatorial optimization · structural normal forms | [A Polynomial-Time Algorithm for Three-Machine Unit-Job Scheduling](../reviews/scheduling.md) |
| [Separate shared blocks, then constrain their growth](matrix-multiplication.md) | tensor algebra · finite Fourier analysis · numerical invariants | [An Upper Bound of 9/4 for the Matrix Multiplication Exponent](../reviews/matrix-multiplication.md) |
| [Make every short seed safe to enumerate](logspace.md) | complexity theory · matrix algebra · group-based mixing | [Exact derandomization of logarithmic space: L = RL = BPL](../reviews/logspace.md) |
| [Measure information and energy through one construction](area-law.md) | quantum many-body theory · representation theory · information theory | [A two-dimensional area law from a global spectral gap](../reviews/area-law.md) |
| [Force two transforms to agree on one signal](quasi-riemann.md) | automorphic forms · analytic number theory · harmonic analysis | [The Quasi-Riemann Hypothesis: A Zero-Free Half-Plane Re s > 7/8](../reviews/quasi-riemann.md) |
| [Regularize while preserving the forbidden event](plane-coloring.md) | graph coloring · ergodic harmonic analysis · topology | [The Euclidean plane is not five-colorable](../reviews/plane-coloring.md) |
| [Exclude nonstandard escape routes by growth](hilbert-tenth.md) | logic · elliptic curves · local arithmetic · height geometry | [Hilbert’s tenth problem over the rational numbers](../reviews/hilbert-tenth.md) |
| [Preserve a nonlinear signal while linear probes stay sensitive](unique-games.md) | hardness of approximation · finite-field algebra · Fourier analysis | [The Unique Games Theorem](../reviews/unique-games.md) |
| [No shortcut would imply an impossible price](tensor-fourier.md) | linear circuits · convex duality · algebraic geometry · spectral constructions | [Finite tensor savings and exact Fourier circuits](../reviews/tensor-fourier.md) |

## Patterns worth comparing

- **Change the representation:** [scheduling](scheduling.md), [plane coloring](plane-coloring.md), and [area law](area-law.md) seek an intermediate object on which another tool becomes available.
- **Make two views disagree about an obstruction:** [quasi-Riemann](quasi-riemann.md), [Hilbert’s tenth](hilbert-tenth.md), and [tensor/Fourier](tensor-fourier.md) compare analytic signals, growth rates, or prices.
- **Engineer different responses to the same operation:** [Unique Games](unique-games.md) separates nonlinear stability from linear detectability; [sampling](sampling.md) makes controlled noise enable recursion.
- **Separate a finite mechanism from its asymptotic consequence:** [matrix multiplication](matrix-multiplication.md) and [tensor/Fourier](tensor-fourier.md) turn finite constructions into exponent constraints or savings.

These are editorial comparisons, not mathematical equivalences between the proofs.
