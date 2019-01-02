# coding=utf-8

import cv2
import numpy as np
import pygame
import json
import time, sys, os
import pyaudio
import wave
import threading

 
#if you get error while importing the google how to install <Package Name> in python 3.6

FORMAT = pyaudio.paInt16
CHANNELS = 2
RATE = 44100
CHUNK = 1024
#RECORD_SECONDS = 5
WAVE_OUTPUT_FILENAME = "file.wav"

audio = pyaudio.PyAudio()

camera = cv2.VideoCapture(0)

size = (int(camera.get(cv2.CAP_PROP_FRAME_WIDTH)),
				int(camera.get(cv2.CAP_PROP_FRAME_HEIGHT)))


# Write test video
fps = 2 #camera.get(cv2.CAP_PROP_FPS)
pygame.mixer.init()

dir_path = os.path.dirname(os.path.realpath(__file__))
#video file name
videofile = "basic_motion_detection.avi"

class UltimateSecurityCam:
	"""	UltimateSecurityCam class identifies object movements and 
		detection of any kind of undesirable movement in the 
		surroundings
	"""

	def __init__(self):

		self.stream = audio.open(format=FORMAT, channels=CHANNELS,
				rate=RATE, input=True,
				frames_per_buffer=CHUNK)
		self.frames = []


		#initial values set
		self.THRESHOLD = 40

		self.es = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (9,4))
		#self.kernel = np.ones((5,5), np.uint8)
		self.background = None

		self.cameraSound = pygame.mixer.Sound("snapshotsound.ogg")
		
		self.videoWriter = cv2.VideoWriter(os.path.join(str(dir_path),videofile),
						  cv2.VideoWriter_fourcc('D', 'I', 'V', 'X'),
						  fps, size)

		
	def initial_window(self):
		#initial window starts 
		initial = int(time.time())
		final = initial + 4
		while (final-initial):
			#start timer on the frames
			ret, frame = camera.read()
			initailiztion_text = ("Starting in " + str(final-initial) + "...")
			cv2.putText(frame,initailiztion_text,(60,30),
						cv2.FONT_HERSHEY_TRIPLEX,1,(0,100,255),2)
			cv2.imshow("Ultimate Security Camera",frame)

			if cv2.waitKey(int(45)) &0xff == ord('q'):
				break
				
			elif int(time.time()) == (initial + 1):
				initial = initial + 1
				#print(str(final-initial) + "...")

	def usc(self):
		#main window opens and opject movement detection starts
		maxcnts = 0		
		#global background
		start = time.time()	
		
		while (True):
			
			print ("recording...")
						
			ret, frame = camera.read()
			self.stream_audio(self.frames)

			# The first frame as the background
			if self.background is None:
				self.background = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
				self.background = cv2.GaussianBlur(self.background, (21,21), 0)
				continue
			
			gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
			gray_frame = cv2.GaussianBlur(gray_frame, (21,21), 0)

			self.stream_audio(self.frames)
							
			# Compare the difference between each frame of image and the background
			#print(background.shape, gray_frame.shape)
			diff = cv2.absdiff(self.background, gray_frame)
			diff = cv2.threshold(diff, self.THRESHOLD, 255, cv2.THRESH_BINARY)[1]
			diff = cv2.dilate(diff, self.es, iterations=2)
			
			# Calculate the outline of the target in the image
			image, cnts, hierarchy = cv2.findContours(diff.copy(),
								  cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
			detection_text = ("Detecting " + str(len(cnts)) + " Moving Objects")
			
			
			#identifying if lights are on or off
			#b,g,r = cv2.split(frame)
			#pixels = frame.shape[0]*frame.shape[1]
			#print(sum(sum(b+g+r))/(3*pixels))
			self.stream_audio(self.frames)
			
			#finds the level of darkness value ranging from 0 to 255
			darkness_level = np.mean(gray_frame)
			
			#Level of darkness selected
			if darkness_level < 50:
				detection_text = detection_text + str('(Dark)')
				
				
			detection_text_colour = (0,255,0) 	#set as green
			if len(cnts) > 0:
				#if breach detected
				detection_text_colour = (0,0,255)   #set to red
				self.cameraSound.play()

			self.stream_audio(self.frames)
			
			for c in cnts:
				if cv2.contourArea(c) < (self.background.shape[0]*self.background.shape[1])/204:
					#minimum area to be calculated based on image size and camera megapixels
					continue
				# Calculate the bounding box
				(x, y, w, h) = cv2.boundingRect(c)
				cv2.rectangle(frame, (x,y), (x+w, y+h), (0,255,0), 2)

			#maximum object detected
			if len(cnts)>maxcnts: maxcnts=len(cnts)

			#print(detection_text)
			cv2.putText(frame,detection_text,(60,30),cv2.FONT_HERSHEY_DUPLEX,1,detection_text_colour,2)

			diff = cv2.cvtColor(diff, cv2.COLOR_GRAY2BGR)			#3 channel gray scaled image

			horizontal_stack = np.hstack((frame, diff))				#proper way to stack 3D arrays
			merged_windows = np.concatenate((frame, diff), axis=1)

			cv2.imshow("Ultimate Security Camera", merged_windows)

			
			#cv2.imshow("contours", frame)
			self.videoWriter.write(frame)
			#cv2.imshow("dif", diff)
			#cv2.imwrite('didff.jpg', diff)

			self.stream_audio(self.frames)

			keypress = cv2.waitKey(25)
			if keypress:
				if keypress &0xff == ord('q'):
					self.save_audio(self.frames)
					break
				elif keypress &0xff == ord('r'):			
					#reset the camera
					self.background = None

		cv2.destroyAllWindows()
		camera.release()

		end = time.time() 
		duration = end-start

		data={"Date and Time":time.asctime(time.localtime(time.time())),
			 "Camera FPS":fps,
			 "Threshold":self.THRESHOLD,
			 "Max Objects recorded":maxcnts,
			 "Video File":videofile,
			 "Path":dir_path,
			 "Duration": '%0.2f' %(duration) + ' seconds'}
		return data

	def stream_audio(self,frames):
		data = self.stream.read(CHUNK)
		frames.append(data)

	def save_audio(self,frames):
		print ("finished recording") 
		# stop Recording
		self.stream.stop_stream()
		self.stream.close()
		audio.terminate()

		waveFile = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
		waveFile.setnchannels(CHANNELS)
		waveFile.setsampwidth(audio.get_sample_size(FORMAT))
		waveFile.setframerate(RATE)
		waveFile.writeframes(b''.join(frames))
		waveFile.close()
		
	def config(self,data):
		#saves all necessary configurations
		
		confirm = input("Do you wish to save the current configs? [Y/N]: ")
		#if run with python2 use raw_input

		configfile = "config.txt"

		if confirm.startswith('y' or 'Y'):
			print("\nUpdating config file...")
			with open(configfile,'w') as jfile:
				json.dump(data, jfile, indent = 4)
			print("Data updated to " + configfile + " successfully!")

		elif confirm.startswith('n' or 'N'):
			pass

		else:
			print("Invalid input!")


