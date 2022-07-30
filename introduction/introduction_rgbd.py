import open3d as o3d

if __name__ == '__main__':
    # read the color and the depth image:
    color_raw = o3d.io.read_image("../data/rgb.jpg")
    depth_raw = o3d.io.read_image("../data/depth.png")

    # create an rgbd image object:
    rgbd_image = o3d.geometry.RGBDImage.create_from_color_and_depth(
        color_raw, depth_raw, convert_rgb_to_intensity=False)
    # use the rgbd image to create point cloud:
    pcd = o3d.geometry.PointCloud.create_from_rgbd_image(
        rgbd_image,
        o3d.camera.PinholeCameraIntrinsic(
            o3d.camera.PinholeCameraIntrinsicParameters.PrimeSenseDefault))

    # visualize:
    o3d.visualization.draw_geometries([pcd])