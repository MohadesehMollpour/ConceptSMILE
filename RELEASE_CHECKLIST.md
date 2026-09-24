# Release checklist

| Item | Status |
| --- | --- |
| Current manuscript source recorded in `configs/paper.yaml` | PASS |
| 40-image evaluation manifest | PASS; author-confirmed subset documented in `data/manifests/paper_40_images.csv` |
| Manuscript-transcribed Tables 2–7 clearly labelled | PASS |
| Historical notebooks separated from reusable software | PASS |
| Automated CI on Python 3.10 and Python 3.11 | PASS |
| Ruff checks | PASS |
| Unit tests | PASS; 33 tests |
| Synthetic smoke test | PASS |
| Configuration validation | PASS |
| Python package build | PASS |
| Exact model/checkpoint revisions or hashes | ACTION REQUIRED for exact reproduction |
| Complete final preprocessing settings | ACTION REQUIRED where not preserved |
| Final XGBoost hyperparameters | ACTION REQUIRED where not preserved |
| Train/test or validation split details | ACTION REQUIRED where not preserved |
| Repeat counts and aggregation rules | ACTION REQUIRED where not preserved |
| Complete row-level outputs for the four-dataset study | NOT AVAILABLE |
| Complete source data for reported figures and tables | INCOMPLETE |
| Complete end-to-end reproduction of the manuscript experiments | NOT ESTABLISHED |

## Interpretation

A `PASS` entry indicates that the listed repository or software check has been
verified.

`ACTION REQUIRED`, `NOT AVAILABLE`, `INCOMPLETE`, and `NOT ESTABLISHED` entries
identify remaining reproducibility or provenance gaps and must not be replaced by
inferred values.

The authoritative repository assessment is maintained in:

`FINAL_REPOSITORY_STATUS.md`
