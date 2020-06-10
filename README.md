#Navigation system using Monodepth and PCL

<hr/>

## 1. Requirements

 [Github]
* Ubuntu : 16.04.6 LTS
* nvidia-driver : nvidia-440.64 
* cuda : 10.0.130 
* CUDNN : 7.65
* Python : 3.7.7
* pip : 20.1.1
* tensorflow-gpu : 1.13.2
* keras : 2.2.4
* (other package) : keras pillow matplotlib scikit-learn scikit-image opencv-python pydot GraphViz PyGLM PySide2 pyopengl 

 [Realsense D435]
* RealSense SDK 2.0 (librealsense version 2.35.0)

 [PCL & ROS]

<hr/>

## 2. Setting_[Github]

### 2.1. nvidia-driver : nvidia-440.64
	(Reference - https://hiseon.me/linux/ubuntu/install_nvidia_driver/)

### 2.2 cuda 10.0 & CUDNN 7.65
	(Reference - https://blog.nerdfactory.ai/2019/07/25/how-to-install-tensorflow-gpu-in-ubuntu16.04-copy.html)

	(Package List add)
	release="ubuntu"$(lsb_release -sr | sed -e "s/\.//g")
	echo $release				
	sudo apt install sudo gnupg
	sudo apt-key adv --fetch-keys "http://developer.download.nvidia.com/compute/cuda/repos/"$release"/x86_64/7fa2af80.pub"
	sudo sh -c 'echo "deb http://developer.download.nvidia.com/compute/cuda/repos/'$release'/x86_64 /" > /etc/apt/sources.list.d/nvidia-cuda.list'
	sudo sh -c 'echo "deb http://developer.download.nvidia.com/compute/machine-learning/repos/'$release'/x86_64 /" > /etc/apt/sources.list.d/nvidia-machine-learning.list'
	sudo apt update
	sudo apt-get install cuda-10-0
	sudo apt-get install libcudnn7-dev
	
	(version check)
	cat /usr/local/cuda/version.txt
	cat /usr/include/cudnn.h | grep -E "CUDNN_MAJOR|CUDNN_MINOR|CUDNN_PATCHLEVEL"
	sudo find / -name libcudnn*.*

### 2.3 Python3.7
	(in Ubuntu16.04, default version is 3.5)
	sudo apt update 
	sudo apt install software-properties-common
	sudo add-apt-repository ppa:deadsnakes/ppa
	sudo apt update
	sudo apt install python3.7

	(venv)
	sudo apt-get install python3.7-venv
	python3.7 -m venv my-common-env

### 2.4 tensorflow-gpu 1.13.2
	pip install tensorflow-gpu==1.13.2

### 2.5 keras 2.2.4
	pip install keras==2.2.4


<hr/>

## 3. Setting_[Realsense D435]

### 3.1 librealsense 2.35.0
	sudo apt-key adv --keyserver keys.gnupg.net --recv-key F6E65AC044F831AC80A06380C8B3A55A6F3EFCDE || sudo apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv-key F6E65AC044F831AC80A06380C8B3A55A6F3EFCDE
	sudo add-apt-repository "deb http://realsense-hw-public.s3.amazonaws.com/Debian/apt-repo xenial main" -u
	sudo apt-get install librealsense2-dkms
	sudo apt-get install librealsense2-utils

<hr/>

## 4. Setting_[PCL & ROS]

### 4.1 PCL-C++
	(Package install)
	sudo apt-get update && sudo apt-get install -y software-properties-common git
	sudo add-apt-repository ppa:v-launchpad-jochen-sprickerhof-de/pcl -y && sudo apt-get update
	sudo apt-get install -y libpcl-dev #ubuntu 16
	
	(Source install)
	git clone https://github.com/PointCloudLibrary/pcl.git
	cd pcl && mkdir release && cd release
	cmake -DCMAKE_BUILD_TYPE=None -DCMAKE_INSTALL_PREFIX=/usr -DBUILD_GPU=ON -DBUILD_apps=ON -DBUILD_examples=ON -DCMAKE_INSTALL_PREFIX=/usr ..
	make -j8
	sudo make install

### 4.2 ROS-kinetic
	wget https://raw.githubusercontent.com/ROBOTIS-GIT/robotis_tools/master/install_ros_kinetic.sh
	chmod +x install_ros_kinetic.sh
	./install_ros_kinetic.sh 
	
	(Execution)
	roscore

### 4.3 ROS & PCL


<hr/>

## a.TroubleShoot

### a.1 Nvidia Driver (Reason is Language setting)
	(Reference - https://hiseon.me/linux/ubuntu/install_nvidia_driver/)

### a.2 'connection reset by peer' during tensorflow-gpu installation 
	pip install tensorflow-gpu==1.13.1
	(instead)
	pip install tensorflow-gpu==1.13.2

### a.3 'HTTPSConnectionPool(---): Read timed out.'
	pip --default-timeout=100 install (package name)

### a.4  'UnknownError: Failed to get convolution algorithm. <br/> This is probably because cuDNN failed to initialize, so try looking to see if a warning log message was printed above.'

	