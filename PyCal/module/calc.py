# -*- coding: utf-8 -*-
import os,sys,datetime
import tkinter as tk
import tkinter.filedialog as fd
from tkinter import scrolledtext
from PIL import Image, ImageTk

# Self Certificate 2021.07.17S
digit='''
-----BEGIN CERTIFICATE-----
MIIDrTCCApWgAwIBAgIULl3Kk0SvSaL3bzyuEnewpKKB+FAwDQYJKoZIhvcNAQEN
BQAwZjELMAkGA1UEBhMCSlAxDjAMBgNVBAgMBUNoaWJhMSEwHwYDVQQKDBhJbnRl
cm5ldCBXaWRnaXRzIFB0eSBMdGQxJDAiBgkqhkiG9w0BCQEWFXJ5b2hlaS5zdWdh
QGdtYWlsLmNvbTAeFw0yMTA3MTUxMjE0MDRaFw0zMTA3MTMxMjE0MDRaMGYxCzAJ
BgNVBAYTAkpQMQ4wDAYDVQQIDAVDaGliYTEhMB8GA1UECgwYSW50ZXJuZXQgV2lk
Z2l0cyBQdHkgTHRkMSQwIgYJKoZIhvcNAQkBFhVyeW9oZWkuc3VnYUBnbWFpbC5j
b20wggEiMA0GCSqGSIb3DQEBAQUAA4IBDwAwggEKAoIBAQCwqsxUTqhuUG+gwS83
kuDhwUMuymUj9zi+LsfqiqIggmf4AIc7KiQZak+pF3CV4z9GNOSsDgUoF5x1fYq9
/WraKv3RIfC56wh9KS2O90RX61e+6dqPN8eckV5LBNkK5CDAULuPhf+HmMeJKNNL
nWhCDHirIJUiD3Nt+Q90cZsCH8758g0co15ekQFQ0+yXQuCF/ccpbZ0RJwmokCs9
m+5M34e7K1DzmNWaIcxmGwtiGOcz1Rns5w1cuq1ul9pNeSUtsTH+bB/KZmpHs6Ma
sU1+4iZ/KGoQeKe6DWPH62aNM6oXkr0wJeJ/0D6mQDB8KUy9N90tM9ReYNI0dY36
YuSLAgMBAAGjUzBRMB0GA1UdDgQWBBS5h2OeDghZlZaQL5P7jKAf7LQOZzAfBgNV
HSMEGDAWgBS5h2OeDghZlZaQL5P7jKAf7LQOZzAPBgNVHRMBAf8EBTADAQH/MA0G
CSqGSIb3DQEBDQUAA4IBAQAtjRxXd5vgJ6hvrhW60HBjHqkbSsKxh/esGDwBkg0Q
ktZ6H1oS+Z41d7vH6DO4bBf7cLvFt7/dSHlMMa+k1qwRZdGtcq7MgVCch13ffnwa
+zQHv9eAqXQBJtvPZ1Pl5YPsoQsIrBgXRMst2KlD8zW5HyVmAKqrT6/RIcYV/m40
YFooBUeRnQFBC4u463bs+MMe0+kDRApFepcLbJNWWJ3B33kJFvnj/wZjqIWk0xKb
U1D+L6TssYx7GpsqH8AnYlaSY/M64rG5mfE6rGob3/9QDdewf6YFEo9d2ESzyLgb
SuqA/vaA6DF/2dV2vRioohK5MGkvQDUTqCbI1aHIrQvj
-----END CERTIFICATE-----
'''

class Calc:

    def __init__(self):
        self.App={
            'Name':'CalcPy Tk',
            'Set':['+','-','*','/','=','C'],
            'Developer':'Ryohei Suga.',
        }
        self.Button=[]
        self.History=[]
        self.Keycode={
            'num':[48,49,50,51,52,53,54,55,56,57], # 0-9
            'op':[42,43,45,47,2359309]# オペランド
        }
        #self.key_code_op=
    def getDate(self):
        return datetime.datetime.today().strftime('%Y-%m-%d')
    
    def CalcOnClick(self, e):
        text=e.widget['text']
        string=self.textOneLine['text']+text
        
        if text!='C' and text!='=' and text!='+' and text!='-' and text!='*' and text!='/':
            self.text.set(string)
        
        # Clear and Return( Equal )
        if text=='C':
            self.text.set('')
            self.History.clear()
        elif text=='=':
            self.text.set('')
            self.History.clear()
        
        if text=='+' or text=='-' or text=='*' or text=='/':
            self.History.append(self.textOneLine['text'])
            self.History.append(text)
        
        if len(self.History)>3:
            self.History.append(string)
            del self.History[:2]
        
        if len(self.History)>0:
            # 
            pass
        print(self.History, text, string)

    def CalcOnKeyPress(self, e):
        string=''
        print(e)
        for c in range(0,len(self.Keycode['num'])):
            if e.keycode==self.Keycode['num'][c]:
                string=self.textOneLine['text']+e.char
                string=string.replace('+', '').replace('-', '').replace('*', '').replace('/', '')
                self.text.set(string)

        for c in range(0,len(self.Keycode['op'])):
            if e.keycode==self.Keycode['op'][c]:
                self.History.append(self.textOneLine['text'])
                self.History.append(e.char)
                self.text.set(e.char)
                print(e.char)
        
        # 42(-), 43(+), 45(*), 47(/)
        if e.keycode==3342463:
            # self.History.remove(self.textOneLine['text'])
            print(self.History)
            print(self.textOneLine['text'])
            self.text.set('')
        
        print(self.History)

        # Return Code
        if e.keycode==2359309:
            pass

    def TextEditOnKeyPress(self,e):
        print(self.textOneLine['text'])

    def loop(self):
        self.root=tk.Tk()
        self.root.geometry('600x600')
        # Frame1: logo/date
        Frame=tk.Frame(self.root)

        pylogo='image/py.png'
        # Python Logo
        self.img=ImageTk.PhotoImage(Image.open(pylogo))
        self.pyLogoLabel=tk.Label(Frame, bg='white', image=self.img)
        self.text=tk.StringVar()
        self.pyLogoLabel.grid()
        
        # Result View
        font=('Meiryo', 48)
        self.textOneLine=tk.Label(Frame, font=font, height=1, textvariable=self.text, bg='white')
        self.textOneLine.grid()
        # self.textOneLine.bind('<Key>', self.TextEditOnKeyPress)

        dateNow=tk.Label(Frame, text=self.getDate())
        dateNow.grid()
        Frame.grid(columnspan=2,row=0)

        # Button [1-9]
        Frame2=tk.Frame(self.root)
        row=0
        font=('Courier', 12)
        for b in range(0, 9):

            if b%3==0:
                row+=1

            self.Button.append(tk.Button(Frame2, font=font, width=3, height=3, text=str(b+1)))
            self.Button[b].bind('<1>', self.CalcOnClick)
            self.Button[b].grid(column=b%3, row=row)

        # Button [0]
        self.Button.append(tk.Button(Frame2, font=font, width=15, height=3, text='0'))
        num=len(self.Button)-1
        self.Button[num].bind('<1>', self.CalcOnClick)
        self.Button[num].grid(columnspan=3, row=row+1)
        self.root.bind('<Key>', self.CalcOnKeyPress)

        Frame3=tk.Frame(self.root)
        for b in range(0,len(self.App['Set'])):
            self.Button.append(tk.Button(Frame3, width=3, height=2, text=str(self.App['Set'][b])))
            num=len(self.Button)-1
            self.Button[num].bind('<1>', self.CalcOnClick)
            self.Button[num].grid()
        
        Frame2.grid(column=0,row=1)
        Frame3.grid(column=1,row=1)

        self.root.mainloop()

    def run(self):
        self.loop()

    