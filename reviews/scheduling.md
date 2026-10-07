# A Polynomial-Time Algorithm for Three-Machine Unit-Job Scheduling

[All reviews](README.md) · [Quick bridge](../bridges/scheduling.md) · [Pinned PDF](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/preprints/A-polynomial-time-algorithm-for-three-machine-unit-job-scheduling-September-24-2026/paper.pdf) · [Current PDF](https://github.com/openai/math/blob/main/preprints/A-polynomial-time-algorithm-for-three-machine-unit-job-scheduling-September-24-2026/paper.pdf)

- **Provenance:** Reconstructed from the current manuscript introduction and proof overview. The earlier conversation review text was unavailable; this is not a recovered transcript.
- **Compiled:** 2026-10-07. Historical review date not recorded.
- **Proof status:** Manuscript claims summarized; not independently verified.


## What the manuscript claims

An exact, uniform polynomial-time algorithm minimizes makespan for unit-duration, nonpreemptive jobs with arbitrary precedence constraints on three identical machines. This is the classical model without extra release-time or machine-eligibility constraints.

The explicit deterministic Turing-machine bound is $O((L+2)^{150020})$, where $L$ is the input length. The result concerns the polynomial-time classification; this bound offers no immediate practical scheduling algorithm.

## The interesting move

Dynamic programming needs a small description of the jobs assigned to an interval. Two boundary triples alone do not determine that set, while recording the whole recursive history would create too many states.

The proposed solution is a **normal form for inherited constraints**. Padding with isolated jobs allows three-job time slots. Separator triples divide a schedule into gaps. Precedence predicates, priority cutoffs, and exchange invariants compress the conditions inherited from earlier separators into bounded-size Boolean descriptions, independent of recursion depth.

Once this compression is available, the algorithm can enumerate descriptions rather than schedules. Lexicographically selected witness schedules help prove that a suitable description exists; the algorithm is not assumed to know those witnesses.

## Assessment

The conceptual move is to find the right state space. The difficult object remains globally constrained, but the manuscript claims that all information needed for recursive optimization has a bounded descriptive form. This is a useful pattern to watch for in other algorithms: the breakthrough may be a theorem about what a state must remember.

## What to scrutinize next

- Does the normalization preserve every necessary global constraint, rather than only local boundary compatibility?
- Do exchange operations retain a representative of an optimal schedule?
- Does the descriptor bound survive repeated recursion and reversals of direction?

## Reading basis

Current manuscript: introduction, algorithm overview, and the descriptions of interval states and normalization. This reconstruction does not verify the normalization lemmas or the full dynamic program.
