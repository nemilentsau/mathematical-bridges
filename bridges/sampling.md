# Make noise part of the evaluator

**Paper:** Subpolynomial query complexity for well-conditioned log-concave sampling

[Full review](../reviews/sampling.md) · [All bridges](README.md)

**Areas connected:** probability · analysis · oracle algorithms

**Obstacle.** High-order transports call conditional means whose centers are themselves uncertain.

**Bridge.** Gaussian conditioning supplies smoothness, and a translation/covariance identity absorbs center uncertainty into random seeds. Sampling and mean estimation become mutually recursive finite-query procedures.

**What becomes manageable.** A formally nested transport can be implemented using the original gradient oracle; later conditioning removes the auxiliary noise.

**Hinge to check.** Correct joint laws and finite recursion with the claimed dimension dependence.

**Reusable question.** Can controlled randomness make a recursive subroutine composable, rather than merely make its output approximate?

**Status:** Interpretation of the manuscript strategy; not proof verification or evidence of the model’s internal reasoning. See the linked review for provenance and scope.
