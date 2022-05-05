# -*- coding: utf-8 -*-

import sys,os
from time import sleep
import random
import threading
import json

"""
    * TyPy Class

    -- Description:
        1. "sample.py" Text write >>
            
            from pypy import typy

            instanse=None

            if __name__ == "__main__":
                instanse=typy.TyPy()

            - # Program Test
            - # instanse.test()
            - instance.run()

        2. terminal(OSX) or shell console >>
            - python sample.py + Enter
            - * start program *
"""
class TyPy:
    
    def __init__(self):
        # Initialize TyPy
        self.__TyPy={
            "__Version__":"0.5 alpha",
            "__AppName__":"Typy",
            "__ProgLang__":"Python",
            "__Lang__":"ja",
            "__ChrSet__":"utf-8"
        }
        self.__Data=[]
        self.__lineData=""
        self.__t=0
        self.__missCount=0
        self.__lineLogNum=0
        self.__validateLine=""
        self.__TyPyCount=1
        self.__TyPyColor={
            "BLACK":'\033[30m',
            "RED":'\033[31m',
            "GREEN":'\033[32m',
            "END":'\033[0m',
            "UNDERLINE":'\033[4m',
        }
        self.__selfTimerData=0
    
    def __getVersion(self):
        return self.__TyPy["__Version__"]

    def __getAppName(self):
        return self.__TyPy["__AppName"]

    def __getLang(self):
        return self.__TyPy["__Lang__"]

    # Get Data
    """
        - csv
        - json:
            {"name":"typing for console/program by Python.","type":"json","data":[]}
        - sql
    """
    def __getData(self):
        return self.__Data[random.randint(0,len(self.__Data)-1)]

    def getLineData(self):
        return self.__lineData
    
    def setLineData(self,line):
        self.__lineData=line

    def getTime(self):
        return self.__t

    def setTime(self,t):
        self.__t=t

    # Self Timer
    def selfTimer(self, t):
        for i in range(t,-1,-1):
            # print(i)
            self.setTime(i)
            sleep(1)
        return self.getTime()

    def getSelfTimerData(self):
        return self.__selfTimerData

    def setSelfTimerData(self, num):
        self.__selfTimerData=num

    # 入力文字数 / Input Char Num
    def getLineLog(self):
        return self.__lineLogNum

    def setLineLog(self, line):
        self.__lineLogNum+=len(line)

    def getMissCount(self):
        return self.__missCount

    def setMissCount(self):
        self.__missCount+=1
    
    def getValidateLine(self):
        return self.__validateLine.lower()

    def setValidateLine(self, data):
        self.__validateLine=data
    
    def isNotValidateLine(self, line):
        if self.getValidateLine()!=line:
            return True
        return False
    
    def getTyPyCount(self):
        return self.__TyPyCount

    def setTyPyCount(self):
        self.__TyPyCount+=1

    def printInitMsg(self,msg):
        print(msg)
    
    def printProgram(self, line):
        
        (practice_Data, msg) = None, ""
        if len(self.__getData())>0:
            practice_Data = self.__getData()
        
        if line == "":
            print("Enterが押されました。")

        # debug print
        # print("Debug>>>",line, practice_Data, len(line), len(practice_Data))
        # Log :: Line Chr Count
        
        self.setLineLog(line)

        if self.isNotValidateLine(line):
            self.setMissCount()

        msg=f'****************************************\n'
        msg+=f'[ Practice: {self.getTyPyCount()} ]\n'
        msg+=f'[ 問題 ]=>{self.__TyPyColor["RED"]}{self.__TyPyColor["UNDERLINE"]}{practice_Data}{self.__TyPyColor["END"]}\n'
        msg+=f'--------------------------------------\n'
        msg+=f'[残り時間はあと：{self.getTime()}秒です。]\n'
        msg+=f'--------------------------------------\n'
        msg+=f'{self.__TyPyColor["GREEN"]}現在の入力文字数：{self.getLineLog()}| '
        msg+=f'現在のタイプミス回数:{self.getMissCount()}回です。{self.__TyPyColor["END"]} \n'
        msg+=f'****************************************\n'
        print(msg)

        # 現在の入力文字を保持
        self.setValidateLine(practice_Data)
        # ループカウンター
        self.setTyPyCount()

    def printFinishProgramMsg(self,type):
        msg=f''
        if type=="q":
            msg=f'{type}が押されました。プログラムを終了します。\n'
            msg+=f'- 中断までに入力された文字数は{self.__TyPyColor["GREEN"]}[{self.getLineLog()}文字]{self.__TyPyColor["END"]}でした。'
        elif type==0:
            msg=f'時間が経過しました。（{type}秒）'
            msg+=f'- 入力された文字数は{self.__TyPyColor["GREEN"]}[{self.getLineLog()}文字]{self.__TyPyColor["END"]}でした。\n'
        
        msg+=f'- うち、タイプミス回数は{self.__TyPyColor["UNDERLINE"]}[{self.getMissCount()}回]{self.__TyPyColor["END"]}です。\n'
        msg+=self.printFinishErrorCount()
        msg+=f'ご利用ありがとうございました。\n'

        print(msg)

    def printFinishErrorCount(self):
        msg=f''
        if self.getMissCount()==0:
            msg=f'パーフェクト！素晴らしい！！'
        elif self.getMissCount()>0 and self.getMissCount()<=5:
            msg=f'この調子でいきましょう、目指せ！パーフェクト！！'
        elif self.getMissCount()>6 and self.getMissCount()<=10:
            msg=f'キーボードの配列を覚えるまで練習しましょう'
        else:
            msg=f'もっと頑張りましょう'
        msg+='\n'
        return msg

    def getProgData(self):
        return self.__Data

    def setProgData(self, p):
        self.__Data.append(p)

    #データの読み込み（csv/net)
    def setTyPyDataLoad(self):
        try:
            pass
        except NameError:
            pass
        pass

    def TyPyThread(self):
        return 0

    def test(self):
        pass
        for i in range(0,50):
            self.setProgData("Sample"+str(i))
        #print(self.__getVersion())

    """
        未実装
        入力データのデータ保存
    """


    def __debug(self):
        pass
    
    def setToJsonData(self,file):
        # JSONデータを抽出、self.__Dataに格納
        data={}
        with open(file,"rt") as fp:
            data=json.load(fp)
        words=data["word"]
        self.__Data = []
        for w in words:
            self.__Data.append(w["roma"])

    def TyPyMainLoop(self):
        file = "./json/typy.json"
        # print(os.path.isfile(file))
        self.setToJsonData(file)
        # print(self.__getData())
        # exit()
        # Jsondataからwordのみを抽出・読み込み
        # init variable in TyPyMainLoop
        (lineInitMsg,lineMsg) = f"", f"[ Press Enter !! ] >>"
        
        self.setSelfTimerData(60)
        # プログラム開始時に表示されるメッセージ
        lineInitMsg = f"""
#######################################################################
        [[[ タイピング練習を開始します ]]]
            > 制限時間は{self.getSelfTimerData()}秒。
            
            > 入力したら、Enter Keyを押すと次の問題に進みます。
            > ※ 終了する場合は[ q + Enter Key ]で終了するよ
            > {self.getSelfTimerData()}秒で何文字打てるかな？
            > 問題は半角英数字で出題されます。
            > （大文字/小文字は区別しません。）
            > 準備はいいかな？（Enter Keyを押してね。） 
#######################################################################
        """

        self.printInitMsg(lineInitMsg)        
        
        sleep(0.5)

        # SelfTimer / Thread
        TyPyThread_SelfTimer = threading.Thread(target=self.selfTimer, args=(self.getSelfTimerData(),))
        TyPyThread_SelfTimer.setDaemon(True)
        TyPyThread_SelfTimer.start()
        # loop counter
        counter = 0
        while True:
            
            if counter > 0:
                lineMsg = '[問題]に書かれている文字をタイピングしてください >>'

            line=input(lineMsg)
            
            if line=="q":
                self.printFinishProgramMsg(line)
                break
            if self.getTime()==0:
                self.printFinishProgramMsg(self.getTime())
                break
            # データなし
            if len(self.__Data)==0:
                print(f'データがありません。プログラムを終了します。')
                break
            
            self.printProgram(line)
            
            counter += 1

    def run(self):
        self.TyPyMainLoop()
