"""ConceptSMILE acquisition-robustness utilities.

This package contains utilities for the additional robustness
analysis reported in Section 5.3 of the manuscript.
"""

from .acquisition import (
    add_simulated_occlusion,
    modify_retinal_contrast,
    retinal_fov_mask,
)

__all__ = [
    "add_simulated_occlusion",
    "modify_retinal_contrast",
    "retinal_fov_mask",
]
