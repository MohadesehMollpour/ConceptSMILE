"""ConceptSMILE robustness evaluation.

Manuscript correspondence:
    Section 5.3

Contrast factors:
    0.6, 0.8, 1.0, 1.2, 1.4

Simulated occlusion:
    0%, 1%, 2%, 3% of retinal width

Robustness outcome:
    repeated XGBoost Test R² values,
    summarised using mean, median, and standard deviation.
"""

from __future__ import annotations

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
class RobustnessMetrics:
    """Summary of repeated robustness Test R² values."""

    mean_r2: float
    median_r2: float
    standard_deviation: float
    n_runs: int


def evaluate_test_r2(
    y_true: np.ndarray,
    y_pred: np.ndarray,
) -> float:
    """Compute Test R² for one robustness evaluation run."""

    true = np.asarray(
        y_true,
        dtype=float,
    ).reshape(-1)

    predicted = np.asarray(
        y_pred,
        dtype=float,
    ).reshape(-1)

    if true.shape != predicted.shape:
        raise ValueError(
            "y_true and y_pred must have equal length."
        )

    if len(true) < 2:
        return float("nan")

    if not (
        np.isfinite(true).all()
        and np.isfinite(predicted).all()
    ):
        raise ValueError(
            "y_true and y_pred must contain only finite values."
        )

    return float(
        r2_score(true, predicted)
    )


def summarise_robustness(
    test_r2_values: np.ndarray,
) -> RobustnessMetrics:
    """Summarise repeated Test R² values.

    The manuscript displays:
    - individual repeated evaluations;
    - mean;
    - median; and
    - mean ± standard deviation.
    """

    values = np.asarray(
        test_r2_values,
        dtype=float,
    ).reshape(-1)

    values = values[np.isfinite(values)]

    if len(values) == 0:
        raise ValueError(
            "At least one valid Test R² value is required."
        )

    mean_r2 = float(
        np.mean(values)
    )

    median_r2 = float(
        np.median(values)
    )

    if len(values) < 2:
        standard_deviation = float("nan")
    else:
        standard_deviation = float(
            np.std(values, ddof=1)
        )

    return RobustnessMetrics(
        mean_r2=mean_r2,
        median_r2=median_r2,
        standard_deviation=standard_deviation,
        n_runs=len(values),
    )
