# UltimateSecurityCam
---

#### An easy-to-build , un-hack-able security camera which is impossible to fool . "Beginner Friendly"

[![forthebadge](https://forthebadge.com/images/badges/built-with-love.svg)](https://forthebadge.com)
[![forthebadge](https://forthebadge.com/images/badges/made-with-python.svg)](https://forthebadge.com)

##### Working demo video  [here](SampleVid/SecurityCam.mp4)
##### To ask doubts and staying in touch , join our [gitter channel](https://gitter.im/UltimateSecurityCam/Lobby)

[![Chat at gitter](https://img.shields.io/badge/Chat%20on%20-Gitter-brightgreen.svg)](https://gitter.im/UltimateSecurityCam/Lobby)


---
## Table of content

- [Introduction](#introduction)
  - [Technologies](#technologies)
  - [Working](#how-it-works)
- [Step by step guide](#step-by-step-guide)
- [Setup](#setup-instructions)
- [Running](#running)
  - [Linux support](#ultimatesecuritycam-running-on-linux)
  - [Running instructions](#running-instructions)
- [Get in touch](#get-in-touch)



---
## Introduction
[(Back to top👆🏻)](#table-of-content)
- This is a security camera software which detects any intruder and alerts the owner .
- This is the basic prototype , we'll make it un-hack-able by using microphone and eliminating every possible hack to fool our software.
- Many issues are up-for-grabs. Check them out from issues tab.


### Technologies:
- `Python 3.6`
- `Opencv (cv2)` [tutorial](https://pythonprogramming.net/loading-images-python-opencv-tutorial/)

### How it works?
We take a snapshot of the room , lets call this `base.jpg`. Now , the code continuously scan the current frame and subtract it from `base.jpg`.
If the difference is more than a threshold , we'll consider a breach happening.

### Features
- Detects any kind of unwanted movements or disturbances in the surroundings.
- Capable of differentiaing day and night or darkness in the surroundings.
- The program is integrated with automatic recording feature whenever it detects darkness or lights being off. So that when the camera can not 
  identify intruders in dark the sound can be recorded, making the camera foolproof.
- The program automatically clicks snapshot and saves the image as 'image.jpg' which show maximum movement in it's complete cycle.

---
## Step by step guide
[(Back to top👆🏻)](#table-of-content)

- Installation of all the required depedencies is completed first. [Setup](#setup-instructions)
- The code is made to run via terminal/IDE. [Running](#running)
- Sequence of code:
	- The Graphical user interfaces initializes. When user presses `Run` button the main program executes in a new window. 
	- The code first initializes a three seconds waiting camera window.
	- The main code runs to detect movements and record the complete video footage.
	- The code is also capable of detecting darkness in the surroundings, by calculating the average brightness by overall pixels of a frame.
	  It indicates the user whenever it finds surroundings getting dark.
	- Whenever the program detects darkness it initializes the microphone to record the audio in the region.
	- The code takes snapshot of the frame with maximum movement count as`image.jpg` during it's complete execution cycle.
	- All the configurations of the video clip are recorded (like Date and Time, camera fps, maximum object movement recorded at a time, duration, etc.)
	- The video clip saved as `basic_motion_detection.avi` and the audio as `audio.wav`.
	- The GUI makes confirmation for saving the config file.
	- The configuration data like camera fps, duration of running, maximum object recorded, video file location is saved in `config.txt` for future reference.
	- Finally the code terminates with the termination of the main GUI window.
	

---
## Setup instructions
[(Back to top👆🏻)](#table-of-content)

## Initialisation :
To install the required packages use the following command in command prompt[windows] OR terminal[Unix]
````sh
 sudo python3 setup.py install
````
Packages can also be installed using pip-install [Tutorial](https://www.youtube.com/watch?v=237dNNQhD3Q).

---
## Running instructions :

## Working on the code:
- Windows: Open up `gui.py` in your preferred python IDE 
- Linux: Open the terminal in the `PythonCode` directory, copy the code `python3 gui.py` and run it.
- More formally , fork the code , and clone it your machine . I recommend that you use the GitHub desktop app.
  - If you need a python IDE , I recommend using pycharm. [Tutorial to install !](https://www.youtube.com/watch?v=QzcaEELafkE).
  - If you get an error , make sure all the **import statements are working** (required packages are [installed](#setup-instructions)) 
  

---
## Running 
[(Back to top👆🏻)](#table-of-content)

### UltimateSecurityCam running on Linux
Command (with `PythonCode` as the working directory):
`python3 gui.py`

![ultimatesecuritycam](https://user-images.githubusercontent.com/30645315/49302849-31d16380-f4ee-11e8-9bfa-4e99866fa3bc.gif)


### Running instructions:

- Open up `gui.py` in your preferred python IDE [UltimateSecurityCam.py](PythonCode/gui.py)
- Open up `gui.py` in your preferred python IDE [UltimateSecurityCam.py](PythonCode/gui.py) or run on command prompt using the command (in `PythonCode` directory)
  run the command `python3 gui.py`.
- Run using python 3.6 (recommended).
- The program takes 3-second waiting time, after that it starts detecting motion , making an alert sound.

Many improvements and developments are in the pipeline!

---
## Get in touch
[(Back to top👆🏻)](#table-of-content)

Shikhar Johri
[<img src="https://image.flaticon.com/icons/svg/185/185964.svg" width="35" padding="10">](https://www.linkedin.com/in/shikhar-johri/)
[<img src="https://image.flaticon.com/icons/svg/185/185981.svg" width="35" padding="10">](https://www.facebook.com/shikhar.johri.3)
[<img src="https://upload.wikimedia.org/wikipedia/commons/9/91/Octicons-mark-github.svg" width="35" padding="10">](https://github.com/johri002)

Nitesh Chaudhary
[<img src="https://image.flaticon.com/icons/svg/185/185964.svg" width="35" padding="10">](https://www.linkedin.com/in/niteshx2/)
[<img src="https://image.flaticon.com/icons/svg/185/185985.svg" width="35" padding="10">](https://www.instagram.com/nitz_chaudhry/)
[<img src="https://image.flaticon.com/icons/svg/185/185981.svg" width="35" padding="10">](https://www.facebook.com/niteshx2)
[<img src="https://upload.wikimedia.org/wikipedia/commons/9/91/Octicons-mark-github.svg" width="35" padding="10">](https://github.com/NIteshx2)

## Contribute
Found a bug, please [create an issue](https://github.com/njackwinterofcode/UltimateSecurityCam/issues)

<p align="center"> Made with ❤ by <a href="https://github.com/johri-lab">Shikhar Johri</a>a and <a href="https://github.com/NIteshx2">Nitesh Chaudhry</a></p>
