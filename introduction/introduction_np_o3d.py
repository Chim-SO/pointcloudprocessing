import numpy as np
import matplotlib.pyplot as plt
import open3d as o3d

if __name__ == '__main__':
    # Create numpy pointcloud:
    number_points = 2000
    pcd_np = np.random.rand(number_points, 3)

    # Convert to Open3D.PointCLoud:
    pcd_o3d = o3d.geometry.PointCloud()  # create point cloud object
    pcd_o3d.points = o3d.utility.Vector3dVector(pcd_np)  # set pcd_np as the point cloud points

    # Visualize:
    o3d.visualization.draw_geometries([pcd_o3d])

    # Read the bunny point cloud file:
    pcd_o3d = o3d.io.read_point_cloud("../data/bunny_pcd.ply")

    # Convert the open3d object to numpy:
    pcd_np = np.asarray(pcd_o3d.points)

    # Display using matplotlib:
    # Create Figure:
    fig, ax = plt.subplots(subplot_kw={"projection": "3d"})
    ax.scatter3D(pcd_np[:, 0], pcd_np[:, 2], pcd_np[:, 1])
    # label the axes
    ax.set_xlabel("X")
    ax.set_ylabel("Y")
    ax.set_zlabel("Z")
    ax.set_title("Bunny Point Cloud")
    # display:
    plt.show()
