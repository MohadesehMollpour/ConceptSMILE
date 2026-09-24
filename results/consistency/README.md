"""ConceptSMILE consistency metrics.

Paper:
    Eq. (18): mean concept-importance score
    Eq. (19): sample variance and standard deviation
"""

from dataclasses import dataclass

import numpy as np


@dataclass(frozen=True)
class ConsistencyResult:
    mean_importance: float
    variance: float
    standard_deviation: float
    n_runs: int


def evaluate_consistency(
    concept_importance_scores,
) -> ConsistencyResult:
    scores = np.asarray(
        concept_importance_scores,
        dtype=float,
    ).reshape(-1)

    scores = scores[np.isfinite(scores)]

    if len(scores) < 2:
        raise ValueError(
            "At least two repeated concept-importance "
            "scores are required."
        )

    # Eq. (18)
    mean_importance = np.mean(scores)

    # Eq. (19), denominator R - 1
    variance = np.sum(
        (scores - mean_importance) ** 2
    ) / (len(scores) - 1)

    standard_deviation = np.sqrt(variance)

    return ConsistencyResult(
        mean_importance=float(mean_importance),
        variance=float(variance),
        standard_deviation=float(standard_deviation),
        n_runs=len(scores),
    )
