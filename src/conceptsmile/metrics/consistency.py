"""ConceptSMILE consistency metrics.

Manuscript correspondence:
    Eq. (18): mean concept-importance score
    Eq. (19): sample variance and standard deviation

Lower variance and standard deviation indicate stronger
reproducibility across repeated runs.
"""

from __future__ import annotations

from dataclasses import dataclass

import numpy as np


@dataclass(frozen=True)
class ConsistencyMetrics:
    """Consistency evaluation results."""

    mean_importance: float
    variance: float
    standard_deviation: float
    n_runs: int


def evaluate_consistency(
    concept_importance_scores: np.ndarray,
) -> ConsistencyMetrics:
    """Evaluate repeated-run ConceptSMILE consistency.

    Parameters
    ----------
    concept_importance_scores:
        Repeated concept-importance scores a_i^(r)
        for the same concept and unchanged image
        under identical experimental settings.

    Returns
    -------
    ConsistencyMetrics
        Mean importance, sample variance,
        standard deviation, and number of runs.
    """

    scores = np.asarray(
        concept_importance_scores,
        dtype=float,
    ).reshape(-1)

    scores = scores[np.isfinite(scores)]

    if len(scores) < 2:
        raise ValueError(
            "At least two valid repeated "
            "concept-importance scores are required."
        )

    # Eq. (18)
    mean_importance = float(
        np.mean(scores)
    )

    # Eq. (19): denominator R - 1
    variance = float(
        np.sum(
            (scores - mean_importance) ** 2
        )
        / (len(scores) - 1)
    )

    standard_deviation = float(
        np.sqrt(variance)
    )

    return ConsistencyMetrics(
        mean_importance=mean_importance,
        variance=variance,
        standard_deviation=standard_deviation,
        n_runs=len(scores),
    )


def consistency_statistics(
    concept_importance_scores: np.ndarray,
) -> tuple[float, float]:
    """Return variance and standard deviation only."""

    result = evaluate_consistency(
        concept_importance_scores
    )

    return (
        result.variance,
        result.standard_deviation,
    )
