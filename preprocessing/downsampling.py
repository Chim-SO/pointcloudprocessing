import open3d as o3d
import numpy as np

if __name__ == '__main__':
    # Read point cloud:
    pcd = o3d.io.read_point_cloud("../data/depth_2_pcd.ply")

    # Random down-sampling:
    random_pcd = pcd.random_down_sample(sampling_ratio=0.005)

    # Uniform down-sampling:
    uniform_pcd = pcd.uniform_down_sample(every_k_points=200)

    # Voxel down-sampling:
    voxel_pcd = pcd.voxel_down_sample(voxel_size=0.4)

    # Translating point clouds and updating colors to display:
    points = np.asarray(random_pcd.points)
    points += [-3, 3, 0]
    random_pcd.points = o3d.utility.Vector3dVector(points)

    points = np.asarray(uniform_pcd.points)
    points += [0, 3, 0]
    uniform_pcd.points = o3d.utility.Vector3dVector(points)

    points = np.asarray(voxel_pcd.points)
    points += [3, 3, 0]
    voxel_pcd.points = o3d.utility.Vector3dVector(points)

    # Display:
    o3d.visualization.draw_geometries([pcd, random_pcd, uniform_pcd, voxel_pcd])


