# Provenance: RECONSTRUCTED reusable code; historical execution not established.
"""Random-state control for repeatable experiments."""

from __future__ import annotations

import random

import numpy as np


def set_random_seeds(seed: int = 42) -> None:
    """Seed Python, NumPy, and PyTorch when available."""
    random.seed(seed)
    np.random.seed(seed)
    try:
        import torch
    except ImportError:
        return
    torch.manual_seed(seed)
    if torch.cuda.is_available():
        torch.cuda.manual_seed_all(seed)

