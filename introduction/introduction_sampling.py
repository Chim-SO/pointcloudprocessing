# reference: http://graphics.im.ntu.edu.tw/~robin/courses/cg03/model/
import open3d as o3d

if __name__ == '__main__':
    # Read the PLY file:
    mesh = o3d.io.read_triangle_mesh("../data/bunny.ply")

    # Import data from open3D:
    # bunny = o3d.data.BunnyMesh()
    # mesh = o3d.io.read_triangle_mesh(bunny.path)

    # Visualize:
    mesh.compute_vertex_normals() # compute normals for vertices or faces
    o3d.visualization.draw_geometries([mesh])

    # Sample 1000 points:
    pcd = mesh.sample_points_uniformly(number_of_points=1000)

    # visualize:
    o3d.visualization.draw_geometries([pcd])

    # Save into ply file:
    o3d.io.write_point_cloud("../output/bunny_pcd.ply", pcd)
