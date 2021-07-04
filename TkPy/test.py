import tkinter
import tkinter as tk
from tkinter import ttk

def GUITEST():
    # print(ttp._getNowTime())
    root=tkinter.Tk()
    root.geometry("800x400")

    #print(datetime.datetime.now(), datetime.date.today())


    # Frame=ttk.Frame(root, padding=16)
    # Label=tkinter.Label(text="現在時刻は"+str(ttp._getNowTime()))
    # Timer=threading.Thread(target=updateTime)
    # Timer.start()
    textWidget=tk.Text(root)
    textWidget.grid(column=0,row=0,sticky=(tk.N,tk.S,tk.E,tk.W))
    # Entry = ttk.Entry(Frame, textvariable=setTimer)

    # Frame.pack()
    # Entry.pack()
    # Label.pack()


    # root.columnconfigure(0, weight=1)
    # root.rowconfigure(0, weight=1)
    root.mainloop()
    # setTimer(60)
    count=0
