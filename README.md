# pointcloudprocessing
This repository contains the code examples of my medium tutorial "Point Cloud Processing".  
"Point Cloud Processing" tutorial is beginner-friendly in which we will simply introduce the point cloud processing pipeline from data preparation to data segmentation and classification.

# Content
In this repository you will find:
- [data](https://github.com/Chim-SO/pointcloudprocessing/tree/main/data) folder:  
Includes the input files that are used for demonstration.

- [output](https://github.com/Chim-SO/pointcloudprocessing/tree/main/output) folder:  
Includes some saved output data.

- [introduction](https://github.com/Chim-SO/pointcloudprocessing/tree/main/introduction) folder:  
includes the examples of the first tutorial: [Introduction to Point Cloud Processing]().
    - [introduction_random_points.py](https://github.com/Chim-SO/pointcloudprocessing/blob/main/introduction/introduction_random_points.py) : creates a random point cloud and display it using Matplotlib.
    - [introduction_sampling.py](https://github.com/Chim-SO/pointcloudprocessing/blob/main/introduction/introduction_sampling.py) : samples point cloud from a mesh and display it using Open3D.
    - [introduction_np_o3d.py](https://github.com/Chim-SO/pointcloudprocessing/blob/main/introduction/introduction_np_o3d.py) : switching between Open3D and NumPy.
    - [introduction_rgbd.py](https://github.com/Chim-SO/pointcloudprocessing/blob/main/introduction/introduction_rgbd.py) : computing point clours from RGB-D data using Open3D functions.
    
- [pointcloudfromdepth](https://github.com/Chim-SO/pointcloudprocessing/tree/main/pointcloudfromdepth) folder:  
includes the examples of the second tutorial: [Point cloud computing from RGB-D images]().
    - [pointcloud_from_depth.py](https://github.com/Chim-SO/pointcloudprocessing/blob/main/pointcloudfromdepth/pointcloud_from_depth.py) : compute point clouds from RGB-D data without using Open3D functions.
    - [colored_pointcloud_from_depth.py](https://github.com/Chim-SO/pointcloudprocessing/blob/main/pointcloudfromdepth/colored_pointcloud_from_depth.py) : compute colored point clouds.

# Requirements
- Open3D 
- NumPy
