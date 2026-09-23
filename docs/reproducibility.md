# Reproducibility guide

This package supports software-only tests. It does not supply a complete retinal experiment driver or recover the manuscript results.

```bash
python -m pip install -e .[dev]
python -m pytest
python -m conceptsmile
python scripts/synthetic_smoke_test.py
python scripts/validate_config.py configs/paper.yaml
python scripts/audit_manuscript_tables.py
```

The last command audits arithmetic and provenance of existing transcriptions; it does not regenerate experiments. No model download is needed for these commands. Current tested versions and validation outcomes are under audits/.

Historical notebooks are sanitised provenance records and contain Kaggle paths, moving installs and conflicting environment steps. Do not equate candidate requirements-models.txt with a tested historical environment. Heavy model runs require original local data, reviewed model dependencies and verified checkpoints.

Paper-level settings are manuscript-reported, not proof of execution. Legacy settings remain separate. Exact 40-image selection, independent annotations, four-dataset outputs, stability and VLM robustness artefacts are NOT AVAILABLE. Any new experiment must record resolved config, input identifiers, model hashes, environment and row-level outputs under a distinct RE-RUN location; never overwrite manuscript_transcribed/.
