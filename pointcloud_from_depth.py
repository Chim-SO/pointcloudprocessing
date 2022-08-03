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
    depth_image = iio.imread('data/depth.png')

    # print properties:
    print(f"Image resolution: {depth_image.shape}")
    print(f"Data type: {depth_image.dtype}")
    print(f"Min value: {np.min(depth_image)}")
    print(f"Max value: {np.max(depth_image)}")

    # Compute depth grayscale:
    depth_grayscale = np.array(256 * depth_image / 0x0fff, dtype=np.uint8)
    iio.imwrite('output/depth_grayscale.png', depth_grayscale)

    # Display depth and grayscale image:
    fig, axs = plt.subplots(1, 2)
    axs[0].imshow(depth_image, cmap="gray")
    axs[0].set_title('Depth image')
    axs[1].imshow(depth_grayscale, cmap="gray")
    axs[1].set_title('Depth grayscale image')
    plt.show()

    # compute point cloud:
    scale = 1  # scale = 1000 if want to convert it to meters
    height, width = depth_image.shape
    pcd = []
    for i in range(height):
        for j in range(width):
            z = depth_image[i][j] / scale
            x = (j - CX_DEPTH) * depth_image[i][j] / FX_DEPTH
            y = ((height - i) - CY_DEPTH) * depth_image[i][j] / FY_DEPTH
            pcd.append([x, y, z])

    # visualization:
    # Convert to Open3D.PointCLoud:
    pcd_o3d = o3d.geometry.PointCloud()  # create point cloud object
    pcd_o3d.points = o3d.utility.Vector3dVector(pcd)  # set pcd_np as the point cloud points
    # Visualize:
    o3d.visualization.draw_geometries([pcd_o3d])
