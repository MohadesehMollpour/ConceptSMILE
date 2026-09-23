# Final package validation

Software-only validation, 22 September 2026. Local runtime dependencies were initially unavailable and installed in a temporary validation directory. Commands were run with that directory and the final package src directory on PYTHONPATH so imports exercised the final source. This is not a fresh historical environment reconstruction. Exact current versions are in current_test_environment.json.

| Check | Observed result |
| --- | --- |
| python -m pytest -q | 28 passed |
| python -m ruff check src scripts tests | PASS |
| All discovered package imports | 22 modules PASS; no weights downloaded |
| python -m conceptsmile | PASS, 0.1.0.dev0 |
| Synthetic smoke test | PASS, 6×4 vectors, masking and weighted fidelity calculations |
| validate_config.py configs/paper.yaml | PASS, mapping parsing; not full experiment completeness |
| All YAML/YML/CFF parsing | PASS; full CFF schema not certified |
| audit_manuscript_tables.py | PASS; 48 Table6 pairs, 144 Table4 entries and cross-table exact matches |
| Notebook preservation | All source cells, execution counts and plain-text outputs equal original; changes restricted to declared non-text output/metadata removal |
| Manuscript table CSVs | Byte-identical to earlier verified transcriptions |
| Markdown file targets | PASS after final reports generated |
| Current-tree credential-pattern scan | No confirmed secret; no secrets printed |
| Image/model/data binary scan | No such assets bundled; notebook data MIME restricted to text/plain |
| Documentation build | PASS after replacing links outside MkDocs docs root with plain path references |
| Heavy models / paper reproduction | NOT RUN |

Placeholder scan found only quoted manuscript placeholders in manuscript-review.md and paper/README.md; those are audit findings, not unresolved repository-template fields. Historical Kaggle paths remain in two notebook derivatives and two legacy configs for provenance. Necessary author metadata in CFF is retained; no patient metadata was supplied or introduced. No clinical/privacy certification or complete Git-history scan is claimed.

The original notebooks are preserved outside this package. Release hashes intentionally differ due to disclosed sanitisation. Original rich-output MIME locations are indexed historically; they are not silently represented as still available in this ZIP. Numeric audit formulas do not fabricate corrected manuscript values.
