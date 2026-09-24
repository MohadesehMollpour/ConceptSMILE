# Submission readiness scope

The authoritative repository status is documented in
[FINAL_REPOSITORY_STATUS.md](FINAL_REPOSITORY_STATUS.md).

The current repository status is **AMBER** for a transparent, limited research
release. This status reflects remaining gaps in complete end-to-end experimental
reproducibility and result provenance; it is not a certification that all manuscript
results have been independently reproduced.

The detailed scientific and provenance review is recorded in:

`docs/audits/final-scientific-audit.md`

The original repository audit used commit:

`83a10462036a7b8de7ce356cf617a98d67357131`

as a historical comparison baseline.

The live GitHub repository has since been updated through explicit commits covering
documentation, metadata, manuscript alignment, reusable software, tests, validation,
and provenance records.

The current reusable software package has passed GitHub Actions validation under
Python 3.10 and Python 3.11, including:

- package installation;
- Ruff checks;
- 33 unit tests;
- the synthetic smoke test;
- validation of `configs/paper.yaml`; and
- package build.

These software checks do not constitute a rerun of the complete four-dataset retinal
experiments reported in the manuscript.

No repository visibility change or Git-history rewrite is implied by these updates.
Historical repository content and provenance limitations remain documented separately.

For scientific interpretation, manuscript-transcribed tables, preserved historical
notebooks, reconstructed utilities, and any future verified reruns must continue to be
treated as distinct evidence categories.
