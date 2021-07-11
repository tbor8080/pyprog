# -*- encoding: utf-8 -*-
from time import sleep
import datetime
import tkinter
import tkinter as tk
from tkinter import ttk
import threading
from test import GUITEST
from module import *
from scra import *
from requests import request

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

def __OnClick(e):
    print()

    # new instanse : Text Editor

    root = tk.Tk()
    textwidget =tk.Text(root, height=1,width=100)
    result=tk.Text(root, height=30,width=120)
    Button=tk.Button(root,width=5)

    Button.bind('<1>',__OnClick)

    textwidget.grid(row=0,column=0)
    Button.grid(row=0,column=1)
    result.grid(row=1,columnspan=2)

    root.mainloop()

ins=ScraPy()
