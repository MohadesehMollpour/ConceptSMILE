# Provenance: RECONSTRUCTED reusable code; historical execution not established.
"""XGBoost surrogate configuration recorded in the publication-style cells."""

from __future__ import annotations

from dataclasses import dataclass

from xgboost import XGBRegressor


@dataclass(frozen=True)
class XGBoostConfig:
    """Recorded XGBoost settings used by repeated-run notebook cells."""

    n_estimators: int = 200
    max_depth: int = 3
    learning_rate: float = 0.05
    subsample: float = 0.8
    colsample_bytree: float = 0.8
    reg_lambda: float = 1.0
    objective: str = "reg:squarederror"
    n_jobs: int = 1


def build_xgboost_regressor(
    *, random_state: int = 42, config: XGBoostConfig | None = None
) -> XGBRegressor:
    """Construct, but do not fit, the recorded local surrogate."""
    settings = config or XGBoostConfig()
    return XGBRegressor(
        n_estimators=settings.n_estimators,
        max_depth=settings.max_depth,
        learning_rate=settings.learning_rate,
        subsample=settings.subsample,
        colsample_bytree=settings.colsample_bytree,
        reg_lambda=settings.reg_lambda,
        objective=settings.objective,
        random_state=random_state,
        n_jobs=settings.n_jobs,
    )

