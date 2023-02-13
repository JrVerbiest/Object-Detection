# Object detection 

Development tools
- Linux computer.
- [Edge Impulse Studio](https://www.edgeimpulse.com/)

Hardware
- NVIDIA® Jetson Nano™ Developer Kit (4GB)
- Intel® RealSense™ Depth Camera D435i

---

## ° Conda environment

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

# Single Board Computer - NVIDIA Jetson Nano

## ° NVIDIA® Jetson Nano™ Developer Kit 

[NVIDIA JetPack 4.6.1.](https://developer.nvidia.com/embedded/jetpack-sdk-461)<br>
see also [Getting Started with Jetson Nano Developer Kit](https://developer.nvidia.com/embedded/learn/get-started-jetson-nano-devkit)

## ° Realsense on Jetson Nano

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

---
## Optional
### ° Nomachine

Install [NoMachine](https://www.nomachine.com/) for remote destop. 

### ° Visual Code

Install [Visual Code](https://code.visualstudio.com/). To install Visual Code on Jetson Nano follow the instruction on: [JetsonHacks - Visual Studio Code](https://jetsonhacks.com/2020/11/28/visual-studio-code/)

<br>
# References

- [Edge Impulse - Build an Object Detection Model Using Transfer Learning [Part 1]](https://www.youtube.com/watch?v=Vwv0PJPeC4s&list=PL7VEa1KauMQqAbcN_RxSON4P7fPpNTJxl&index=4)
- [Edge - Impulse - Running Object Detection with Linux Python SDK [Part 2]](https://www.youtube.com/watch?v=rUzXcICfDR0&list=PL7VEa1KauMQqAbcN_RxSON4P7fPpNTJxl&index=3)
- [Beginners guide to Object Detection with Edge Impulse](https://peter-ing.medium.com/beginners-guide-to-object-detection-with-edge-impulse-c8ea95f844a0)