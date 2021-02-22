from pygame import time
import launchpad_py as launchpad 
import threading
import json
from playsound import playsound

def checkLunchpad():
	if launchpad.LaunchpadPro().Check(0):
		lp = launchpad.LaunchpadPro()
	elif launchpad.LaunchpadMk2().Check(0):
		lp = launchpad.LaunchpadMk2()
	elif launchpad.LaunchpadMiniMk3().Check(1):
		lp = launchpad.LaunchpadMiniMk3()
	elif launchpad.LaunchpadProMk3().Check(1):
		lp = launchpad.LaunchpadProMk3()	
	elif launchpad.Launchpad().Check(0):
		lp = launchpad.Launchpad()
	else:
		print("Lanchpad not connected")
		input()
		exit(0)

	lp.Open(0)
	return lp

def setUp():
	try:
		DetectMidi = True
		GetFile = None
		PathProj = None
		mode = None

		lp = checkLunchpad()

		LedValue = [5,9,13,21,37,45,49,0]
		sleep = 20
		sleep2 = [30, 50, 30, 30, 30, 30, 30, 30]

		Page = 0

		ButtonClick = {}
		ButtonSound = {}

		for i in range(8):
			ButtonClick[i] = [
				1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,
				1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,
				1,1,1,1,1,1,1,1,1,1,1,1,1,1
			]

		for i in range(8):
			ButtonSound[i] = [
				1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,
				1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,
				1,1,1,1,1,1,1,1,1,1,1,1,1,1
			]
		
		return DetectMidi, GetFile, PathProj, mode, lp, LedValue, sleep, sleep2, Page, ButtonClick, ButtonSound	
	except:
		print("Error - setup")
		return 0