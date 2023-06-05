import tensorflow as tf
import os
import numpy as np
from google.colab import files
from tensorflow.keras.utils import load_img, img_to_array

uploaded = files.upload()

model_h5 = 'my_model.h5'
model=tf.keras.models.load_model(model_h5)