# A two-dimensional area law from a global spectral gap

[All reviews](README.md) · [Quick bridge](../bridges/area-law.md) · [Pinned PDF](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/preprints/A-two-dimensional-area-law-from-a-global-spectral-gap-September-24-2026/paper.pdf) · [Current PDF](https://github.com/openai/math/blob/main/preprints/A-two-dimensional-area-law-from-a-global-spectral-gap-September-24-2026/paper.pdf)

- **Provenance:** Reconstructed from the current manuscript introduction and proof overview. The earlier conversation review text was unavailable; this is not a recovered transcript.
- **Compiled:** 2026-10-07. Historical review date not recorded.
- **Proof status:** Manuscript claims summarized; not independently verified.


## What the manuscript claims

A finite-range Hamiltonian on a finite induced domain of the square lattice, with fixed local dimension and interaction bounds, a unique ground state, and a global spectral gap $\Delta$, obeys an entropy area law

$$S(A)\le C(q,R,J,\Delta)\,|\partial A|.$$

The claim does not assume a spectral gap for every restricted local Hamiltonian and allows frustration. The dependence on the global gap is essential.

## The interesting move

The manuscript first seeks quasi-local positive constraints that annihilate the ground state individually while retaining the useful force of the global gap. This creates a setting in which local operations can be compared with excitation energy without assuming local gaps.

It then uses symmetric replicas, Schur–Weyl structure, and de Finetti reasoning to encode information quantities through operator norms. A shared interpolation is intended to control both information gained and energy paid. Buffered regions and moving partitions translate that comparison into mutual-information estimates; localized contractions and entropy-chain cancellations strengthen the estimate to boundary scaling.

The key bridge is therefore **global energy control → information control → boundary entropy**. It is substantially more ambitious than inferring an area law from ordinary correlation decay alone.

## Assessment

The interesting aspect is the construction of an intermediate language in which a spectral statement and an entropic statement constrain the same process. The geometry of buffers and partitions is part of the argument, not merely bookkeeping.

A companion discussion of polynomial-bond-dimension PEPS existence would require its own analysis. An entropy bound alone does not provide an efficient procedure to construct or contract such a representation.

## What to scrutinize next

- Does replacing the Hamiltonian by quasi-local positive constraints retain a quantitative global gap?
- Are replica limits and approximation constants uniform in system size?
- Do the geometric and entropy cancellations work for every claimed region and boundary shape?

## Reading basis

Current manuscript: main claim, introductory discussion, and proof overview (§1.4). The analytic and geometric lemmas were not independently verified in this reconstruction.
