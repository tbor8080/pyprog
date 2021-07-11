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
root = tk.Tk()
root.geometry("800x800")
edit=tk.Text(root, height=2,width=100)

column=[]
for i in range(0,8):
    column.append([])
    for k in range(0,16):
        column[i].append(tk.Text(root, height=1,width=10))
        column[i][k].grid(column=i, row=k,ipadx=0,ipady=0)
        
# print(column)
edit.grid(columnspan=8)

# Button.pack()
root.mainloop()