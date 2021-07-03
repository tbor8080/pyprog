from time import sleep
import threading
import tkinter
from tkinter import ttk
import random


time_v=0

def main():
    tkinter._test()

def testWindow():
    pass

def StringVar():
    pass

root = tkinter.Tk()
root.title("Sample Window")
root.geometry("800x600")
t = StringVar()
Frame1 = ttk.Frame(root, padding=16)
Button=ttk.Button(Frame1, text=u'ボタン')
Entry1 = ttk.Entry(Frame1, textvariable=t)


Frame1.pack()
Entry1.pack()
Button.pack()

root.mainloop()
