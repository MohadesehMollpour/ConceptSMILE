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

Important:
    The manuscript does not specify the degrees-of-freedom
    convention used for the robustness standard deviation.
    Therefore, ddof must be supplied explicitly rather than
    inferred.
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
    ddof: int


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
    *,
    ddof: int,
) -> RobustnessMetrics:
    """Summarise repeated Test R² values.

    Parameters
    ----------
    test_r2_values:
        Repeated Test R² values for one robustness condition.

    ddof:
        Degrees of freedom used when calculating the standard
        deviation. This must be supplied explicitly because the
        manuscript does not specify the convention.

    Returns
    -------
    RobustnessMetrics
        Mean, median, standard deviation, number of runs,
        and the supplied ddof.
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

    if not isinstance(ddof, int):
        raise TypeError(
            "ddof must be an integer."
        )

    if ddof < 0:
        raise ValueError(
            "ddof must be non-negative."
        )

    if ddof >= len(values):
        raise ValueError(
            "ddof must be smaller than the number of valid runs."
        )

    mean_r2 = float(
        np.mean(values)
    )

    median_r2 = float(
        np.median(values)
    )

    standard_deviation = float(
        np.std(
            values,
            ddof=ddof,
        )
    )

    return RobustnessMetrics(
        mean_r2=mean_r2,
        median_r2=median_r2,
        standard_deviation=standard_deviation,
        n_runs=len(values),
        ddof=ddof,
    )
