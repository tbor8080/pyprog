import sys
import os
import tkinter.filedialog as fd
from time import sleep
import datetime
import tkinter
import tkinter as tk
from tkinter import ttk
from tkinter import scrolledtext

import threading

# New File & Duplicate File Save
def saveasFilePath( filetype=[ ("",".txt"), ("CSV",".csv") ] ):
    return fd.asksaveasfilename(filetypes=filetype, initialdir=os.path.abspath(os.path.dirname(__file__)))

# FileSave
def saveFile(file_name, data, encoding='utf-8'):
    with open(file_name, "wt", encoding=encoding) as fp:
        fp.write(data)


class PyTkTextEditor:

    def __init__(self, geometory='800x600'):
        # Window Geometory
        self.__geometory=geometory
        # Application Path
        self.__appdir=os.path.abspath(os.path.dirname(__file__))
        self.__fileTypes=[("*", ".txt"),("CSV", ".csv")]
        # Child Objects
        
    
    def getWindowSize(self):
        return self.__geometory.split('x')

    def __OnClick(self, e):
        print(e,self)

    def __onKeyPress__(self, e):# KeyPressEventHandle
        print(e.state, e.keycode, self.__root.focus_get(), e, self)
        if e.state==8 and e.keycode==65651:# command + s current save
            # Debug Print
            # self.asSave("sample.txt", textWidget.get("1.0","end"))

            if self.__root.filename=="":
                self.__root.title("Untitled")

            self.__root.filename=self.asSavePath(self.__fileTypes)
            self.asSave(self.__root.filename, self.widget.get("1.0","end"))

        elif e.state==8 and e.keycode==2949230:# commmand + n ( new open )
            self.widget.insert("1.0", "未実装(command + n")

        elif e.state==8 and e.keycode==2031727:# commmand + o ( open file )
            self.asOpen()

        elif e.state==9 and e.keycode==65651:# commmand + shift + s ( save multi )

            self.__root.filename=self.asSavePath(self.__fileTypes)
            self.__root.title(self.__root.filename)
            self.asSave(self.__root.filename, self.widget.get("1.0","end"))

        elif e.state==9 and e.keycode==2031727:# commmand + shift + o ( open file multi )
            self.widget.insert("1.0", "未実装(Open + Shift + O)")

        elif e.state==64 and e.keycode==7927557:# fn + F2
            self.widget.insert("1.0", "未実装(fn + F2")

    def windows(self):
        self.__root=tkinter.Tk()
        self.__root.geometry(self.__geometory)
        self.__root.filename=''
        self.__root.font=''

        self.__root.title('Untitled')
        self.__root.focus_set()
        self.__root.title(self.__root.focus_get())

        fonts=('Hiragino,Meiryo',32,'')
        width,height=self.getWindowSize()
        
        self.widget=tk.scrolledtext.ScrolledText(self.__root, bg="#fff", width=width, height=height)
        self.widget.configure(font=fonts)
        self.widget.pack()
        self.__root.bind('<Key>', self.__onKeyPress__)
        self.__root.mainloop()
        return self.__root

    def asSave(self, filename, data, encoding='utf-8'):
        with open(filename, "wt", encoding=encoding) as f:
            f.write(data)

    def asSavePath(self,filetype=[("",".txt"),("CSV",".csv")]):
        return fd.asksaveasfilename(filetypes=filetype, initialdir=self.__appdir)
    
    def asOpenPath(self, filetype=[("*",".txt"),("csv",".csv")]):
        return fd.askopenfilename(filetypes=filetype,initialdir=self.__appdir)
    
    def asOpen(self):
        self.__root.filename=self.asOpenPath(self.__fileTypes)
        self.__root.title(self.__root.filename)
        self.__root.focus_set()
        text=''
        with open(self.__root.filename, 'rt') as fp:
            text=fp.read()
        self.widget.insert("1.0", text)