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
		master.geometry("300x90")
		
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
		self.runButton = Button(master, text="Run", command=self.usc, activebackground="black", activeforeground ="red", padx=30, bg="orange", relief=GROOVE)
		self.runButton.flash()
		self.runButton.pack()
		
		#Exit Button
		self.exitButton = Button(master, text="Quit", command=self.client_exit, activebackground="black", activeforeground ="red", padx=29, bg="orange", relief=GROOVE)
		self.exitButton.pack()

	def usc(self):
		global root
		root.destroy()
		start = UltimateSecurityCam()
		start.initial_window()
		data = start.usc()
		start.config(data)
		print("Program succesfully terminated!")
	
	def client_exit(self):
		answeryes = tkinter.messagebox.askyesno("Question", "Do you really wish to exit?")
		if answeryes: 
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
