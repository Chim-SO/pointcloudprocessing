import open3d as o3d
import numpy as np

if __name__ == '__main__':
    # Read point cloud
    pcd = o3d.io.read_point_cloud("../data/depth_2_pcd.ply")

    # Convert it into numpy array:
    points = np.asarray(pcd.points)
    # Create passthrough filter:
    pass_through_filter = np.logical_and(points[:, 2] >= 0.8, points[:, 2] <= 2.5)
    # Get the points that passed through the filter:
    filtered_points = points[pass_through_filter]

    # Create filtered open3D point cloud:
    filtered_pcd = o3d.geometry.PointCloud()  # create point cloud object
    filtered_pcd.points = o3d.utility.Vector3dVector(filtered_points)  # set pcd_np as the point cloud points

    # To preserve the color information in case of colored point cloud:
    colors = np.asarray(pcd.colors)
    filtered_pcd.colors = o3d.utility.Vector3dVector(colors[pass_through_filter])

    # Display:
    o3d.visualization.draw_geometries([filtered_pcd])

    # Or change the color of the points:
    colors[pass_through_filter] = [0., 1., 0.]
    pcd.colors = o3d.utility.Vector3dVector(colors)
    o3d.visualization.draw_geometries([pcd])

