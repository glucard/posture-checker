from source.models import PoseEstimator
from source.camera import Camera
from matplotlib import pyplot as plt
import cv2

def debugging():
    """
    # pose estimator
    pose_estimator = PoseEstimator()
    keypoints = pose_estimator.predict_path("image.jpg")
    for keypoint in keypoints:
        ymin, xmin, ymax, xmax, keypoint_score = keypoint[-5:]
        if keypoint_score > 0.5:
            print(ymin, xmin, ymax, xmax, keypoint_score)
        print(keypoint_score)
    """
    # camera
    frame = Camera.take_photo_eco()
    print(type(frame), frame.shape)
    cv2.imwrite("frame", frame)

if __name__ == "__main__":
    debugging()