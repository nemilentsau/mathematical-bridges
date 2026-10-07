# Mathematical Bridges

A reading notebook for manuscripts in [openai/math](https://github.com/openai/math), focused on **interesting mathematical moves**: changes of representation, intermediate objects, reductions, rigidity arguments, and connections between fields.

The conversation began by asking about practical applications, then shifted to a more useful reading question: **what bridge makes the difficult step approachable, and where does that bridge need the most scrutiny?** This repository preserves that focus.

## Start here

- [Paper reviews](reviews/README.md): 10 substantive entries, including claims, mechanisms, limits, and follow-up questions.
- [Quick bridge insights](bridges/README.md): 10 short companion cards, separate from the reviews.
- [Reading queue](reading-queue.md): 9 unread papers from the latest title-based shortlist.
- [Review method and provenance](REVIEW_METHOD.md): what the notes do and do not establish.
- [Source manifest](sources/manifest.json): pinned upstream revision, PDF hashes, and source identities.

The three most developed retained reviews are [Hilbert’s tenth over the rationals](reviews/hilbert-tenth.md), [Unique Games](reviews/unique-games.md), and [finite tensor savings / Fourier circuits](reviews/tensor-fourier.md).

## Status at creation

Compiled on **2026-10-07**. Seven earlier review texts could not be recovered; their entries are explicitly **reconstructed from manuscript introductions and proof overviews**. Three entries are edited from retained conversation reviews. This is not a verbatim conversation archive.

The notes report manuscript claims and interpret proof strategies. **No entry is an independent verification of the claimed theorem.** “Model-built bridge” is shorthand for a construction described in the manuscript, not evidence about the model’s private reasoning or a verified claim of novelty.

An early reference to “number 2” could not be identified from the available record. It has not been assigned a paper or fabricated review. The later ten-paper shortlist is separately preserved in the reading queue.

## Keeping it going

Use the [review template](templates/review.md) and [bridge template](templates/bridge.md), then follow [CONTRIBUTING.md](CONTRIBUTING.md). [catalog.json](catalog.json) contains the machine-readable index. [CHANGELOG.md](CHANGELOG.md) records substantive changes.

This download is an initialized Git repository with an initial commit. It has no remote and has not been published to GitHub. After extracting it, inspect it with:

```sh
cd mathematical-bridges
git status
git log --oneline
python3 tools/check_repo.py
```

The repository contains original review notes and source links. It does not redistribute the paper PDFs or claim ownership of those manuscripts.
