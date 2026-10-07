# Make every short seed safe to enumerate

**Paper:** Exact derandomization of logarithmic space: L = RL = BPL

[Full review](../reviews/logspace.md) · [All bridges](README.md)

**Areas connected:** complexity theory · matrix algebra · group-based mixing

**Obstacle.** Randomized computation has a huge path space, and recursively evaluating approximations can exhaust memory.

**Bridge.** A correction hierarchy and compressed rows use a short shared random environment. Most seeds are accurate; every seed must halt within the same space limit.

**What becomes manageable.** Enumerating the short seed space and selecting a median removes randomness.

**Hinge to check.** Simultaneously live storage and bad-seed behavior, including dependencies introduced by shared randomness.

**Reusable question.** Can probabilistic success be converted to determinism by making failed trials cheap and total, not just by increasing the success probability?

**Status:** Interpretation of the manuscript strategy; not proof verification or evidence of the model’s internal reasoning. See the linked review for provenance and scope.
