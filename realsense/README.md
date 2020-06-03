# Realsense D435i

<hr/>

## Get started
(ref : https://dev.intelrealsense.com/docs/docs-get-started)

* Installation (linux) 



## 1. Installation

### 1.1 Most issues
* firewall
* timeout
* device is empty (my troubleshooting)
		
### 1.2 Prerequisites
* verify supported kernel version 

 	uname -a

* Prepare linux backend and the Dev. Environment

	sudo apt-get install git libssl-dev libusb-1.0-0-dev pkg-config libgtk-3-dev
	sudo apt-get install libglfw3-dev

 	(Cmake: librealsense requires version 3.8+ 
	 which is currently not made available via apt manager for Ubuntu LTS.)

## a. Troubleshooting

