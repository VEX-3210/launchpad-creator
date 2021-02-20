from imports import *


def LoadPro():
	lp.LedAllOn(0)
	for Value in range(8):
		for x in range(6):
			if x==1:
				lp.LedCtrlRawByCode(45,LedValue[Value])
				lp.LedCtrlRawByCode(44,LedValue[Value])

				lp.LedCtrlRawByCode(54,LedValue[Value])
				lp.LedCtrlRawByCode(55,LedValue[Value])
				
				time.wait(sleep)
			if x==2:
				lp.LedCtrlRawByCode( 33,LedValue[Value])
				lp.LedCtrlRawByCode( 36,LedValue[Value])

				lp.LedCtrlRawByCode( 63,LedValue[Value])
				lp.LedCtrlRawByCode( 66,LedValue[Value])
				time.wait(sleep)
			if x==3:
				lp.LedCtrlRawByCode( 23,LedValue[Value])
				lp.LedCtrlRawByCode( 24,LedValue[Value])
				lp.LedCtrlRawByCode( 25,LedValue[Value])
				lp.LedCtrlRawByCode( 26,LedValue[Value])

				lp.LedCtrlRawByCode( 73,LedValue[Value])
				lp.LedCtrlRawByCode( 74,LedValue[Value])
				lp.LedCtrlRawByCode( 75,LedValue[Value])
				lp.LedCtrlRawByCode( 76,LedValue[Value])

				lp.LedCtrlRawByCode( 32,LedValue[Value])
				lp.LedCtrlRawByCode( 33,LedValue[Value])
				lp.LedCtrlRawByCode( 36,LedValue[Value])
				lp.LedCtrlRawByCode( 37,LedValue[Value])

				lp.LedCtrlRawByCode( 62,LedValue[Value])
				lp.LedCtrlRawByCode( 63,LedValue[Value])
				lp.LedCtrlRawByCode( 66,LedValue[Value])
				lp.LedCtrlRawByCode( 67,LedValue[Value])

				lp.LedCtrlRawByCode( 41,LedValue[Value])
				lp.LedCtrlRawByCode( 48,LedValue[Value])

				lp.LedCtrlRawByCode( 51,LedValue[Value])
				lp.LedCtrlRawByCode( 58,LedValue[Value])

				time.wait(sleep)
			if x==4:	
				lp.LedCtrlRawByCode( 11,LedValue[Value])
				lp.LedCtrlRawByCode( 12,LedValue[Value])
				lp.LedCtrlRawByCode( 13,LedValue[Value])
				lp.LedCtrlRawByCode( 16,LedValue[Value])
				lp.LedCtrlRawByCode( 17,LedValue[Value])
				lp.LedCtrlRawByCode( 18,LedValue[Value])

				lp.LedCtrlRawByCode( 21,LedValue[Value])
				lp.LedCtrlRawByCode( 28,LedValue[Value])

				lp.LedCtrlRawByCode( 81,LedValue[Value])
				lp.LedCtrlRawByCode( 82,LedValue[Value])
				lp.LedCtrlRawByCode( 83,LedValue[Value])
				lp.LedCtrlRawByCode( 86,LedValue[Value])
				lp.LedCtrlRawByCode( 87,LedValue[Value])
				lp.LedCtrlRawByCode( 88,LedValue[Value])

				lp.LedCtrlRawByCode( 71,LedValue[Value])
				lp.LedCtrlRawByCode( 78,LedValue[Value])

				time.wait(sleep)
			if x==5:
				lp.LedCtrlRawByCode(1,LedValue[Value])
				lp.LedCtrlRawByCode(2,LedValue[Value])
				lp.LedCtrlRawByCode(3,LedValue[Value])
				lp.LedCtrlRawByCode(6,LedValue[Value])
				lp.LedCtrlRawByCode(7,LedValue[Value])
				lp.LedCtrlRawByCode(8,LedValue[Value])

				lp.LedCtrlRawByCode(10,LedValue[Value])
				lp.LedCtrlRawByCode(19,LedValue[Value])

				lp.LedCtrlRawByCode(20,LedValue[Value])
				lp.LedCtrlRawByCode(29,LedValue[Value])

				lp.LedCtrlRawByCode(40,LedValue[Value])
				lp.LedCtrlRawByCode(49,LedValue[Value])

				lp.LedCtrlRawByCode(50,LedValue[Value])
				lp.LedCtrlRawByCode(59,LedValue[Value])

				lp.LedCtrlRawByCode(70,LedValue[Value])
				lp.LedCtrlRawByCode(79,LedValue[Value])

				lp.LedCtrlRawByCode(80,LedValue[Value])
				lp.LedCtrlRawByCode(89,LedValue[Value])

				lp.LedCtrlRawByCode(91,LedValue[Value])
				lp.LedCtrlRawByCode(92,LedValue[Value])
				lp.LedCtrlRawByCode(93,LedValue[Value])
				lp.LedCtrlRawByCode(96,LedValue[Value])
				lp.LedCtrlRawByCode(97,LedValue[Value])
				lp.LedCtrlRawByCode(98,LedValue[Value])

				time.wait(sleep)