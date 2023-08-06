import pyautogui
import os
from time import sleep

def find():
	while True:
		cwd = os.getcwd()
		for root, dirs, files in os.walk(cwd):
			for file in files:
				if file.endswith(".PNG" or ".png"):
					image = file
		if pyautogui.locateOnScreen(image) != None:
			found = True
			print ("True")
			sleep(0.5)
		else:
			found = False
			print ("False")
			sleep(0.5)
find()