import imageio.v3 as iio
import numpy as np
import matplotlib.pyplot as plt
import open3d as o3d


def compute_pcd_nested_loops(depth_im):
    """
    Compute the point cloud using nested loops.
    This function is written for demonstration purposes.
    It takes time.
    :param depth_im: a depth image
    :return: the computed point cloud
    """
    height, width = depth_im.shape
    pcd = []
    for i in range(height):
        for j in range(width):
            z = depth_image[i][j]
            x = (j - CX_DEPTH) * depth_im[i][j] / FX_DEPTH
            y = (i - CY_DEPTH) * depth_im[i][j] / FY_DEPTH
            pcd.append([x, y, z])
    return pcd


def compute_pcd_vectorization(depth_im):
    """
    This function use victorization operations to optimize time.
    We can do better by computing constants first.
    Please see the main function.
    :param depth_im: a depth image
    :return: the computed point cloud
    """
    # get depth resolution:
    height, width = depth_im.shape
    # compute indices:
    ii = np.tile(range(width), height)
    jj = np.repeat(range(height), width)
    # rechape depth image
    z = depth_im.reshape(height * width)
    # compute pcd:
    pcd = np.array([(ii - CX_DEPTH) * z / FX_DEPTH,
                    (jj - CY_DEPTH) * z / FY_DEPTH,
                    z]).transpose()
    return pcd


if __name__ == '__main__':
    print(np.ndindex(480, 640))
    # Camera parameters:
    FX_DEPTH = 5.8262448167737955e+02
    FY_DEPTH = 5.8269103270988637e+02
    CX_DEPTH = 3.1304475870804731e+02
    CY_DEPTH = 2.3844389626620386e+02

    # Read depth image:
    depth_image = iio.imread('../data/depth.png')

    # print properties:
    print(f"Image resolution: {depth_image.shape}")
    print(f"Data type: {depth_image.dtype}")
    print(f"Min value: {np.min(depth_image)}")
    print(f"Max value: {np.max(depth_image)}")

    # Compute depth grayscale:
    depth_grayscale = np.array(256 * depth_image / 0x0fff, dtype=np.uint8)
    iio.imwrite('../output/depth_grayscale.png', depth_grayscale)

    # Display depth and grayscale image:
    fig, axs = plt.subplots(1, 2)
    axs[0].imshow(depth_image, cmap="gray")
    axs[0].set_title('Depth image')
    axs[1].imshow(depth_grayscale, cmap="gray")
    axs[1].set_title('Depth grayscale image')
    plt.show()

    # get depth image resolution:
    height, width = depth_image.shape
    # compute indices:
    ii = np.tile(range(width), height)
    jj = np.repeat(range(height), width)
    # Compute constants:
    xx = (jj - CX_DEPTH) / FX_DEPTH
    yy = (ii - CY_DEPTH) / FY_DEPTH
    # transform depth image to vector of z:
    length = height * width
    z = depth_image.reshape(height * width)
    # compute point cloud
    pcd = np.array([xx * z, yy * z, z]).transpose()

    # visualization:
    # Convert to Open3D.PointCLoud:
    pcd_o3d = o3d.geometry.PointCloud()  # create point cloud object
    pcd_o3d.points = o3d.utility.Vector3dVector(pcd)  # set pcd_np as the point cloud points

    # Visualize:
    o3d.visualization.draw_geometries([pcd_o3d])
