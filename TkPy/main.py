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
#root=Interface()
#root.bind('<Key>', OnKeyPress)

# Text
#textWidget=tk.Text(root, fg="black")

# textWidget.grid(column=0,row=0)
#textWidget.pack()
# textWidget.bind('<Key>', OnKeyPress)
#root.mainloop()

"""
===================================================================
"""
# Main Loop End

# new instanse : Text Editor
root = PyTkTextEditor()
root.windows()