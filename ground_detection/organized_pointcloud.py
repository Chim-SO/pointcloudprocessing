import imageio.v3 as iio
import numpy as np
import matplotlib.pyplot as plt
import open3d as o3d

if __name__ == '__main__':
    # Camera parameters:
    FX_DEPTH = 5.8262448167737955e+02
    FY_DEPTH = 5.8269103270988637e+02
    CX_DEPTH = 3.1304475870804731e+02
    CY_DEPTH = 2.3844389626620386e+02

    # Read depth image:
    depth_image = iio.imread('../data/depth_2.png')
    # Compute the grayscale image:
    depth_grayscale = np.array(256 * depth_image / 0x0fff, dtype=np.uint8)
    # Convert a grayscale image to a 3-channel image:
    depth_grayscale = np.stack((depth_grayscale,) * 3, axis=-1)

    # get depth image resolution:
    height, width = depth_image.shape
    # compute indices:
    jj = np.tile(range(width), height).reshape((height, width))
    ii = np.repeat(range(height), width).reshape((height, width))
    # Compute constants:
    xx = (jj - CX_DEPTH) / FX_DEPTH
    yy = (ii - CY_DEPTH) / FY_DEPTH
    # compute organised point cloud:
    organized_pcd = np.dstack((xx * depth_image, yy * depth_image, depth_image))

    # Ground_detection:
    THRESHOLD = 0.075 * 1000  # Define a threshold
    y_max = max(organized_pcd.reshape((height * width, 3)), key=lambda x: x[1])[
        1]  # Get the max value along the y-axis

    # Set the ground pixels to green:
    for i in range(height):
        for j in range(width):
            if organized_pcd[i][j][1] >= y_max - THRESHOLD:
                depth_grayscale[i][j] = [0, 255, 0]  # Update the depth image

    # Display depth_grayscale:
    plt.imshow(depth_grayscale)
    plt.show()
