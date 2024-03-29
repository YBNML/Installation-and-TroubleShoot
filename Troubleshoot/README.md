#Navigation system using Monodepth and PCL

<hr/>

## 1. Index

### 1.1 Install & Config 
	- [x] Ubuntu Gnone - terminator config 
	- [x] nvidia-driver installation
	- [x] cuda installation
	- [x] CUDNN installation
	- [x] Python & venv installation
	- [x] Anaconda installation
	- [x] OpenCV version 4.1.0.25 
	- [x] librealsense 2.35.0 (relasnse-viewer) installation

### 1.2 TroubleShoot
	- [x] Install Nvidia Driver
	- [x] 'connection reset by peer' during tensorflow-gpu installation
	- [x] ReadTimeoutError: 'HTTPSConnectionPool(---): Read timed out.'
	- [x] 'UnknownError: Failed to get convolution algorithm. <br/> This is probably because cuDNN failed to initialize, so try looking to see if a warning log message was printed above.'
	- [x] ImportError: libcublas.so.10.0: cannot open shared object file: No such file or directory
	- [x] Could not load the Qt platform plugin "xcb" in "" even though it was found. (error about pyside2)
	- [x] 'ResourceExhaustedError: OOM when allocating tensor with shape[4,1280,15,20] and type float on ...' <br/> Hint: If you want to see a list of allocated tensors when OOM happens, add report_tensor_allocations_upon_oom to RunOptions for current allocation info.
	- [x] raise TypeError('Not JSON Serializable: %s' % (obj,)) <br/> TypeError: Not JSON Serializable: ?

<hr/>

## 2. Install & Config

### 2.1. Ubuntu Gnone - terminator config 
	[global_config]
	  focus = system
	  handle_size = 0
	  suppress_multiple_term_dialog = True
	  tab_position = bottom
	[keybindings]
	[layouts]
	  [[default]]
	    [[[child1]]]
	      parent = window0
	      type = Terminal
	    [[[window0]]]
	      parent = ""
	      size = 1000, 600
	      type = Window
	[plugins]
	[profiles]
	  [[default]]
	    background_darkness = 0.8
	    background_type = transparent
	    font = Bold 12
	    scrollbar_position = hidden
	    show_titlebar = False
	    use_system_font = False
                    
### 2.2. nvidia-driver installation
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

### 2.3 cuda installation
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

### 2.4 CUDNN installation
	(Reference - https://docs.nvidia.com/deeplearning/sdk/cudnn-install/index.html)
	(CUDNN 설치파일을 다운)
	sudo tar -xzvf cudnn-10.0-linux-x64-v7.6.1.34.tgz
	sudo cp include/cudnn*.h /usr/local/cuda/include
	sudo cp lib64/libcudnn* /usr/local/cuda/lib64
	sudo chmod a+r /usr/local/cuda/include/cudnn*.h /usr/local/cuda/lib64/libcudnn*

	(version check)
	cat /usr/local/cuda/include/cudnn.h | grep CUDNN_MAJOR -A 2

### 2.5 Python & venv installation
	(in Ubuntu16.04, default version is 3.5)
	sudo apt update 
	sudo apt install software-properties-common
	sudo add-apt-repository ppa:deadsnakes/ppa
	sudo apt update
	sudo apt install python3.7

	(venv)
	sudo apt-get install python3.7-venv
	python3.7 -m venv my-common-env

### 2.6 Anaconda installation
	(Install 'Anaconda Installer')
	bash Anaconda3-2019.03-Linux-x86_64.sh
	conda create -n monodepth2 python=3.6.6

### 2.7 OpenCV version 4.1.0.25
	conda install opencv-python==4.1.0.25 

<hr/>

### 2.8 librealsense 2.35.0 (relasnse-viewer) installation
	sudo apt-key adv --keyserver keys.gnupg.net --recv-key F6E65AC044F831AC80A06380C8B3A55A6F3EFCDE || sudo apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv-key F6E65AC044F831AC80A06380C8B3A55A6F3EFCDE
	sudo add-apt-repository "deb http://realsense-hw-public.s3.amazonaws.com/Debian/apt-repo xenial main" -u
	sudo apt-get install librealsense2-dkms
	sudo apt-get install librealsense2-utils

<hr/>


## 3.TroubleShoot

### 3.1 Install Nvidia Driver (Reason is Language setting)
	(Reference - https://hiseon.me/linux/ubuntu/install_nvidia_driver/)

### 3.2 'connection reset by peer' during tensorflow-gpu installation 
	(try many times)

### 3.3 ReadTimeoutError: 'HTTPSConnectionPool(---): Read timed out.'
	pip --default-timeout=100 install (package name)

### 3.4  'UnknownError: Failed to get convolution algorithm. <br/> This is probably because cuDNN failed to initialize, so try looking to see if a warning log message was printed above.' 
	<sol 1>
	(Reference - https://docs.nvidia.com/cuda/cuda-installation-guide-linux/index.html#package-manager-metas)
	(incorrected) 	sudo apt-get install cuda			<< Handles upgrading to the next version of the cuda package when it's released. 
	(corrected) 	sudo apt-get install cuda-10-0

	<sol 2> // issue = "GPU: "CUDNN_STATUS_INTERNAL_ERROR"."
	(Reference - https://github.com/tensorflow/tensorflow/issues/24496)
	(Reference - https://eehoeskrap.tistory.com/290)
	config = tf.ConfigProto()
	config.gpu_options.allow_growth = True
	sess = tf.Session(config=config)

### 3.5 ImportError: libcublas.so.10.0: cannot open shared object file: No such file or directory
	(PATH setting) (~/.bashrc)
	export PATH=$PATH:/usr/local/cuda-10.0/bin
	export CUDADIR=/usr/local/cuda-10.0
	export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/usr/local/cuda-10.0/lib64

### 3.6 Could not load the Qt platform plugin "xcb" in "" even though it was found. (error about pyside2)
	export QT_DEBUG_PLUGINS=1
	(Read the actual error message caused by QT)
	(libxcb-xinerama.so.0. libxcb-xinerama0 작동 하도록 다시 설치)
	export QT_DEBUG_PLUGINS=0
	sudo apt-get install --reinstall libxcb-xinerama0

### 3.7 'ResourceExhaustedError: OOM when allocating tensor with shape[4,1280,15,20] and type float on ...' <br/> Hint: If you want to see a list of allocated tensors when OOM happens, add report_tensor_allocations_upon_oom to RunOptions for current allocation info.
	<sol 1>
	(Reference - https://stackoverflow.com/questions/49665757/how-to-add-report-tensor-allocations-upon-oom-to-runoptions-in-keras)
	import tensorflow as tf
	run_opts = tf.RunOptions(report_tensor_allocations_upon_oom = True)
	model.compile(loss = "...", optimizer = "...", metrics = "..", options = run_opts)

	<sol 2>
	batch size issue!

### 3.8 raise TypeError('Not JSON Serializable: %s' % (obj,)) <br/> TypeError: Not JSON Serializable: ?
	(Reference - https://github.com/keras-team/keras/issues/9342#issuecomment-396056333)
	(in /home/iasl/my-common-env/lib/python3.7/site-packages/keras/engine)
	from tensorflow.python.framework.tensor_shape import Dimension
	if type(obj) == Dimension:
	return int(obj.value or 0)