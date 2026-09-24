# Dataset acquisition

Obtain images independently from the original dataset providers. No source dataset,
retinal image collection, annotation bundle, model weight, or third-party logo is
redistributed by this repository.

The author-confirmed ConceptSMILE evaluation subset is documented in:

`data/manifests/paper_40_images.csv`

It contains 40 retinal fundus image identifiers in total, with 10 images each from
HRF, APTOS 2019, ODIR-5K, and IDRiD.

The manifest identifies the manuscript evaluation subset. Exact source filenames,
extensions, checksums, and provider-side annotation mappings remain blank or
unverified where they have not been independently established.

| Dataset | Provider/source link | Verification and acquisition guidance |
| --- | --- | --- |
| HRF | [FAU HRF](https://www5.cs.fau.de/research/data/fundus-images/) | Obtain the dataset from the provider and follow its attribution and licence requirements. Provider-supplied annotations must not automatically be assumed to be the exact references used in the historical ConceptSMILE experiments unless that mapping is verified. |
| APTOS 2019 | [Kaggle competition data](https://www.kaggle.com/competitions/aptos2019-blindness-detection/data) | Sign in through Kaggle where required and review the competition access and usage conditions. The ConceptSMILE repository does not redistribute APTOS images. |
| ODIR-5K | [ODIR challenge dataset](https://odir2019.grand-challenge.org/dataset/) | Obtain the dataset through the official challenge/provider instructions and review its terms before use. The repository does not infer redistribution rights from availability of the dataset online. |
| IDRiD | [IDRiD challenge data](https://idrid.grand-challenge.org/Data/) | Obtain the dataset through the official challenge/provider instructions and review its access and usage terms before use. |

A practical local structure for a future reproduction run is:

```text
data/
  raw/
    HRF/
    APTOS_2019/
    ODIR_5K/
    IDRiD/
