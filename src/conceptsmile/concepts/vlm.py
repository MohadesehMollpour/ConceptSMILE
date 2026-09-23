# Provenance: RECONSTRUCTED reusable code; historical execution not established.
"""Qwen2.5-VL prompt and token-confidence parsing from the submitted notebook."""

from __future__ import annotations

from collections.abc import Mapping, Sequence
from typing import Any

CONCEPT_ORDER = ("blood_vessels", "lesion", "optic_disc")

RETINAL_CONCEPT_PROMPT = """You are an expert retinal image analyst.

Analyze this retinal image and evaluate only these three concepts:

1. blood_vessels = visible retinal blood vessels
2. lesion = any visible retinal abnormality or pathological sign, including
   hemorrhage, exudate, microaneurysm, edema, or other anomaly
3. optic_disc = visible optic disc

Decision rule:
- Answer "yes" only if the concept is clearly visible in the image.
- Answer "no" if the concept is not visible or if you are uncertain.

Return only one valid JSON object.
Do not use markdown.
Do not add explanation.
Do not add extra text.
Do not include any concept other than these three.

Output format:
{
  "blood_vessels": "yes",
  "lesion": "yes",
  "optic_disc": "yes"
}
"""

_FIELD_TOKEN_MAP = {
    "blood_vessels": ("blood", "_v", "ess", "els"),
    "lesion": ("les", "ion"),
    "optic_disc": ("optic", "_disc"),
}


def build_qwen_messages(image: Any) -> list[dict[str, Any]]:
    """Build the fixed image-and-text message expected by Qwen2.5-VL."""
    return [
        {
            "role": "user",
            "content": [
                {"type": "image", "image": image},
                {"type": "text", "text": RETINAL_CONCEPT_PROMPT},
            ],
        }
    ]


def extract_confidences_from_token_scores(
    token_scores: Sequence[Mapping[str, Any]],
) -> dict[str, dict[str, float | str | None]]:
    """Reproduce the notebook's tokenizer-piece confidence extraction.

    This implementation is intentionally traceable to the notebook. It is tied
    to the recorded Qwen tokenizer pieces and should be revalidated if the model
    or tokenizer revision changes.
    """
    results: dict[str, dict[str, float | str | None]] = {}
    index = 0
    concept_index = 0

    while index < len(token_scores) and concept_index < len(CONCEPT_ORDER):
        concept = CONCEPT_ORDER[concept_index]
        expected = _FIELD_TOKEN_MAP[concept]
        observed = tuple(
            str(token_scores[index + offset].get("token", ""))
            for offset in range(len(expected))
            if index + offset < len(token_scores)
        )

        if observed != expected:
            index += 1
            continue

        cursor = index + len(expected)
        answer: str | None = None
        confidence: float | None = None

        while cursor < len(token_scores):
            token = (
                str(token_scores[cursor].get("token", ""))
                .replace("Ġ", "")
                .replace('"', "")
                .strip()
                .lower()
            )
            if token in {"yes", "no"}:
                answer = token
                probability = float(token_scores[cursor]["probability_like"])
                confidence = probability if token == "yes" else 1.0 - probability
                break
            cursor += 1

        results[concept] = {"answer": answer, "confidence": confidence}
        concept_index += 1
        index = cursor if cursor > index else index + 1

    return results
