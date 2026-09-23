# Provenance: RECONSTRUCTED reusable code; historical execution not established.
"""Lazy DINOv2 CLS-token embedding extraction."""

from __future__ import annotations

from typing import Any

import numpy as np

DEFAULT_MODEL_NAME = "facebook/dinov2-base"


class DINOv2Embedder:
    """Load a Hugging Face DINOv2 model and return its CLS-token embedding."""

    def __init__(self, model_name: str = DEFAULT_MODEL_NAME, device: str = "cpu") -> None:
        try:
            import torch
            from transformers import AutoImageProcessor, AutoModel
        except ImportError as exc:  # pragma: no cover - depends on optional models extra
            raise ImportError("install ConceptSMILE with the 'models' extra") from exc

        self._torch = torch
        self.device = device
        self.processor = AutoImageProcessor.from_pretrained(model_name)
        self.model = AutoModel.from_pretrained(model_name).to(device)
        self.model.eval()

    def __call__(self, image: Any) -> np.ndarray:
        """Return the ``last_hidden_state[:, 0, :]`` CLS embedding."""
        inputs = self.processor(images=image, return_tensors="pt")
        inputs = {key: value.to(self.device) for key, value in inputs.items()}
        with self._torch.no_grad():
            outputs = self.model(**inputs)
        return (
            outputs.last_hidden_state[:, 0, :]
            .squeeze(0)
            .detach()
            .cpu()
            .numpy()
            .astype(np.float32)
        )

