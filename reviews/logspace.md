# Exact derandomization of logarithmic space: L = RL = BPL

[All reviews](README.md) · [Quick bridge](../bridges/logspace.md) · [Pinned PDF](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/preprints/Exact-Derandomization-of-Logarithmic-Space-L-equals-RL-equals-BPL-September-23-2026/paper.pdf) · [Current PDF](https://github.com/openai/math/blob/main/preprints/Exact-Derandomization-of-Logarithmic-Space-L-equals-RL-equals-BPL-September-23-2026/paper.pdf)

- **Provenance:** Reconstructed from the current manuscript introduction and proof overview. The earlier conversation review text was unavailable; this is not a recovered transcript.
- **Compiled:** 2026-10-07. Historical review date not recorded.
- **Proof status:** Manuscript claims summarized; not independently verified.


## What the manuscript claims

The manuscript claims $\mathrm L=\mathrm{RL}=\mathrm{BPL}$. It also describes probability approximation to error $2^{-q}$ using $O(\log n+q)$ space and $n^{O(1)}2^{O(q)}$ time. Inverse-polynomial accuracy would therefore fit polynomial time and logarithmic space.

This concerns space-bounded computation. It does not establish $\mathrm{BPP}=\mathrm P$ for general randomized polynomial-time algorithms.

## The interesting move

A time-layered randomized computation becomes a substochastic matrix $S$. Because time advances, the relevant resolvent $(I-S)^{-1}$ represents a finite computation. A correction hierarchy transforms transition information while carrying rewards that preserve the desired probability.

The proposed compression uses a shared random environment with only $O(\log n)$ random bits, conditional rank retention, sparse sample tables, and compressed row estimates. Conditional averaging also brings in group-theoretic mixing, including finite-action consequences of property (T).

The decisive conversion to determinism is simple to state but demanding to implement: **a large majority of short seeds produce good estimates, and every seed—including a bad one—can be evaluated within the space bound and halts**. Enumeration and median selection can then remove randomness. The hard part is keeping all suspended work, counters, fingerprints, and recursive corrections within the same bound.

## Assessment

The bridge is from random computation to a compressible algebraic evaluation, followed by exhaustive processing of a short seed space. Small randomness alone is insufficient; the manuscript must make evaluation uniformly cheap even on unsuccessful seeds.

## What to scrutinize next

- Does reusing randomness introduce bias or correlations not covered by the analysis?
- Are all simultaneously live memory requirements included?
- Is termination and resource control genuinely worst-case over seeds?
- Is the construction uniform rather than dependent on uncomputed advice?

## Reading basis

Current manuscript: introduction, main guarantees, and proof-strategy overview (§1.2). The 108-page implementation and error analysis were not fully audited in this reconstruction.
