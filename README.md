#Navigation system using Monodepth and PCL

<hr/>

## 1. Requirements

 [Github]
* Ubuntu : 16.04.6 LTS
* nvidia-driver : nvidia-440.64 
* cuda : 10.0.130 
* CUDNN : 7.6.1
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

### 2.2 cuda 10.0 & CUDNN 7.6.1
	(Reference - https://blog.nerdfactory.ai/2019/07/25/how-to-install-tensorflow-gpu-in-ubuntu16.04-copy.html)
	(Reference - https://goodtogreate.tistory.com/entry/TensorFlow-GPU-%EB%B2%84%EC%A0%84-%EC%9A%B0%EB%B6%84%ED%88%AC-1604%EC%97%90-%EC%84%A4%EC%B9%98-%ED%95%98%EA%B8%B0)

	(먼저 nvidia 홈페이지에서 ubuntu16.04, cuda10.0에 맞는 설치파일을 다운로드, 설치한 경로에서 아래의 커맨트를 입력)
	sudo dpkg -i cuda-repo-ubuntu1604-10-0-local-10.0.130-410.48_1.0-1_amd64.deb
	sudo apt-key add /var/cuda-repo-10-0-local-10.0.130-410.48/7fa2af80.pub
	sudo apt-get update
	sudo apt-get install cuda

	(version check)
	nvcc --version

	(CUDNN 설치파일을 다운)
	sudo tar -xzvf cudnn-9.0-linux-x64-v7.0.tgz
	sudo cp include/cudnn.h /usr/local/cuda/include
	sudo cp lib64/libcudnn* /usr/local/cuda/lib64
	sudo chmod a+r /usr/local/cuda/lib64/libcudnn*

	(version check)
	cat /usr/local/cuda/include/cudnn.h | grep CUDNN_MAJOR -A 2

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

### a.4  'UnknownError: Failed to get convolution algorithm. <br/>		This is probably because cuDNN failed to initialize, so try looking to see if a warning log message was printed above.'


### a.5