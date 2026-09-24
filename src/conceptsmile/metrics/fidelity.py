"""ConceptSMILE surrogate-fidelity metrics.

Manuscript correspondence:
    Eq. (12): weighted mean squared error (WMSE)
    Eq. (13): weighted mean absolute error (WMAE)
    Eq. (14): weighted coefficient of determination (R²_w)
    Eq. (15): weighted mean concept-response shift

The manuscript also reports ordinary MSE, MAE, and R².
"""

from __future__ import annotations

from dataclasses import dataclass

import numpy as np
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score


@dataclass(frozen=True)
class FidelityMetrics:
    """Surrogate-fidelity evaluation results."""

    mse: float
    mae: float
    wmse: float
    wmae: float
    r2: float
    weighted_r2: float
    n: int


def _prepare_inputs(
    y_true: np.ndarray,
    y_pred: np.ndarray,
    weights: np.ndarray,
) -> tuple[np.ndarray, np.ndarray, np.ndarray]:
    """Validate and align fidelity inputs."""

    true = np.asarray(y_true, dtype=float).reshape(-1)
    predicted = np.asarray(y_pred, dtype=float).reshape(-1)
    locality_weights = np.asarray(weights, dtype=float).reshape(-1)

    if true.size == 0:
        raise ValueError("Inputs must be non-empty.")

    if not (
        len(true)
        == len(predicted)
        == len(locality_weights)
    ):
        raise ValueError(
            "y_true, y_pred, and weights must have equal length."
        )

    if not (
        np.isfinite(true).all()
        and np.isfinite(predicted).all()
        and np.isfinite(locality_weights).all()
    ):
        raise ValueError(
            "y_true, y_pred, and weights must contain only finite values."
        )

    if np.any(locality_weights < 0):
        raise ValueError(
            "Locality weights must be non-negative."
        )

    if locality_weights.sum() <= 0:
        raise ValueError(
            "Locality weights must have a positive sum."
        )

    return true, predicted, locality_weights


def weighted_mean(
    values: np.ndarray,
    weights: np.ndarray,
) -> float:
    """Compute the weighted mean from Eq. (15)."""

    return float(
        np.sum(weights * values) / np.sum(weights)
    )


def evaluate_fidelity(
    y_true: np.ndarray,
    y_pred: np.ndarray,
    weights: np.ndarray,
) -> FidelityMetrics:
    """Evaluate local-surrogate fidelity.

    Parameters
    ----------
    y_true:
        Observed concept-response shifts.

    y_pred:
        Surrogate-predicted concept-response shifts.

    weights:
        Locality weights associated with the perturbations.

    Returns
    -------
    FidelityMetrics
        MSE, MAE, WMSE, WMAE, R², weighted R²,
        and the number of evaluated perturbations.
    """

    true, predicted, locality_weights = _prepare_inputs(
        y_true,
        y_pred,
        weights,
    )

    residual = true - predicted
    weight_sum = locality_weights.sum()

    # Eq. (12)
    wmse = float(
        np.sum(locality_weights * residual**2)
        / weight_sum
    )

    # Eq. (13)
    wmae = float(
        np.sum(locality_weights * np.abs(residual))
        / weight_sum
    )

    # Eq. (15)
    weighted_true_mean = weighted_mean(
        true,
        locality_weights,
    )

    # Eq. (14)
    weighted_residual_sum = float(
        np.sum(locality_weights * residual**2)
    )

    weighted_total_sum = float(
        np.sum(
            locality_weights
            * (true - weighted_true_mean) ** 2
        )
    )

    if weighted_total_sum <= 0:
        weighted_r2 = float("nan")
    else:
        weighted_r2 = float(
            1.0
            - weighted_residual_sum
            / weighted_total_sum
        )

    mse = float(
        mean_squared_error(true, predicted)
    )

    mae = float(
        mean_absolute_error(true, predicted)
    )

    if len(true) < 2:
        r2 = float("nan")
    else:
        r2 = float(
            r2_score(true, predicted)
        )

    return FidelityMetrics(
        mse=mse,
        mae=mae,
        wmse=wmse,
        wmae=wmae,
        r2=r2,
        weighted_r2=weighted_r2,
        n=len(true),
    )
