import imageio.v3 as iio
import matplotlib.pyplot as plt
import numpy
import numpy as np
import open3d as o3d

if __name__ == '__main__':
    # Read point cloud
    pcd = o3d.io.read_point_cloud("../data/depth_2_pcd.ply")
    # Create a 3D coordinate system:
    origin = o3d.geometry.TriangleMesh.create_coordinate_frame(size=0.5)

    # Green color:
    GREEN = [0., 1., 0.]

    # Define a threshold:
    THRESHOLD = 0.075

    # Get the max value along the y-axis:
    y_max = max(pcd.points, key=lambda x: x[1])[1]

    # Get the original points color to be updated:
    pcd_colors = np.asarray(pcd.colors)

    # Number of points:
    n_points = pcd_colors.shape[0]

    # update color:
    for i in range(n_points):
        # if the current point is aground point:
        if pcd.points[i][1] >= y_max - THRESHOLD:
            pcd_colors[i] = GREEN  # color it green

    pcd.colors = o3d.utility.Vector3dVector(pcd_colors)

    # Display:
    o3d.visualization.draw_geometries([pcd, origin])
