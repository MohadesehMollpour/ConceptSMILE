## Validation already performed

The current reusable software package has been validated through GitHub Actions on
Python 3.10 and Python 3.11.

The latest completed CI validation recorded:

- package installation passed;
- Ruff checks passed;
- 33 unit tests passed;
- the synthetic smoke test passed;
- `configs/paper.yaml` validation passed; and
- the Python package build passed.

Earlier repository-audit validation also included:

- package import and entry-point checks;
- configuration/YAML/CFF parsing;
- Table 6 arithmetic auditing covering 48 displayed variance/SD pairs;
- Table 4 auditing covering 144 displayed values;
- cross-table exact-value matching;
- manuscript-table transcription checking;
- historical notebook preservation checks;
- Markdown target checking;
- current-tree credential-pattern scanning; and
- documentation build validation.

Full details and the distinction between the earlier audit and current CI validation
are recorded in:

`docs/audits/validation.md`

These checks establish software, documentation, transcription, and provenance
validation only. They are **not** equivalent to rerunning the complete retinal
experiments reported in the manuscript.
