import pyautogui
import os
from time import sleep

def found():
	pass

def notFound():
	pass

def find():
	while True:
		cwd = os.getcwd()
		for root, dirs, files in os.walk(cwd):
			for file in files:
				if file.endswith(".PNG" or ".png"):
					image = file
		if pyautogui.locateOnScreen(image) != None:
			found()
			print ("True")
			sleep(0.5)
		else:
			notFound()
			print ("False")
			sleep(0.5)