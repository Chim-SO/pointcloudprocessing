import open3d as o3d

if __name__ == '__main__':
    # Download data from Open3D repo:
    demo_crop_data = o3d.data.DemoCropPointCloud()

    # Import point cloud and display it:
    pcd = o3d.io.read_point_cloud(demo_crop_data.point_cloud_path)
    o3d.visualization.draw_geometries([pcd])

    # Read from a json file the polygon volume to be selected:
    polygon_volume = o3d.visualization.read_selection_polygon_volume(demo_crop_data.cropped_json_path)

    # Crop the point cloud to get the points that are inside the polygon and display it:
    pcd_cropped = polygon_volume.crop_point_cloud(pcd)
    o3d.visualization.draw_geometries([pcd_cropped])
