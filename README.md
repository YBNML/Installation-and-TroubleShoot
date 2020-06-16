#Navigation system using Monodepth and PCL

<hr/>

## 1. Requirements

 [Github]
* Ubuntu : 18.04.6 LTS
* nvidia-driver : nvidia-450.36.06 (automatically fetched, when I install 'cuda')
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
	release="ubuntu"$(lsb_release -sr | sed -e "s/\.//g")
	echo $release

	sudo apt install sudo gnupg
	sudo apt-key adv --fetch-keys "http://developer.download.nvidia.com/compute/cuda/repos/"$release"/x86_64/7fa2af80.pub"
	sudo sh -c 'echo "deb http://developer.download.nvidia.com/compute/cuda/repos/'$release'/x86_64 /" > /etc/apt/sources.list.d/nvidia-cuda.list'
	sudo sh -c 'echo "deb http://developer.download.nvidia.com/compute/machine-learning/repos/'$release'/x86_64 /" > /etc/apt/sources.list.d/	idia-machine-learning.list'
	sudo apt update
	
	apt-cache search nvidia

	sudo apt-get install nvidia-driver-440
	sudo apt-get install dkms nvidia-modprobe

	(reboot)

	nvidia-smi

### 2.2 cuda 10.0.130
	(Reference - https://www.pugetsystems.com/labs/hpc/How-To-Install-CUDA-10-together-with-9-2-on-Ubuntu-18-04-with-support-for-NVIDIA-20XX-Turing-GPUs-1236/#do-i-need-to-install-cuda-10)
	(Reference - https://jangjy.tistory.com/195)
	(Reference - https://eungbean.github.io/2018/08/08/Ubuntu-Installation2-1/)
	
	(Install CUDA "dependencies")
	sudo apt-get install build-essential dkms
	sudo apt-get install freeglut3 freeglut3-dev libxi-dev libxmu-dev

	(Get the CUDA 10 "deb" file to set up the package repository && Do the install!) 
	sudo dpkg -i cuda-repo-ubuntu1804-10-0-local-10.0.130-410.48_1.0-1_amd64.deb
	sudo apt-key add /var/cuda-repo-<version>/7fa2af80.pub
	sudo apt-get update
	sudo apt-get install cuda-10-0

	(reboot)
	vim ~/.bashrc

	export PATH=$PATH:/usr/local/cuda-10.0/bin
	export CUDADIR=/usr/local/cuda-10.0
	export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/usr/local/cuda-10.0/lib64

	source .bashrc

	(version check)
	nvcc -V
	cat /usr/local/cuda/version.txt
	cat /usr/local/cuda-10.0/version.txt

	(Test CUDA by building the "samples")
	mkdir cuda-testing
	cd cuda-testing/
	cp -a /usr/local/cuda-10.0/samples samples-10.0
	cd samples-10.0/
	make -j 4
	cd bin/x86_64/linux/release/
	./nbody

### 2.3 CUDNN 7.6.1
	(Reference - https://docs.nvidia.com/deeplearning/sdk/cudnn-install/index.html)
	(CUDNN 설치파일을 다운)
	sudo tar -xzvf cudnn-10.0-linux-x64-v7.6.1.34.tgz
	sudo cp include/cudnn*.h /usr/local/cuda/include
	sudo cp lib64/libcudnn* /usr/local/cuda/lib64
	sudo chmod a+r /usr/local/cuda/include/cudnn*.h /usr/local/cuda/lib64/libcudnn*

	(version check)
	cat /usr/local/cuda/include/cudnn.h | grep CUDNN_MAJOR -A 2

### 2.4 Python3.7
	(in Ubuntu16.04, default version is 3.5)
	sudo apt update 
	sudo apt install software-properties-common
	sudo add-apt-repository ppa:deadsnakes/ppa
	sudo apt update
	sudo apt install python3.7

	(venv)
	sudo apt-get install python3.7-venv
	python3.7 -m venv my-common-env

### 2.5 tensorflow-gpu 1.13.2
	pip install tensorflow-gpu==1.13.1

### 2.6 keras 2.2.4
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

### a.1 Install Nvidia Driver (Reason is Language setting)
	(Reference - https://hiseon.me/linux/ubuntu/install_nvidia_driver/)

### a.2 'connection reset by peer' during tensorflow-gpu installation 
	(try many times)

### a.3 ReadTimeoutError: 'HTTPSConnectionPool(---): Read timed out.'
	pip --default-timeout=100 install (package name)

### a.4  'UnknownError: Failed to get convolution algorithm. <br/> This is probably because cuDNN failed to initialize, so try looking to see if a warning log message was printed above.' 
	<sol 1>
	(Reference - https://docs.nvidia.com/cuda/cuda-installation-guide-linux/index.html#package-manager-metas)
	(incorrected) 	sudo apt-get install cuda			<< Handles upgrading to the next version of the cuda package when it's released. 
	(corrected) 	sudo apt-get install cuda-10-0

	<sol 2>
	(Reference - https://github.com/tensorflow/tensorflow/issues/24496)
	(Reference - https://eehoeskrap.tistory.com/290)
	config = tf.ConfigProto()
	config.gpu_options.allow_growth = True
	sess = tf.Session(config=config)

### a.5 ImportError: libcublas.so.10.0: cannot open shared object file: No such file or directory
	(PATH setting) (~/.bashrc)
	export PATH=$PATH:/usr/local/cuda-10.0/bin
	export CUDADIR=/usr/local/cuda-10.0
	export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/usr/local/cuda-10.0/lib64

### a.6 Could not load the Qt platform plugin "xcb" in "" even though it was found. (error about pyside2)
	export QT_DEBUG_PLUGINS=1
	(Read the actual error message caused by QT)
	(libxcb-xinerama.so.0. libxcb-xinerama0 작동 하도록 다시 설치)
	export QT_DEBUG_PLUGINS=0
	sudo apt-get install --reinstall libxcb-xinerama0