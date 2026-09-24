# Repository changelog

This document records the principal repository changes made during the ConceptSMILE
submission-readiness and reproducibility review.

The original repository audit used commit:

`83a10462036a7b8de7ce356cf617a98d67357131`

as a historical comparison baseline.

An earlier main-repository reference was:

`bac08af5df086aea20eb81872f1e1cb2cc5fde39`

These commits are retained as historical references only. The live GitHub repository
has subsequently been updated through explicit commits and should not be described as
an unchanged local package.

## Repository-alignment changes

The repository has been updated to improve alignment with the current ConceptSMILE
manuscript while preserving uncertainty where original experimental evidence is
unavailable.

Principal changes include:

- documented the author-confirmed 40-image evaluation subset in
  `data/manifests/paper_40_images.csv`;
- aligned `configs/paper.yaml` with the current reviewed manuscript and its verified
  manuscript hash;
- retained unknown experimental settings as `null` rather than inferring them from
  historical notebooks;
- updated dataset and reproducibility documentation;
- completed repository author metadata in `CITATION.cff` and `pyproject.toml`;
- retained manuscript-transcribed Tables 2–7 as explicitly labelled transcription
  records rather than presenting them as regenerated experimental outputs;
- retained historical notebooks separately from reconstructed reusable software;
- documented known discrepancies between historical notebooks and the
  manuscript-reported protocol;
- added and refined reusable ConceptSMILE components for perturbation, locality,
  surrogate modelling, reliability metrics, and robustness evaluation;
- strengthened validation of degenerate inputs and metric assumptions;
- added automated behaviour tests;
- added a deterministic synthetic smoke test;
- added configuration validation;
- added Python package build validation; and
- established GitHub Actions testing under Python 3.10 and Python 3.11.

## Validation updates

The current software package has passed CI checks under both Python 3.10 and
Python 3.11.

The validated checks include:

- package installation;
- `ruff check .`;
- 33 unit tests;
- the synthetic smoke test;
- validation of `configs/paper.yaml`; and
- Python package build.

Earlier repository-audit checks also covered manuscript-table arithmetic,
transcription consistency, notebook preservation, documentation, and provenance.

These checks validate the software and repository structure. They do not constitute
an independent rerun of the complete four-dataset retinal experiments reported in
the manuscript.

## Provenance preservation

Historical notebook derivatives remain preserved as historical evidence.

Where notebook sanitisation was required, source code and retained plain-text outputs
were preserved while unverified rich-output material was excluded according to the
repository preservation records.

Historical notebooks must not be modified merely to make them appear consistent with
the final manuscript protocol.

Likewise, manuscript-transcribed numerical results must not be relabelled as
computational reproductions unless they are independently regenerated from verified
experimental inputs and implementation records.

## Remaining reproducibility limitations

The repository still does not establish complete end-to-end reproduction of all
reported manuscript experiments.

Outstanding provenance includes, among other items:

- exact final model/checkpoint revisions;
- complete final preprocessing settings;
- locality kernel parameters where not recorded;
- final XGBoost hyperparameters;
- train/test or validation split details;
- repeat counts and aggregation rules;
- complete row-level experimental outputs;
- full source data for manuscript figures and tables;
- complete robustness-experiment provenance; and
- a verified final experimental environment.

Unknown settings remain explicitly unresolved rather than being reconstructed without
evidence.

## Release and rights status

The repository remains under its existing rights statement.

No source retinal datasets or model weights are redistributed as part of the reviewed
repository.

The repository should not be described as providing complete experimental
reproducibility until the remaining implementation and provenance gaps are resolved.

The authoritative current assessment is maintained in:

`FINAL_REPOSITORY_STATUS.md`

Detailed validation information is maintained in:

`docs/audits/validation.md`

Detailed scientific traceability is maintained in:

`docs/audits/final-scientific-audit.md`

and:

`MANUSCRIPT_CODE_TRACEABILITY.md`
