from source.models import PoseEstimator

def debugging():
    pose_estimator = PoseEstimator()
    keypoints = pose_estimator.predict_path("image.jpg")
    for keypoint in keypoints:
        ymin, xmin, ymax, xmax, keypoint_score = keypoint[-5:]
        if keypoint_score > 0.5:
            print(ymin, xmin, ymax, xmax, keypoint_score)
        print(keypoint_score)

if __name__ == "__main__":
    debugging()