#! /bin/env python3

from re import S
import cv2
import datetime
import matplotlib.pyplot as plt
import numpy as np
import os
import pandas as pd


def main():
    # reading the poses file and ensuring it's in a better format
    poses = pd.read_csv(
        "~/Documents/kitti/odometry/dataset/poses/00.txt", delimiter=" ", header=None
    )
    print("Shape of poses: ", poses.shape)

    # removing the poses.head() call to use all the poses
    number_of_poses = len(poses)
    print("Number of poses: ", number_of_poses)

    # reshape the first pose
    first_pose = np.array(poses.iloc[0]).reshape((3, 4)).round(2)
    print("First pose: \n", first_pose)

    # initialize the ground truth array
    gt = np.zeros((number_of_poses, 3, 4))
    for i in range(number_of_poses):
        gt[i] = np.array(poses.iloc[i]).reshape((3, 4))

    # dot product with the second pose and origin
    origin = np.array([0, 0, 0, 1])
    dot_product_result = gt[1].dot(origin)
    print("Dot product result for second pose: ", dot_product_result)

    # setting up the plot
    fig = plt.figure(figsize=(7, 6))
    ax = fig.add_subplot(111, projection="3d")

    # plotting the ground truth positions
    ax.plot(gt[:, 0, 3], gt[:, 1, 3], gt[:, 2, 3])
    ax.set_xlabel("x")
    ax.set_ylabel("y")
    ax.set_zlabel("z")

    # setting axis limits
    ax.set_xlim(-200, 300)
    ax.set_ylim(-20, 0)
    ax.set_zlim(0, 400)

    ax.view_init(elev=-40, azim=270)

    plt.show()


if __name__ == "__main__":
    main()
