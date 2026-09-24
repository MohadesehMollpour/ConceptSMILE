"""ConceptSMILE acquisition-robustness evaluation.

Paper Section 5.3:
    Contrast: 0.6, 0.8, 1.0, 1.2, 1.4
    Occlusion: 0%, 1%, 2%, 3% retinal width
    Outcome: repeated XGBoost Test R^2
"""

from dataclasses import dataclass

import numpy as np
from sklearn.metrics import r2_score


CONTRAST_FACTORS = (
    0.6,
    0.8,
    1.0,
    1.2,
    1.4,
)

OCCLUSION_PERCENTAGES = (
    0,
    1,
    2,
    3,
)


@dataclass(frozen=True)
class RobustnessSummary:
    mean_r2: float
    median_r2: float
    std_r2: float
    n_runs: int


def test_r2(y_true, y_pred):
    y_true = np.asarray(
        y_true,
        dtype=float,
    ).reshape(-1)

    y_pred = np.asarray(
        y_pred,
        dtype=float,
    ).reshape(-1)

    if y_true.shape != y_pred.shape:
        raise ValueError(
            "y_true and y_pred must have equal length."
        )

    if len(y_true) < 2:
        return float("nan")

    return float(r2_score(y_true, y_pred))


def summarise_robustness(test_r2_values):
    values = np.asarray(
        test_r2_values,
        dtype=float,
    ).reshape(-1)

    values = values[np.isfinite(values)]

    if len(values) == 0:
        raise ValueError(
            "At least one valid Test R2 value is required."
        )

    std = (
        np.std(values, ddof=1)
        if len(values) > 1
        else float("nan")
    )

    return RobustnessSummary(
        mean_r2=float(np.mean(values)),
        median_r2=float(np.median(values)),
        std_r2=float(std),
        n_runs=len(values),
    )
