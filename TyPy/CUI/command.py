import sys,os
import json
import pykakasi
import datetime

class TypyConsole:
    
    def __init__(self):
        self.__appname__ = 'Typing for Python'
        self.__dataPath__ = './json/word_jpn_n.json'
        self.__filename__ = './json/typy.json'
        self.__json__ = {"name":self.__appname__,"regist":None,"word":[]}
        self.__args__ = []
        self.__data__ = []
        self.__command__,self.__option__="",[]

    def getArgv(self):
        for x in sys.argv:
            self.__args__.append(x)
        return self.__args__
    
    def getCommand(self):
        return self.__command__
    
    def setCommand(self,command):
        self.__command__=command

    def getOption(self):
        return self.__option__
    
    def setOption(self,op):
        self.__option__=op

    def getDataPath(self):
        return self.__dataPath__

    def isWordDataPath(self):
        # True | False
        return os.path.isfile(self.__dataPath__)

    def isTyPyFilePath(self):
        # True | False
        return os.path.isfile(self.__filename__)

    def getAppName(self):
        return self.__appname__
    
    def setAppName(self, name=None):
        if name is not None:
            self.__appname__=name
    
    def getTyPyFile(self):
        return self.__filename__

    def getTyPyJsonData(self):
        if self.isTyPyFilePath() is False:
            with open(self.getDataPath(),'rt') as fp:
                self.__json__["word"] = json.load(fp)
        else:
            with open(self.getTyPyFile(),'rt') as fp:
                self.__json__ = json.load(fp)
        return self.__json__
    
    def setTyPyJsonData(self,word={}):
        self.__json__["word"].append(word) # -> dict
        self.saveTyPyJson(self.__json__)
    
    # self.getTyPyFile()ファイルに保存。
    def saveTyPyJson(self,data):
        # 上書き保存
        with open(self.getTyPyFile(), "wt") as fp:
            fp.write(json.dumps(data))

    def getWordJsonData(self):
        return self.__data__
    
    def setWordJsonData(self,word):
        self.__data__.append(word) # -> list

    def getDateNow(self):
        return datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    # ---------------------------------------------------------------------------------------------------    

    def create(self):
        data = self.getTyPyJsonData()
        if self.isTyPyFilePath() is False:
            with open(self.getTyPyFile(), "wt") as fp:
                fp.write(json.dumps(data))
        else:
            line = input(f"{self.getTyPyFile()}は存在しています。上書き作成しますか？[Y/n]")
            if line.upper() == "Y":
                with open(self.getTyPyFile(), "wt") as fp:
                    fp.write(json.dumps(data))
                print("上書き保存しました。")
            else:
                print("処理を中断しました。")

    def modifyROMA(self,typy_data):
        # ローマ字変換 一括
        kks = pykakasi.kakasi()
        print("変換中.... >>")
        for data in typy_data["word"]:
            data["roma"] = kks.convert(data["lemma"])[0]["passport"].upper()
        print(self.__json__["word"][:2],len(self.__json__["word"]))
    
    def roma(self):
        data = self.getTyPyJsonData()
        if self.isTyPyFilePath() is False:
            print(f'ファイル:{self.isTyPyFilePath()}が存在しないため、新規作成しました。')
            with open(self.getTyPyFile(), "wt") as fp:
                fp.write(json.dumps(data))
            print("ファイルの保存が終了しましたので、再度$ python cmd.py romaを実行してください。")
        else:
            line = input(f"単語にローマ字を追加します。（この変換には時間がかかりますが、実行しますか？）[Y/n]")
            if line.upper() == "Y":
                self.modifyROMA(data)
                with open(self.getTyPyFile(), "wt") as fp:
                    fp.write(json.dumps(data))
                print("上書き保存しました。")
            else:
                print("処理を中断しました。")
    
    def ls(self,words):
        option=self.getOption()
        # print(option)
        num=5
        if len(option)>0:
            try:
                # 数値を代入
                num=int(option[0])
            except ValueError:
                # 例外：その他の場合はそのまま代入
                num=option[0]
            # print(num,type(num))
            if type(num) is str and num == "all" :
                if "y".upper() == input(f"{len(words)}件のデータを閲覧しようとしています。よろしいですか？[Y/n]"):
                    print(words)
            elif type(num) is str and ":" in num:
                nums = num.split(":")
                # print(nums)
                if nums[0]=="" and nums[1]=="":
                    # 全ての件数表示は怖いので、1/100件数
                    nums=["0",f"{int(len(words)/100)}"]
                if nums[0]=="":
                    nums[0]=0
                if nums[1]=="":
                    nums[0],nums[1] = int(nums[0]),len(words)
                else:
                    nums[0],nums[1] = int(nums[0]),int(nums[1])
                # print(nums[1])
                print(words[nums[0]:nums[1]])
            elif type(num) is int:
                print(words[num-1]["lemma"])
        else:
            print(words[:num])
    
    def count(self,words):
        return len(words)
    
    def insertData(self,word):
        w = self.getTyPyJsonData()['word']
        roma = pykakasi.kakasi().convert(word)[0]["passport"].upper()
        num = int(self.count(w)+1)
        pos = "名詞"
        words = {"num":num,"lemma":word,"pos":pos,"roma":roma}
        if input("保存しますか？>").upper() == 'Y':
            self.setTyPyJsonData(words)
            print(len(self.getTyPyJsonData()["word"]),f"{self.getTyPyFile()}に保存しました。")
        else:
            print("保存を中断しました。")

    def add(self):
        print(f"現在、{self.count(self.getTyPyJsonData()['word'])}件の登録があります。")
        line = input("単語を入力してください。>>")
        self.insertData(line) 

    def rm(self):
        pass

    def mv(self):
        pass

    def help(self):
        msg = f"""
[利用方法]

    list/ls: Typyに登録されている単語を表示します。
        $ python -m cmd ls
        $ python -m cmd ls 50
        $ python -m cmd ls :50
        $ python -m cmd ls all
    [option]




count

##############################################################################"""
        print(msg)
    def debug(self,txt):
        print("debug>>",txt)

    def run(self):
        argv=self.getArgv()
        if len(argv) > 1:
            self.setCommand(argv[1])
        if len(argv) > 2:
            self.setOption(argv[2:])
        command = self.getCommand()
        # get json
        data = self.getTyPyJsonData()
        # self.debug(len(data["word"]))
        # exit()
        # 単語コレクション
        words = data["word"]
        # list
        if command == "ls" or command == "list":
            self.ls(words)
        # length
        elif command == "count" or command == "len":
            length = self.count(words)
            print(f"{length}個の単語データ（日本語）が登録されています。")
        # add
        elif command == "add":
            self.add()
        # rm
        elif command == "rm":
            self.rm(words)
        # mv
        elif command == "mv":
            self.mv(words)
        elif command == "create":
            self.create()
        elif command == "roma":
            self.roma()
        elif command == "help" or command == "h":
            self.help()

# --------------------------------------------------------------------------------------------------------

if __name__ == "__main__":
    TypyConsole().run()