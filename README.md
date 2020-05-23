# Navigation system using Monodepth and PCL

<hr/>

## 1. Requirements

 [Github]
* Ubuntu : 16.04.6 LTS
* Python : 3.7.7 (But Default version is 3.5.2) 
* pip : 20.1.1
* nvidia-driver : nvidia-384 
* cuda : 10.0.130 
* CUDNN : 7.65
* tensorflow-gpu : 1.13.2

 [Realsense D435]
* RealSense SDK 2.0 (librealsense version 2.34.0)
* Ubuntu : 16.04.6 LTS
* ROS kinetic
 
## 2. Setting_[Github]

### 2.1. nvidia-driver : nvidia-384
	sudo apt-get install nvidia-384

### 2.2 cuda 10.0 & CUDNN 7.65
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
	pip install tensorflow-gpu==1.13.1


### PCL-Python install
	sudo add-apt-repository ppa:sweptlaser/python3-pcl #Python3 Only??
	sudo apt update
	sudo apt install python3-pcl
## 3. Setting_[Realsense D435]

### 3.1 librealsense 2.34.0
	sudo apt-key adv --keyserver keys.gnupg.net --recv-key F6E65AC044F831AC80A06380C8B3A55A6F3EFCDE || sudo apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv-key 
	sudo add-apt-repository "deb http://realsense-hw-public.s3.amazonaws.com/Debian/apt-repo xenial main" -u
	sudo apt-get install librealsense2-dkms
	sudo apt-get install librealsense2-utils

## a.TroubleShoot

### a.1 'connection reset by peer' during tensorflow-gpu install 


