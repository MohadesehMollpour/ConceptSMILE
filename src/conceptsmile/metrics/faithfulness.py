# Provenance: RECONSTRUCTED reusable code; historical execution not established.
"""Correlation-based concept faithfulness."""

from __future__ import annotations

from dataclasses import dataclass

import numpy as np
from scipy.stats import pearsonr


@dataclass(frozen=True)
class FaithfulnessResult:
    correlation: float
    p_value: float
    n: int
    status: str


def pearson_faithfulness(
    affected_fraction: np.ndarray,
    response_shift: np.ndarray,
) -> FaithfulnessResult:
    """Correlate supplied perturbation strength with absolute response shift.

    The caller must establish whether strength is concept-specific; correlation
    alone does not establish causal validity or independent clinical relevance."""
    affected = np.asarray(affected_fraction, dtype=float).reshape(-1)
    shift = np.abs(np.asarray(response_shift, dtype=float).reshape(-1))
    if len(affected) != len(shift):
        raise ValueError("affected_fraction and response_shift must have equal length")
    valid = np.isfinite(affected) & np.isfinite(shift)
    affected = affected[valid]
    shift = shift[valid]
    if len(affected) < 3:
        return FaithfulnessResult(float("nan"), float("nan"), len(affected), "too_few_samples")
    if np.unique(affected).size < 2 or np.unique(shift).size < 2:
        return FaithfulnessResult(float("nan"), float("nan"), len(affected), "no_variation")
    correlation, p_value = pearsonr(affected, shift)
    return FaithfulnessResult(float(correlation), float(p_value), len(affected), "ok")

