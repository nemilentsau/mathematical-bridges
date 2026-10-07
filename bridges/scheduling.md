# Compress the history, then enumerate states

**Paper:** A Polynomial-Time Algorithm for Three-Machine Unit-Job Scheduling

[Full review](../reviews/scheduling.md) · [All bridges](README.md)

**Areas connected:** combinatorial optimization · structural normal forms

**Obstacle.** A recursive schedule interval inherits an ever-growing history of precedence constraints.

**Bridge.** Exchange arguments and precedence predicates reduce that history to bounded-size descriptions of job sets.

**What becomes manageable.** A polynomial collection of descriptors can serve as dynamic-programming states.

**Hinge to check.** The normal form must preserve globally feasible optimal witnesses through every recursive level.

**Reusable question.** Is an exponential search hard because the objects are complex, or because we have not proved how little a state needs to remember?

**Status:** Interpretation of the manuscript strategy; not proof verification or evidence of the model’s internal reasoning. See the linked review for provenance and scope.
