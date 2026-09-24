# Final package validation

Software-only validation was performed on 22 September 2026. Local runtime dependencies
were initially unavailable and were installed in a temporary validation directory.
Commands were run with that directory and the repository `src` directory on
`PYTHONPATH` so imports exercised the reviewed source package.

This validation is not a reconstruction of the historical experimental environment and
does not constitute a rerun of the retinal experiments reported in the manuscript.

The validation results below record the checks that were actually run. Subsequent
documentation, manifest, citation-metadata, and repository-alignment updates should not
be interpreted as new model-heavy experimental validation.

| Check | Observed result |
| --- | --- |
| `python -m pytest -q` | 28 passed |
| `python -m ruff check src scripts tests` | PASS |
| All discovered package imports | 22 modules PASS; no model weights downloaded |
| `python -m conceptsmile` | PASS, version `0.1.0.dev0` |
| Synthetic smoke test | PASS; 6×4 vectors, masking, and weighted fidelity calculations |
| `validate_config.py configs/paper.yaml` | PASS for configuration/YAML structure; this is not proof of complete experiment reproducibility |
| YAML/YML/CFF parsing | PASS for reviewed files; full CFF schema certification was not performed |
| `audit_manuscript_tables.py` | PASS; 48 Table 6 variance/SD pairs, 144 Table 4 entries, and cross-table exact-value matches audited |
| Notebook preservation | Source cells, execution counts, and retained plain-text outputs matched the reviewed historical notebook material; sanitisation changes were limited to declared non-text output/metadata removal |
| Manuscript table CSVs | Matched the previously verified manuscript transcriptions |
| Markdown file targets | PASS at the time of the original validation run |
| Current-tree credential-pattern scan | No confirmed secret found in the reviewed tree; no secrets printed |
| Image/model/data binary scan | No source datasets or model weights bundled in the reviewed package; sanitised notebook output MIME restricted to retained textual material |
| Documentation build | PASS at the time of the validation run after links outside the MkDocs documentation root were represented appropriately |
| Heavy models / complete paper reproduction | NOT RUN |

## Current repository-alignment updates

Since the original validation run, the repository documentation and metadata have been
updated to align more closely with the current 49-page ConceptSMILE manuscript.

The following previously identified repository issues are now resolved:

- the author-confirmed 40-image evaluation subset is documented in
  `data/manifests/paper_40_images.csv`;
- `configs/paper.yaml` links to the evaluation manifest;
- the root README links to the evaluation manifest;
- `docs/datasets.md` no longer states that the 40-image subset is unavailable;
- the manuscript dataset-citation placeholders are resolved;
- the manuscript Code Availability section contains the repository URL;
- the manuscript Author Contributions section is completed;
- `CITATION.cff` now lists all seven manuscript authors; and
- `pyproject.toml` now lists all seven manuscript authors.

These changes improve repository/manuscript alignment but do not constitute rerunning
the reported retinal experiments.

## Historical and preserved material

Historical Kaggle/local paths remain in sanitised notebook derivatives and legacy
configuration files where they are necessary for provenance.

These historical paths should not be interpreted as the final manuscript data layout or
as proof that the preserved single-image notebooks generated the complete manuscript
results.

The original notebook material is preserved separately from the sanitised derivatives.
Release hashes intentionally differ where sanitisation removed rich-output MIME payloads,
attachments, or other declared non-text material.

Original rich-output locations are indexed historically; they are not represented as if
their removed payloads were still present in the current repository.

## Scope and limitations of validation

The software validation establishes that the reviewed reusable package and audit
utilities could be imported and exercised successfully under the temporary validation
environment used on 22 September 2026.

It does **not** establish:

- full four-dataset manuscript reproduction;
- recovery of the original historical execution environment;
- independent validation of attribution-reference labels;
- reproduction of Tables 2–7 from row-level experiment outputs;
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
