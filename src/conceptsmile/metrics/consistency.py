# Provenance: RECONSTRUCTED reusable code; historical execution not established.
"""Generic repeated-score statistics; input semantics must be documented."""

from __future__ import annotations

import numpy as np


def consistency_statistics(scores: np.ndarray) -> tuple[float, float]:
    """Return sample variance and standard deviation across repeated scores."""
    values = np.asarray(scores, dtype=float).reshape(-1)
    values = values[np.isfinite(values)]
    if len(values) < 2:
        return float("nan"), float("nan")
    variance = float(np.var(values, ddof=1))
    return variance, float(np.sqrt(variance))

