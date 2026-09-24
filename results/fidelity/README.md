"""ConceptSMILE surrogate-fidelity metrics.

Paper:
    Eq. (12): WMSE
    Eq. (13): WMAE
    Eq. (14): weighted R^2
    Eq. (15): weighted mean

Also reports ordinary MSE, MAE, and R^2.
"""

from dataclasses import dataclass

import numpy as np
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score


@dataclass(frozen=True)
class FidelityResult:
    mse: float
    mae: float
    wmse: float
    wmae: float
    r2: float
    weighted_r2: float


def _prepare(y_true, y_pred, weights):
    y_true = np.asarray(y_true, dtype=float).reshape(-1)
    y_pred = np.asarray(y_pred, dtype=float).reshape(-1)
    weights = np.asarray(weights, dtype=float).reshape(-1)

    if not (len(y_true) == len(y_pred) == len(weights)):
        raise ValueError("y_true, y_pred, and weights must have equal length.")

    if len(y_true) == 0:
        raise ValueError("Inputs cannot be empty.")

    if not (
        np.isfinite(y_true).all()
        and np.isfinite(y_pred).all()
        and np.isfinite(weights).all()
    ):
        raise ValueError("Inputs must contain finite values.")

    if np.any(weights < 0):
        raise ValueError("Locality weights cannot be negative.")

    if np.sum(weights) <= 0:
        raise ValueError("Locality weights must have a positive sum.")

    return y_true, y_pred, weights


def evaluate_fidelity(y_true, y_pred, weights) -> FidelityResult:
    y_true, y_pred, weights = _prepare(
        y_true,
        y_pred,
        weights,
    )

    weight_sum = np.sum(weights)

    errors = y_true - y_pred

    # Eq. (12)
    wmse = np.sum(weights * errors**2) / weight_sum

    # Eq. (13)
    wmae = np.sum(weights * np.abs(errors)) / weight_sum

    # Eq. (15)
    weighted_mean = np.sum(weights * y_true) / weight_sum

    # Eq. (14)
    weighted_residual = np.sum(weights * errors**2)
    weighted_total = np.sum(
        weights * (y_true - weighted_mean) ** 2
    )

    if weighted_total == 0:
        weighted_r2 = float("nan")
    else:
        weighted_r2 = 1.0 - weighted_residual / weighted_total

    mse = mean_squared_error(y_true, y_pred)
    mae = mean_absolute_error(y_true, y_pred)

    if len(y_true) < 2:
        r2 = float("nan")
    else:
        r2 = r2_score(y_true, y_pred)

    return FidelityResult(
        mse=float(mse),
        mae=float(mae),
        wmse=float(wmse),
        wmae=float(wmae),
        r2=float(r2),
        weighted_r2=float(weighted_r2),
    )
