from imports import *

import Load
import MainLoop as ml


Load.LoadPro()

while True:
    try:
        ml.MainLoop()
    except:
        print('application closed')
        exit(0)
