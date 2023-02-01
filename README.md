# Real-time object detection using embedded machine learning.

## Conda environment

**create environment**
```
conda env create -f conda.yml
```

**actvate environment**
```
conda activate rtobjectdect_venv
```

**update environment**
```
conda env update --name rtobjectdect_venv --file conda.yml --prune
```
---

## Realsense on Jetson Nano

To install RealSense viewer, see the instruction on: [Install RealSense Camera in 5 minutes – Jetson Nano](https://jetsonhacks.com/2019/12/22/install-realsense-camera-in-5-minutes-jetson-nano/)

To run realsense-viewer, type: 

```
$ realsense-viewer
```

To get the realsense camera up and running for python3 you need to build realsense from source.<br> 
Follow instruction on: [Install RealSense Camera in 5 minutes – Jetson Nano, Build from Source](https://jetsonhacks.com/2019/12/22/install-realsense-camera-in-5-minutes-jetson-nano/)

and add this to the end of your .bashrc file 
```
export PYTHONPATH=$PYTHONPATH:/usr/local/lib/python3.6/pyrealsense2
```

and 'source ~/.bashrc'


**Errors**

If you get following error: *Failed to load module "canberra-gtk-module"*, install gtk and gtk3 module:

```
sudo apt install libcanberra-gtk-module libcanberra-gtk3-module
```