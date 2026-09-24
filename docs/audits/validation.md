# Final package validation

Software-focused validation has been performed on the current ConceptSMILE repository.

This validation is not a reconstruction of the historical experimental environment and
does not constitute a rerun of the retinal experiments reported in the manuscript.

## Current CI validation

The current repository state was validated through GitHub Actions on 24 September 2026
using both Python 3.10 and Python 3.11.

For both Python versions, the following checks completed successfully:

| Check | Current result |
| --- | --- |
| Package installation | PASS |
| `ruff check .` | PASS |
| `pytest` | 33 passed |
| `python scripts/synthetic_smoke_test.py` | PASS |
| `python scripts/validate_config.py configs/paper.yaml` | PASS |
| `python -m build` | PASS |

The successful CI run verifies that the current reusable software package, tests,
configuration validation, smoke test, and package build complete successfully under
both supported Python versions.

This software validation does not establish that the complete four-dataset retinal
experiments reported in the manuscript have been reproduced.

## Earlier repository audit validation

An earlier software and repository audit was performed on 22 September 2026 before
the most recent code and documentation updates.

That audit included:

- package import checks;
- package entry-point execution;
- synthetic software tests;
- configuration and metadata parsing;
- manuscript table arithmetic and traceability audits;
- notebook preservation checks;
- manuscript table transcription checks;
- Markdown target checking;
- credential-pattern scanning of the reviewed repository tree;
- binary/data-content review; and
- documentation build validation.

Some numerical counts recorded during that earlier audit, including the earlier
28-test result, describe the repository state at that time and have been superseded
for current software validation by the successful 33-test CI result above.

## Repository-alignment updates

The current repository includes the following manuscript-alignment improvements:

- the author-confirmed 40-image evaluation subset is documented in
  `data/manifests/paper_40_images.csv`;
- `configs/paper.yaml` links to the evaluation manifest and identifies the current
  reviewed manuscript;
- the root README links to the evaluation manifest;
- `docs/datasets.md` documents the evaluation subset;
- the manuscript dataset citations are completed;
- the manuscript Code Availability statement contains the repository URL;
- the manuscript Author Contributions section is completed;
- `CITATION.cff` lists all seven manuscript authors; and
- `pyproject.toml` lists all seven manuscript authors.

These changes improve repository/manuscript alignment but do not constitute rerunning
the reported retinal experiments.

## Historical and preserved material

Historical Kaggle/local paths remain in sanitised notebook derivatives and legacy
configuration files where they are necessary for provenance.

These historical paths should not be interpreted as the final manuscript data layout or
as proof that the preserved single-image notebooks generated the complete manuscript
results.

The historical notebooks remain separated from manuscript-aligned reconstructed
software and should not be modified merely to make their settings appear consistent
with the final manuscript protocol.

## Scope and limitations of validation

The current software validation establishes that the reviewed reusable package and
its automated checks execute successfully under Python 3.10 and Python 3.11.

It does **not** establish:

- full four-dataset manuscript reproduction;
- recovery of the original historical execution environment;
- independent validation of attribution-reference labels;
- reproduction of Tables 2–7 from row-level experimental outputs;
- reproduction of Figures 9–11 from original source data;
- complete stability-experiment provenance;
- complete VLM robustness provenance;
- exact historical model/checkpoint hashes;
- exact final preprocessing and surrogate settings where these remain unknown;
- clinical validity or diagnostic performance;
- privacy certification; or
- a complete Git-history security audit.

Numeric audit utilities identify arithmetic or provenance concerns but do not fabricate,
repair, or substitute corrected manuscript values.

Unknown experimental settings and unavailable evidence should remain explicitly
unresolved until genuine source records or verified rerun evidence are available.
