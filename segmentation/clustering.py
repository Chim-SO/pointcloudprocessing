import numpy as np
import open3d as o3d
from sklearn.cluster import KMeans, DBSCAN
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler

if __name__ == '__main__':
    # Read point cloud:
    pcd = o3d.io.read_point_cloud("../data/depth_2_pcd_downsampled.ply")
    # Get points and transform it to a numpy array:
    points = np.asarray(pcd.points)

    # Normalisation:
    scaled_points = StandardScaler().fit_transform(points)

    # Clustering:
    model = DBSCAN(eps=0.15, min_samples=10)
    # model = KMeans(n_clusters=4)
    model.fit(scaled_points)

    # Get labels:
    labels = model.labels_
    # Get the number of colors:
    n_clusters = len(set(labels))

    # Mapping the labels classes to a color map:
    colors = plt.get_cmap("tab20")(labels / (n_clusters if n_clusters > 0 else 1))
    # Attribute to noise the black color:
    colors[labels < 0] = 0
    # Update points colors:
    pcd.colors = o3d.utility.Vector3dVector(colors[:, :3])

    # Display:
    o3d.visualization.draw_geometries([pcd])