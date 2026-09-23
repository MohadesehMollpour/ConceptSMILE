import numpy as np

from conceptsmile.concepts.medsam import mask_bbox, mask_confidence, pool_medsam_embedding
from conceptsmile.concepts.vlm import extract_confidences_from_token_scores
from conceptsmile.robustness.acquisition import add_simulated_occlusion, modify_retinal_contrast


def test_vlm_token_parser_matches_notebook_rule():
    rows = [
        {"token": "blood", "probability_like": 1.0},
        {"token": "_v", "probability_like": 1.0},
        {"token": "ess", "probability_like": 1.0},
        {"token": "els", "probability_like": 1.0},
        {"token": "yes", "probability_like": 0.9},
        {"token": "les", "probability_like": 1.0},
        {"token": "ion", "probability_like": 1.0},
        {"token": "no", "probability_like": 0.8},
        {"token": "optic", "probability_like": 1.0},
        {"token": "_disc", "probability_like": 1.0},
        {"token": "yes", "probability_like": 0.7},
    ]
    result = extract_confidences_from_token_scores(rows)

    assert result["blood_vessels"]["confidence"] == 0.9
    assert np.isclose(result["lesion"]["confidence"], 0.2)
    assert result["optic_disc"]["confidence"] == 0.7


def test_medsam_helpers():
    mask = np.array([[False, True], [False, True]])
    soft = np.array([[0.1, 0.6], [0.2, 0.8]])

    assert mask_bbox(mask) == (1, 0, 1, 1)
    assert np.isclose(mask_confidence(soft), 0.7)
    assert pool_medsam_embedding(np.ones((1, 2, 3, 3))).shape == (2,)


def test_acquisition_functions_preserve_shape():
    image = np.zeros((10, 10, 3), dtype=np.uint8)
    image[1:9, 1:9] = 100

    assert modify_retinal_contrast(image, 1.0).shape == image.shape
    assert add_simulated_occlusion(image, 2).shape == image.shape
    assert np.array_equal(add_simulated_occlusion(image, 0), image)

