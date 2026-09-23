# Provenance: RECONSTRUCTED reusable code; historical execution not established.
"""Unweighted and locality-weighted surrogate-fidelity metrics."""

from __future__ import annotations

from dataclasses import asdict, dataclass

import numpy as np
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score


def _aligned(*arrays: np.ndarray) -> tuple[np.ndarray, ...]:
    converted = tuple(np.asarray(array, dtype=float).reshape(-1) for array in arrays)
    if not converted or not len(converted[0]) or len({len(array) for array in converted}) != 1:
        raise ValueError("all inputs must be non-empty and have equal length")
    if not np.all(np.isfinite(np.concatenate(converted))):
        raise ValueError("inputs must contain only finite values")
    return converted


def weighted_mean(values: np.ndarray, weights: np.ndarray) -> float:
    """Return a weighted mean; reject negative or zero-total locality weights."""
    value_array, weight_array = _aligned(values, weights)
    weight_sum = float(weight_array.sum())
    if (weight_array < 0).any() or weight_sum <= 0:
        raise ValueError("weights must be nonnegative with positive sum")
    return float(
        np.sum(weight_array * value_array) / weight_sum
    )


def weighted_mse(y_true: np.ndarray, y_pred: np.ndarray, weights: np.ndarray) -> float:
    """Weighted mean squared error."""
    true, predicted, weight_array = _aligned(y_true, y_pred, weights)
    return weighted_mean((true - predicted) ** 2, weight_array)


def weighted_mae(y_true: np.ndarray, y_pred: np.ndarray, weights: np.ndarray) -> float:
    """Weighted mean absolute error."""
    true, predicted, weight_array = _aligned(y_true, y_pred, weights)
    return weighted_mean(np.abs(true - predicted), weight_array)


def weighted_r2(y_true: np.ndarray, y_pred: np.ndarray, weights: np.ndarray) -> float:
    """Weighted coefficient of determination; not proof of a manuscript result."""
    true, predicted, weight_array = _aligned(y_true, y_pred, weights)
    mean = weighted_mean(true, weight_array)
    if len(true) < 2:
        return float("nan")
    residual = float(np.sum(weight_array * (true - predicted) ** 2))
    total = float(np.sum(weight_array * (true - mean) ** 2))
    return float("nan") if total <= 1e-12 else 1.0 - residual / total


def kish_effective_n(weights: np.ndarray) -> float:
    """Kish effective sample size used by the legacy adjusted-R² calculation."""
    array = np.asarray(weights, dtype=float).reshape(-1)
    if (not array.size or not np.isfinite(array).all()
            or (array < 0).any() or array.sum() <= 0):
        raise ValueError("weights must be finite, nonnegative, nonempty with positive sum")
    denominator = float(np.sum(array**2))
    return float(len(array)) if denominator <= 0 else float(array.sum() ** 2 / denominator)


@dataclass(frozen=True)
class FidelityMetrics:
    """Complete fidelity metric set reported by the notebook."""

    mse: float
    mae: float
    wmse: float
    wmae: float
    r2: float
    weighted_r2: float

    def to_dict(self) -> dict[str, float]:
        """Return serialisable metric values."""
        return asdict(self)


def evaluate_fidelity(
    y_true: np.ndarray, y_pred: np.ndarray, weights: np.ndarray | None = None
) -> FidelityMetrics:
    """Evaluate surrogate predictions against observed concept-response shifts."""
    true, predicted = _aligned(y_true, y_pred)
    weight_array = np.ones_like(true) if weights is None else _aligned(true, weights)[1]
    return FidelityMetrics(
        mse=float(mean_squared_error(true, predicted)),
        mae=float(mean_absolute_error(true, predicted)),
        wmse=weighted_mse(true, predicted, weight_array),
        wmae=weighted_mae(true, predicted, weight_array),
        r2=float(r2_score(true, predicted)) if len(true) >= 2 else float("nan"),
        weighted_r2=weighted_r2(true, predicted, weight_array),
    )

