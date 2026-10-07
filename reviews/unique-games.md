# The Unique Games Theorem

[All reviews](README.md) · [Quick bridge](../bridges/unique-games.md) · [Pinned PDF](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/preprints/The-Unique-Games-Theorem-September-23-2026/paper.pdf) · [Current PDF](https://github.com/openai/math/blob/main/preprints/The-Unique-Games-Theorem-September-23-2026/paper.pdf)

- **Provenance:** Edited from a retained conversation review. Source identity checked at compilation.
- **Compiled:** 2026-10-07. Historical review date not recorded.
- **Proof status:** Manuscript claims summarized; not independently verified.


## What the manuscript claims

For every fixed $\varepsilon,\delta>0$, there is a finite alphabet and a deterministic polynomial-time reduction from 3SAT to explicit unweighted simple bipartite translation Unique Games instances, with completeness at least $1-\varepsilon$ and soundness at most $\delta$.

This is the Unique Games conjecture's hardness conclusion. It would have major approximation consequences under the usual complexity assumptions; it does not make Unique Games easy to solve or prove $\mathrm P\ne\mathrm{NP}$.

## The central bridge: stability that linear tests cannot imitate

An ordinary matrix shortcode $f_z(M)=Mz$ has limited stability under the elementary rank-one noise used in the starting comparison. The manuscript instead builds a nonlinear equivariant map $C:V\to K$ satisfying

$$C(x+k)=C(x)+k.$$

Its noise is designed to change $C(x)$ with arbitrarily small probability, while every sufficiently high-rank linear observation on $K$ still detects that noise with a fixed positive probability. The rank threshold is selected before the final label dimension.

The construction begins with quadratic blocks over a finite field and recursively perturbs a single leaf. Nonlinear stability improves with recursion depth. A harmonic rank potential and generic-subspace estimates are intended to stop the linear information from disappearing at the same time.

## How the bridge enters the hardness proof

High acceptance is converted, through Fourier analysis, into mass on low-restriction-rank characters. This feeds an ordinary matrix-shortcode acceptance statement and an existing Grassmann-expansion inverse theorem, yielding affine agreement on a bounded slice.

The remaining obstacle is dependence on the chosen advice. The construction separates the information used to select a witness from the private information used by the decoder. Sparse projections with density $\beta=k^{-2/3}$ simultaneously give $k\beta^2\to0$ and $k\beta\to\infty$: little overlap, but many usable coordinates. A conditional product structure then permits a parallel-repetition contradiction. A final repetition step drives soundness to the requested level.

## Assessment

This was our strongest example of a deliberately engineered intermediate object: preserve the nonlinear signal while ensuring the linear probes used in soundness analysis still register the noise. The two properties appear to pull in opposite directions, which makes their proposed coexistence the central insight to inspect.

The main route invokes established external expansion and repetition results. The separately discussed perfect 2-to-1 companion is not a premise of this route. None of this amounts to independent validation of the new gadget or the complete reduction.

## What to scrutinize next

- Does the rank potential remain effective at every recursion level?
- Is the rank threshold independent of the eventual label dimension in the needed order?
- Does witness selection avoid access to decoder-private randomness?
- Do conditioning and projection leave the exact product structure required by repetition?

## Reading basis

Retained conversation review: the gadget construction, substantial portions of soundness, and the final parameter order. Not every lemma or imported theorem application was independently audited. This file is an edited review, not a verbatim transcript.
