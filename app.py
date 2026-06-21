from src.camera_controller import CameraController

controller = CameraController()

controller.run()

import mediapipe as mp
from mediapipe.tasks import python
from mediapipe.tasks.python import vision

# 1. Create options for the Hand Landmarker
hand_options = vision.HandLandmarkerOptions(
    base_options=python.BaseOptions(model_asset_path='hand_landmarker.task')
)

# 2. Create options for the Pose Landmarker
pose_options = vision.PoseLandmarkerOptions(
    base_options=python.BaseOptions(model_asset_path='pose_landmarker_full.task')
)

print("Models loaded successfully!")