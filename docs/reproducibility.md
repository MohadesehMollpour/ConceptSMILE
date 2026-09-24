# Reproducibility guide

This package supports software-level validation and repository traceability. It does not
yet provide a complete end-to-end rerun of all retinal experiments reported in the
manuscript.

```bash
python -m pip install -e .[dev]
python -m pytest
python -m conceptsmile
python scripts/synthetic_smoke_test.py
python scripts/validate_config.py configs/paper.yaml
python scripts/audit_manuscript_tables.py
