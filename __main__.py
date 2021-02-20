from imports import *
import Load
import MainLoop as ml
import TkinterFunctions as tf

Load.LoadPro()

root = Tk.Tk()
root.geometry('500x500+200+100')
root.overrideredirect(0)

bt = Tk.Button(root, command=ButtonClick)
bt.pack()


ml.MainLoop(root)