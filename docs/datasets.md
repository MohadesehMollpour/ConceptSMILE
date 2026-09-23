# Dataset acquisition

Obtain images independently from providers. No dataset, mask image, retinal visualisation or third-party logo is bundled. The historical 40-image manifest is NOT AVAILABLE; the two mirror basenames in notebooks are not verified official identifiers or proof of paper membership.

| Dataset | Provider/source link | Verification and acquisition guidance (22 September 2026) |
| --- | --- | --- |
| HRF | [FAU HRF](https://www5.cs.fau.de/research/data/fundus-images/) | Provider page retrieved; follow its download links and attribution requirements. It states CC BY 4.0 and provides expert vessel masks. This does not establish that historical ConceptSMILE used them. |
| APTOS 2019 | [Kaggle competition data](https://www.kaggle.com/competitions/aptos2019-blindness-detection/data) | Endpoint reached but contents not exposed to retrieval; sign in and review competition rules/access conditions. No licence inferred. |
| ODIR-5K | [ODIR challenge dataset](https://odir2019.grand-challenge.org/dataset/) | Official challenge dataset URL corroborated in search; direct retrieval returned 403. Use challenge access/download instructions and review terms. No redistribution clearance inferred. |
| IDRiD | [IDRiD challenge data](https://idrid.grand-challenge.org/Data/) | Existing source URL retained; direct retrieval returned 403 and terms not verified. Consult challenge provider before use. |

Use a private local root with HRF/, APTOS_2019/, ODIR_5K/ and IDRiD/ directories. This is a suggested layout, not a historical directory structure or an implemented full-data loader. Store any future verified identifiers, checksums, annotation source and selection method with each run. Do not assume every dataset supplies every concept's independent mask.

The original code loads diabetes/image1.png and diabetes/image1001.png from a third-party Kaggle ODIR mirror. The mapping back to official patient/image IDs is not established. Do not treat either filename as a patient identifier or invent patient metadata.
