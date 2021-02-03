# MesentericRadiomics
Script to compute features and fit radiomics models as done in the paper
"Prediction of symptomatic metastatic mesenteric mass in patients with
small intestinal neuroendocrine tumors using CT based radiomics and
systematic clinical evaluation."
A. Blazevic & M. P. A. Starmans et al. 2021.

## Installation
For the feature extraction, only the PREDICT package, version 3.1.13,
and the subsequent dependencies are required, which can be installed through pip:

    pip install "PREDICT==3.1.13"

For the model optimization, additionally WORC, version 3.4.0, is required:

    pip install "WORC==3.4.0"

## Usage
The ExtractFeatures.py script can be used to extract all features. We provided
you with the exact same configuration file that was used in the study. The
script can be easily modified to use your own data instead of the
provided example data and requires:

1. An image in ITK Image format, e.g. .nii, .nii.gz, .tiff, .nrrd, .raw
2. A segmentation in ITK Image format.
3. Optionally, metadata in DCM format

Extracting the features from the example data should take less than 10 seconds.
Using a larger image and/or mask may result in a longer computation time.

Documentation for the model optimization is provided in the respective script.

## Known Issues
See the WORC FAQ: https://worc.readthedocs.io/en/v3.4.0/static/faq.html
