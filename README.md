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
includes the examples of the first tutorial: [Introduction to Point Cloud Processing](https://medium.com/@chimso1994/introduction-to-point-cloud-processing-dbda9b167534).
    - [introduction_random_points.py](https://github.com/Chim-SO/pointcloudprocessing/blob/main/introduction/introduction_random_points.py) : creates a random point cloud and display it using Matplotlib.
    - [introduction_sampling.py](https://github.com/Chim-SO/pointcloudprocessing/blob/main/introduction/introduction_sampling.py) : samples point cloud from a mesh and display it using Open3D.
    - [introduction_np_o3d.py](https://github.com/Chim-SO/pointcloudprocessing/blob/main/introduction/introduction_np_o3d.py) : switching between Open3D and NumPy.
    - [introduction_rgbd.py](https://github.com/Chim-SO/pointcloudprocessing/blob/main/introduction/introduction_rgbd.py) : computing point clours from RGB-D data using Open3D functions.
    
- [pointcloudfromdepth](https://github.com/Chim-SO/pointcloudprocessing/tree/main/pointcloudfromdepth) folder:  
includes the examples of the second tutorial: [Point cloud computing from RGB-D images](https://medium.com/@chimso1994/point-cloud-computing-from-rgb-d-images-918414d57e80).
    - [pointcloud_from_depth.py](https://github.com/Chim-SO/pointcloudprocessing/blob/main/pointcloudfromdepth/pointcloud_from_depth.py) : compute point clouds from RGB-D data without using Open3D functions.
    - [colored_pointcloud_from_depth.py](https://github.com/Chim-SO/pointcloudprocessing/blob/main/pointcloudfromdepth/colored_pointcloud_from_depth.py) : compute colored point clouds.  
    
- [grounddetection](https://github.com/Chim-SO/pointcloudprocessing/tree/main/grounddetection) folder:  
Includes the examples of the third tutorial: [Understand point clouds: a simple ground detection algorithm]()
    - [computer_vision_coordinate_system.py](https://github.com/Chim-SO/pointcloudprocessing/blob/main/grounddetection/computer_vision_coordinate_system.py) : Understand the computer vision system coordinate.
    - [ground_detection.py](https://github.com/Chim-SO/pointcloudprocessing/blob/main/grounddetection/ground_detection.py) : A simple ground detection algorithm.
    - [organized_pointcloud.py](https://github.com/Chim-SO/pointcloudprocessing/blob/main/grounddetection/organized_pointcloud.py) : compute organized point cloud.

- [preprocessing](https://github.com/Chim-SO/pointcloudprocessing/tree/main/preprocessing) folder:  
Includes the examples of the 4th tutorial: [Point Cloud Filtering in Python](https://medium.com/@chimso1994/point-cloud-filtering-in-python-e8a06bbbcee5).
    - [crop_pointcloud_o3d.py](https://github.com/Chim-SO/pointcloudprocessing/blob/main/preprocessing/crop_pointcloud_o3d.py) : pass-through filter using Open3D.
    - [passthrough_filter_np.py](https://github.com/Chim-SO/pointcloudprocessing/blob/main/preprocessing/passthrough_filter_np.py) : a NumPy implementation of pass-through filter.
    - [downsampling.py](https://github.com/Chim-SO/pointcloudprocessing/blob/main/preprocessing/downsampling.py) : down-sampling methods.
    - [point_cloud_filtering.py](https://github.com/Chim-SO/pointcloudprocessing/blob/main/preprocessing/point_cloud_filtering.py) : outlier removal filters: statistical outlier removal and radius outlier removal demonstration.

# Requirements
- Open3D : 0.15.1
- NumPy : 1.21.6
