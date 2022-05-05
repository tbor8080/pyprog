# coding: UTF-8
from time import sleep
import tkinter
import sys
# This Program is Python3 higher
if sys.version_info.major > 2 and sys.version_info.minor > 5:
    pass
else:
    print(sys.version)
    exit()

try:
    import random
except ModuleNotFoundError as e:
    #print('Module: ramdomがimportされていません。')
    pass

try:
    import threading
except ModuleNotFoundError as e:
    print(f'Module: threadingがimportされていません。')

try:
    from time import sleep
except ModuleNotFoundError as e:
    print(f'Module: {module}がimportされていません。')
    print(f'Typing>> from time import {module}')
except NameError:
    print(f'Module: {module}が見つかりませんでした。')
except ImportError:
    print(f'Import Error:{module}の場所がわかりません。')

"""
[[ Typy:Typing Pythonware Prototype(CUI) ]]
    - 
    - [ Developer ]: [Hongo Academy Python & Computer Science Subject Class] Anonimas (s)he
    - [ Date ]: 2021/05/06 - 2021/07/31
    - [ License ]: MIT License
    - [ Github Coding Project ]:https://github.com/tbor8080/TyPy
    - [ Github Dev URL ]:https://github.com/tbor8080
    - [ Github Pages URL ]:https://tbor8080.github.com/
    
    > Like "A Hack Culture."
    > 
    > This code is prototyping software.
    
    && TyPy is Free Software.
    
    (Lile a "I'd like to dance with you!",)
"""

from pypy import typy

time_v=0

def tk_test():
    #tkinter._test()
    for i in range(0,1000000):
        print(i)

def sleep_test():
    for i in range(60,-1,-1):
        global time_v
        time_v=i
        sleep(1)

def mistakeMsg(num):
    msg=""
    if  num == 0:
        msg="完璧"
    elif num < 5:
        msg="素晴らしい"
    else:
        msg="もっと練習しましょう"
    return msg

def main():
    text_data=["IITENKIDESUNE","CATV","KAKARICHOU","SOUDAN","SOUSOU"]
    counter=0
    mistake=0
    
    line_log=0
    thread01=threading.Thread(target=sleep_test)
    print("Python Type writer alpha v.0.00000001")
    sleep(0.1)
    thread01.setDaemon(True)
    thread01.start()

    while True:
        counter+=1
        mondai=text_data[random.randint(0,len(text_data)-1)]
        print(f'\n[問題{counter}：{mondai} | <残り時間：{time_v}秒>]')
        sleep(0.01)
        line_string='文字入力の練習しましょう！＞＞入力してください。\n([q+Enter]または[Ctrl+c]で終了）\n'
        line=input(line_string)
        line_log+=len(line)
        if line.upper()!=mondai:
            mistake+=1
        if line=="q":# ord("q") -> chr code: 113
            break
        elif line=='s':# ord("s") -> chr code: 115
            pass
        if time_v==0:
            msg=mistakeMsg(mistake)
            print(f"60秒が経過したので終了します。\n入力した文字数は{line_log}文字です。\n|{msg}|そのうちタイプミスは{mistake}回です。")
            break
        print(line,f'/Miss:{mistake}\n\n')
        sleep(0.2)
    
instanse=typy.TyPy()
instanse.run()