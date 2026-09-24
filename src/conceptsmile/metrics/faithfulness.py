"""ConceptSMILE faithfulness metric.

Manuscript correspondence:
    Eq. (16)

Faithfulness is measured using Pearson correlation between
concept-relevant perturbation strength and the absolute
concept-response shift.
"""

from __future__ import annotations

from dataclasses import dataclass

import numpy as np
from scipy.stats import pearsonr


@dataclass(frozen=True)
class FaithfulnessMetrics:
    """Faithfulness evaluation results."""

    correlation: float
    p_value: float
    n: int
    status: str


def evaluate_faithfulness(
    perturbation_strength: np.ndarray,
    response_shift: np.ndarray,
) -> FaithfulnessMetrics:
    """Evaluate ConceptSMILE faithfulness.

    Parameters
    ----------
    perturbation_strength:
        Concept-relevant perturbation strength s_i^(k).

    response_shift:
        Concept-response shift Δy_i^(k).
        The manuscript uses its absolute value in Eq. (16).

    Returns
    -------
    FaithfulnessMetrics
        Pearson correlation, p-value, number of valid
        perturbations, and evaluation status.
    """

    strength = np.asarray(
        perturbation_strength,
        dtype=float,
    ).reshape(-1)

    shift = np.abs(
        np.asarray(
            response_shift,
            dtype=float,
        ).reshape(-1)
    )

    if strength.shape != shift.shape:
        raise ValueError(
            "perturbation_strength and response_shift "
            "must have equal length."
        )

    valid = (
        np.isfinite(strength)
        & np.isfinite(shift)
    )

    strength = strength[valid]
    shift = shift[valid]

    if len(strength) < 3:
        return FaithfulnessMetrics(
            correlation=float("nan"),
            p_value=float("nan"),
            n=len(strength),
            status="too_few_samples",
        )

    if (
        np.unique(strength).size < 2
        or np.unique(shift).size < 2
    ):
        return FaithfulnessMetrics(
            correlation=float("nan"),
            p_value=float("nan"),
            n=len(strength),
            status="no_variation",
        )

    correlation, p_value = pearsonr(
        strength,
        shift,
    )

    return FaithfulnessMetrics(
        correlation=float(correlation),
        p_value=float(p_value),
        n=len(strength),
        status="ok",
    )
