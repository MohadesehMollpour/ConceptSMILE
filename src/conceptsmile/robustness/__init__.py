"""ConceptSMILE acquisition-robustness utilities.

This package contains utilities for the additional robustness
analysis reported in Section 5.3 of the manuscript.
"""

from .acquisition import (
    add_simulated_occlusion,
    modify_retinal_contrast,
    retinal_fov_mask,
)
from .evaluation import (
    CONTRAST_FACTORS,
    OCCLUSION_PERCENTAGES,
    RobustnessMetrics,
    evaluate_test_r2,
    summarise_robustness,
)

__all__ = [
    "CONTRAST_FACTORS",
    "OCCLUSION_PERCENTAGES",
    "RobustnessMetrics",
    "add_simulated_occlusion",
    "evaluate_test_r2",
    "modify_retinal_contrast",
    "retinal_fov_mask",
    "summarise_robustness",
]
