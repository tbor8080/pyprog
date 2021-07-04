import tkinter
from tkinter import ttk
import threading
import time
from time import sleep
import datetime

"""
Tk Interface Class
    - TextEditor => ctrl+s | command+s => [ Save ]
    - Modal Dialog : ctrl + shift + s | command + shift + s => [ Change Name Save ] 
"""

class TkPy:
    """
        * new instanse
        - instanse=tktmpy.TkTmPy(title='New Window',geometry='800x400')
        - instanse.TextEditor()
        - instanse.Memo()
        - instance.Calc()
        - instance.Calender()
        - instanse.Timer()
    """
    def __init__(self, title="Tkinter GUI Window", geometry="800x600"):
        self.__root=tkinter.Tk()
        self.__root.title(title)
        self.__root.geometry(geometry)
        self.__TimerNow=datetime.datetime.now()
    
    def getTimer(self):
        return self.__TimerNow

    def setTimer(self):
        self.__TimerNow=datetime.datetime.now()
    
    def OneLineEditor(self):
        pass

    def TextEditor(self, column=0, row=0):
        textEditMultiLine=tk.Text(self.__root)
        textEditMultiLine.grid(column=column, row=row, sticky=(tk.N,tk.S,tk.E,tk.W))
        textEditMultiLine.pack()
        self.setTextEditorFileName("TextEditor.txt")
        textEditMultiLine.bind('<Key>', self.TextEditorOnKeyPress)
    
    def getTextEditorFileName(self):
        return self.file_name

    def setTextEditorFileName(self, fn):
        self.file_name=fn

    # Text Editor Event Handle
    def TextEditorOnKeyPress(self, e):
        print(e)# Event Handler
        if e.keycode==65651:# command+s    
            self.TextEditorSave(self.getTextEditorFileName())

    def TextEditorSave(self, fn, data, encoding='utf-8'):
        with open(file_name, "a", encoding=encoding) as fp:
            fp.write(data)

    def TkPyMainLoop(self):
        self.__root.mainloop()
    
    def run(self):
        self.TkPyMainLoop()

###################################### Test Block(Class) #############
# Initilize Application
test01=TkPy()
test02=TkPy(geometry='480x480')
# Application Code

# Run Program
test01.run()
test02.run()
# print(test01,test02)
###################################### Test Block(Class) #############