# Mask RCNN library
import mrcnn.model as modellib
from mrcnn.config import Config

import os

class FoodConfig(Config):
    """Configuration for training on the custom  dataset.
    Derives from the base Config class and overrides some values.
    """
    # Give the configuration a recognizable name
    NAME = "CapturEat"

    GPU = 1

    IMAGES_PER_GPU = 1

    NUM_CLASSES = 1 + 3  # Background + 3 Food Classes

    BACKBONE = 'resnet50'

    # Number of training steps per epoch
    STEPS_PER_EPOCH = 200

    # Set Image size
    IMAGE_MAX_DIM = 256
    IMAGE_MIN_DIM = 256
    
ROOT_DIR = os.getcwd()
LOG_DIR = os.path.join(ROOT_DIR, "logs")
MODEL_DIR = os.path.join(LOG_DIR, "model/model.h5")

def load_model():
    # Create a new config object
    config = FoodConfig()
    model = modellib.MaskRCNN(mode='inference',
                               config=config,
                               model_dir=LOG_DIR)
    
    # Load trained weights (fill in path to trained weights here)
    model.load_weights(MODEL_DIR, by_name=True)
    model.keras_model._make_predict_function()
    
    return model