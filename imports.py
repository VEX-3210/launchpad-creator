from pygame import time
import launchpad_py as launchpad 
import threading
import json
from playsound import playsound

DetectMidi = True
GetFile = None
PathProj = None
mode = None
lp = None	

if launchpad.LaunchpadPro().Check(0):
	lp = launchpad.LaunchpadPro()
	lp.Open(0)
elif launchpad.LaunchpadMk2().Check(0):
	lp = launchpad.LaunchpadMk2()
	lp.Open(0)
else:
	print("Lanchpad not connected")
	input()
	exit(0)

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