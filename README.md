# Navigation system using Monodepth and PCL

<hr/>

## 1. Requirements

* Ubuntu : 16.04.6 LTS
* Python : 3.7.7 (But Default version is 3.5.2) 
* pip3 : 8.1.1 (python3.5)
* nvidia-driver : nvidia-384 
	sudo apt-get install nvidia-418
* cuda : 10.0
	(Download Installer)
	sudo dpkg -i cuda-repo-ubuntu1604-10-0-local-10.0.130-410.48_1.0-1_amd64.deb
	sudo apt-key add /var/cuda-repo-10-0-local-10.0.130-410.48/7fa2af80.pub
	sudo apt-get update
	sudo apt-get install cuda
* tensorflow 1.13

 
## 2. Setting

### 2.1. PCL-Python install
	sudo add-apt-repository ppa:sweptlaser/python3-pcl #Python3 Only??
	sudo apt update
	sudo apt install python3-pcl

