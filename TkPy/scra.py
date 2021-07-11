
from time import sleep
import datetime
import tkinter
import tkinter as tk
from tkinter import ttk
import threading
import requests

class ScraPy:
    def __init__(self):
        self.app="Scra.Py"
        self.__root = tk.Tk()
        # self.__root.geometry('800x600')
        self.textwidget =tk.Text(self.__root, height=1,width=100)
        self.textwidget.insert('1.0','https://www.google.co.jp/')
        self.result=tk.Text(self.__root, height=30,width=120)
        self.result.configure(state='disabled')
        self.Button=tk.Button(self.__root,width=5,text='Click')

        self.Button.bind('<1>',self.__OnClick)

        self.textwidget.grid(row=0,column=0)
        self.Button.grid(row=0,column=1)
        self.result.grid(row=1,columnspan=2)

        self.__root.mainloop()
    
    def getHtml(self):
        pass

    def __OnClick(self,e):
        print(e)
        self.result.configure(state='normal')
        self.result.delete('1.0','end')
        url=self.textwidget.get("1.0","end")

        r=requests.get(url)
        self.result.insert('1.0', url)
        self.result.insert('1.0', r.text)
        self.result.configure(state='disabled')