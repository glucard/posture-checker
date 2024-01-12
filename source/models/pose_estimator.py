# Import TF and TF Hub libraries.
import tensorflow as tf
import tensorflow_hub as hub
import numpy as np

def load_image(image_path):
    image = tf.io.read_file(image_path)
    image = tf.compat.v1.image.decode_jpeg(image)
    image = tf.expand_dims(image, axis=0)
    # Resize and pad the image to keep the aspect ratio and fit the expected size.
    image = tf.cast(tf.image.resize_with_pad(image, 256, 256), dtype=tf.int32)
    return image

class PoseEstimator:
    def __init__(self):
        # Download the model from TF Hub.
        model = hub.load("https://www.kaggle.com/models/google/movenet/frameworks/TensorFlow2/variations/multipose-lightning/versions/1")
        self.movenet = model.signatures['serving_default']

    def predict(self, image):
        # Run model inference.
        outputs = self.movenet(image)
        output = outputs['output_0']
        keypoints = np.array(output[0])
        return keypoints

    def predict_path(self, image_path):
        # Load the input image.``
        image = load_image(image_path)
        keypoints = self.predict(image)
        return keypoints