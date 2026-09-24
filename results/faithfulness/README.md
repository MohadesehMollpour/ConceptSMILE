"""ConceptSMILE faithfulness metric.

Paper Eq. (16):
Pearson correlation between concept-relevant perturbation
strength and absolute concept-response shift.
"""

from dataclasses import dataclass

import numpy as np
from scipy.stats import pearsonr


@dataclass(frozen=True)
class FaithfulnessResult:
    correlation: float
    p_value: float
    n: int


def evaluate_faithfulness(
    perturbation_strength,
    response_shift,
) -> FaithfulnessResult:
    strength = np.asarray(
        perturbation_strength,
        dtype=float,
    ).reshape(-1)

    shift = np.abs(
        np.asarray(response_shift, dtype=float).reshape(-1)
    )

    if strength.shape != shift.shape:
        raise ValueError(
            "perturbation_strength and response_shift "
            "must have equal length."
        )

    valid = np.isfinite(strength) & np.isfinite(shift)

    strength = strength[valid]
    shift = shift[valid]

    if len(strength) < 3:
        return FaithfulnessResult(
            correlation=float("nan"),
            p_value=float("nan"),
            n=len(strength),
        )

    if (
        np.unique(strength).size < 2
        or np.unique(shift).size < 2
    ):
        return FaithfulnessResult(
            correlation=float("nan"),
            p_value=float("nan"),
            n=len(strength),
        )

    correlation, p_value = pearsonr(strength, shift)

    return FaithfulnessResult(
        correlation=float(correlation),
        p_value=float(p_value),
        n=len(strength),
    )
