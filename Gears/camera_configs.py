# filename: camera_configs.py
import cv2
import numpy as np

left_camera_matrix = np.array([[3213.08, 0., 600.64723],
                               [0.,3060.75, 186.58058],
                               [0., 0., 1.]])
left_distortion = np.array([[-0.1426, -0.4962, -0.0150, -0.0744, 0.00000]])

right_camera_matrix = np.array([[1004.37, 0., 400.00856],
                                [0., 1004.52, 269.37140],
                                [0., 0., 1.]])
right_distortion = np.array([[-0.5450, -0.2870, -0.0110, -0.0329, 0.00000]])

R = np.array(([0.9999,-0.0019,0.0101],# Rotation vector
              [0.0021,0.9999,-0.0138],
              [-0.0100,0.0138,0.9999]))
T = np.array([-150.5252,-4.888,11.9268])  # transformation vector

size = (1280,760)  # image size

# stereoRectify
R1, R2, P1, P2, Q, validPixROI1, validPixROI2 = cv2.stereoRectify(left_camera_matrix, left_distortion,right_camera_matrix, right_distortion, size, R,T)
# modify map
left_map1, left_map2 = cv2.initUndistortRectifyMap(left_camera_matrix, left_distortion, R1, P1, size, cv2.CV_16SC2)
right_map1, right_map2 = cv2.initUndistortRectifyMap(right_camera_matrix, right_distortion, R2, P2, size, cv2.CV_16SC2)