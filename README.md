# SLAM

## GOAL
* [ ] write from scratch no library
* [ ] it should work!!

---

## How to write?  what chat GPT told.

1.  Video Preprocessing: Preprocess the video to remove noise and stabilize the camera motion.
    
2.  Feature Detection and Tracking: Detect and track keypoints in the video, such as corners or edges, that can be used to estimate the vehicle's motion and create a map of the environment.
    
3.  Pose Estimation: Estimate the vehicle's motion using the tracked keypoints and the motion between frames.
    
4.  Map Building: Use the estimated vehicle motion to create a map of the environment, either by updating a map generated from previous frames or by creating a new map from scratch.
    
5.  Loop Closure: Detect and correct for loops in the trajectory, where the vehicle revisits a location it has already been to.
    
6.  Optimization: Refine the map and pose estimates by using non-linear optimization techniques like Bundle Adjustment.


## Detailed Explantion.

1.  Video Preprocessing:
    
    -   Camera Calibration: Calibrate the camera parameters, such as intrinsic matrix, distortion coefficients, and extrinsic parameters, to correct for lens distortion and other artifacts.
    -   Undistortion: Remove lens distortion from the video frames using the calibrated camera parameters.
    -   Color Correction: Adjust the brightness, contrast, and color of the video frames to improve image quality.
2.  Feature Detection and Tracking:
    
    -   Feature Detection: Use computer vision techniques, such as Harris corner detection, SIFT, or SURF, to detect distinctive features in the video frames.
    -   Feature Tracking: Track the detected features from one frame to the next using techniques like the Lucas-Kanade optical flow algorithm.
3.  Pose Estimation:
    
    -   Estimate the camera pose, i.e., its position and orientation, at each frame based on the tracked features.
    -   Two-View Geometry: Given the pose of the camera at two frames, use the relative positions of the matched features to estimate the essential matrix, which can be decomposed to obtain the relative rotation and translation of the camera.
    -   Bundle Adjustment: Refine the camera pose estimates by minimizing the reprojection error of the matched features using non-linear optimization techniques like Bundle Adjustment.
4.  Map Building:
    
    -   Initialize the map with the first frame and the estimated camera pose.
    -   As new frames are processed, use the estimated camera pose to update the map, either by adding new landmarks or updating existing landmarks.
    -   Use techniques like triangulation or depth estimation to estimate the 3D positions of the landmarks in the map.
5.  Loop Closure:
    
    -   Detect when the vehicle revisits a location it has already been to, known as a loop, by comparing the current frame to the map.
    -   Correct the trajectory by updating the map and camera poses to account for the loop.
6.  Optimization:
    
    -   Refine the map and camera pose estimates using non-linear optimization techniques like Bundle Adjustment.
    -   Optimize the map and poses globally to reduce errors and improve accuracy.
