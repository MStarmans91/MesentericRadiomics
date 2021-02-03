import WORC
import os
import glob
from classes import switch


def editconfig(config):
    """Function to edit the WORC configuration for the Mesenteric Fibrosis study."""

    # No Normalization for CT
    config['Preprocessing']['Normalize'] = 'False'

    # Only used for naming conventions
    config['ImageFeatures']['image_type'] = 'CT'

    # Set label to predict
    config['Labels']['label_names'] = 'Operated'
    config['Labels']['modus'] = 'singlelabel'

    return config


# Inputs
name = 'WORC_MF'
current_path = os.path.dirname(os.path.abspath(__file__))
label_file = os.path.join(current_path, 'ExampleData', 'pinfo_MF.txt')
semantics_file = os.path.join(current_path, 'ExampleData', 'sem_MF.txt')
config = os.path.join(current_path, 'ExampleData', 'config_modeloptimization.ini')

# Altough you can also the features, we will supply the raw image
images = glob.glob(os.path.join(current_path, 'ExampleData', 'ExampleImage*.nii.gz'))
images.sort()

segmentations = glob.glob(os.path.join(current_path, 'ExampleData', 'ExampleSegmentation*.nii.gz'))
segmentations.sort()

metadatas = glob.glob(os.path.join(current_path, 'ExampleData', 'ExampleDCM*.dcm'))
metadatas.sort()

# As we only have a single patient/object, hence we will repeat it to mimick
# having multiple. We do this in a dictionary, in which the keys
# correspond to the "patient" names also used in the label and semantics files
patient_names = ['Patient-' + str(i).zfill(3) for i in range(0, 10)]
images = {k: v for k, v in zip(patient_names, images)}
segmentations = {k: v for k, v in zip(patient_names, segmentations)}
metadatas = {k: v for k, v in zip(patient_names, metadatas)}

# Create the WORC network
network = WORC.WORC(name)

# Instead of supplying the .ini file to the network, we will create
# the config object for you directly from WORC,
# so you can interact with it if you want.
# Altough it is a configparser object, it works similar as a dictionary
config = network.defaultconfig()

# The default config from the WORC 2.1.3 version we used, was a stripped
# version in order to get a quick result. The actual default used for normal
# experiments is created through the editconfig function.
config = editconfig(config)

# NOTE: Since we now only use 10 "patients" in this example, we turn of the
# resampling options. Do not do this for the full experiment.
config['Resampling']['Use'] = '0.0'

# Append the sources to be used
network.images_train.append(images)
network.segmentations_train.append(segmentations)
network.metadata.train.append(metadatas)
network.semantics_train.append(semantics_file)

# NOTE: When using multiple ROIs, simply append an extra set of images and segmentations

# Build, set, and execture the network
network.build()
network.set()
network.execute()
