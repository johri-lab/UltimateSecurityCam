import sys
import cv2
from tkinter import filedialog
from tkinter import *
import tkinter.messagebox
from UltimateSecurityCam import UltimateSecurityCam


class Window:

	def __init__(self, master):
	
		master.title("Ultimate Security Camera")
		#master.configure(background='black')
		master.geometry("300x110")
		
		#Menu bar
		menu = Menu(master)
		master.config(menu=menu)
		
		fileTab = Menu(menu)
		fileTab.add_command(label = "Exit", command = self.client_exit)
		menu.add_cascade(label = "File", menu = fileTab)

		help = Menu(menu)
		help.add_command(label = "How it works?")
		help.add_command(label = "About us")#, command = )
		menu.add_cascade(label = "Help", menu = help)


		#Run button
		self.runButton = Button(master, text="Run", command=self.usc, activebackground="black", activeforeground ="red", 
								 padx=36, bg="orange", relief=GROOVE)
		self.runButton.focus_set()
		self.runButton.pack()

		#Object Detection
		self.detectionButton = Button(master, text="Object Detection", command=self.detection, activebackground="black", 
									  activeforeground="red", padx=34, bg="orange", relief=GROOVE) 
		self.detectionButton.pack()
		
		#Exit Button
		self.exitButton = Button(master, text="Quit", command=self.client_exit, activebackground="black", 
								 activeforeground ="red", padx=35, bg="orange", relief=GROOVE)
		self.exitButton.pack()

	def usc(self):
		global root
		#root.destroy()
		#self.runButton.flash()
		
		start = UltimateSecurityCam()
		start.initial_window()
		data = start.usc()
		#self.master.focus_set()
		saveconfig = tkinter.messagebox.askyesno("save configuration", "Do you wish to save the current configs?", icon = tkinter.messagebox.QUESTION)
		if saveconfig:
			start.config(data)
		self.exitButton.focus_set()
	
	def detection(self):
		#global root
		detectstart = UltimateSecurityCam()
		detectstart.ObjectDetection()
	
	def client_exit(self):
		answeryes = tkinter.messagebox.askyesno("Exit", "Do you really wish to exit?", icon = tkinter.messagebox.WARNING)
		if answeryes: 
			print("Program succesfully terminated!")
			exit()

	'''
	def refresh(self):
		#refreshes the complete window		
		global root
		answeryes = tkinter.messagebox.askyesno("Question", "All unsaved progress will be lost by reloading. Do you still want to continue?")
		if answeryes:
			root.destroy()
			exec(open("./UltimateSecurityCam.py").read())
	'''
	
# initialize the app window
global root
root = Tk()

b = Window(root)
root.mainloop()
