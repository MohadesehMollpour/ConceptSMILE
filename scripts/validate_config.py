#!/usr/bin/env python3
"""Validate the minimal structure and referenced local paths of a YAML config."""

from __future__ import annotations

import argparse
import os
from pathlib import Path

import yaml


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("config", type=Path)
    args = parser.parse_args()

    document = yaml.safe_load(args.config.read_text(encoding="utf-8"))
    if not isinstance(document, dict):
        raise SystemExit("configuration root must be a mapping")

    print(f"Config: {args.config}")
    print(f"Top-level sections: {', '.join(document)}")

    data_root = os.getenv("CONCEPTSMILE_DATA_ROOT")
    model_root = os.getenv("CONCEPTSMILE_MODEL_ROOT")
    print(f"CONCEPTSMILE_DATA_ROOT: {data_root or 'NOT SET'}")
    print(f"CONCEPTSMILE_MODEL_ROOT: {model_root or 'NOT SET'}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

