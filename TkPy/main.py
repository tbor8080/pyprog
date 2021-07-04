# -*- encoding: utf-8 -*-
from time import sleep
import datetime
import tkinter
import tkinter as tk
from tkinter import ttk
import threading
from test import GUITEST
from module import *

####################################################################
# Tkinter sample ***************************************************
# 2021.07.04
####################################################################

# Global Variable Start
# Global Variable End

# Main Loop Start
root=tkinter.Tk()
root.geometry("800x400")

# Text
textWidget=tk.Text(root)
textWidget.grid(column=0,row=1,sticky=(tk.N,tk.S,tk.E,tk.W))
textWidget.pack()
textWidget.bind('<Key>', OnKeyPress)
root.mainloop()

"""
===================================================================
"""
# Main Loop End