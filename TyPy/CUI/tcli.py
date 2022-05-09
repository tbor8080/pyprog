import sys,os,datetime,json

try:
    import pykakasi
except ModuleNotFoundError:
    msg = """Module: pykakasi is not found. 
    -------------------------------------------------------------------
    $ pip install pykakasi
    $ open https://github.com/miurahr/pykakasi
    
    PyKakasi::
    Copyright (C) 2010-2021 Hiroshi Miura and contributors(see AUTHORS)
    -------------------------------------------------------------------
"""
    print(msg)
    exit()

class TypyConsole:
    
    def __init__(self):
        self.__appname__ = 'Typing for Python CLI'
        self.__dataPath__ = './json/word_jpn_n.json'
        self.__filename__ = './json/typy.json'
        self.__json__ = {"name":self.__appname__,"regist_date":None,"word":[]}
        self.__args__ = []
        self.__data__ = []
        self.__command__,self.__option__="",[]

    # 変数（__json__）の初期用
    def initTyPyJson(self):
        self.__json__ = {"name":self.__appname__,"regist":None,"word":[],"up_to_date":self.getDateNow()}

    def getArgv(self):
        for x in sys.argv:
            self.__args__.append(x)
        return self.__args__
    
    def getCommand(self):
        return self.__command__
    
    def setCommand(self,command):
        self.__command__= command

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
            with open(self.getTyPyFile(),'rt') as fp: # typy.json
                self.__json__ = json.load(fp)
                if type(self.__json__) is not dict: # dictではないデータは誤り
                    # 変数の初期化
                    self.initTyPyJson()
        return self.__json__
                    
    # self.__json__のみ返す
    def getTyPyJson(self):
        return self.__json__
    
    # 配列操作まで
    def setTyPyJson(self,word={}):
        self.__json__["word"].append(word) # -> dict
    
    def modifyTyPyJson(self,num=0,word=None):
        # 単語の変更
        self.getTyPyJson()[num]["lemma"] = word

    # 保存も行う
    def setTyPyJsonData(self,word={}):
        self.__json__["word"].append(word) # -> dict
        self.saveTyPyJson(self.__json__)
    
    # self.getTyPyFile()ファイルに保存のみ行う。
    def saveTyPyJson(self,data):
        # 上書き保存
        with open(self.getTyPyFile(), "wt") as fp:
            fp.write(json.dumps(data))

    def getWordJsonData(self):
        with open(self.getDataPath(),'rt') as fp:
            self.__data__ = json.load(fp)
        return self.__data__

    def getWordJson(self):
        return self.__data__

    def setWordJsonData(self,word):
        self.__data__.append(word) # -> list

    def getDateNow(self):
        return datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    # ---------------------------------------------------------------------------------------------------    
    def search(self,word=None):
        if word is None:
            word = input("単語を入力してください>>")

        lemmas = []
        for w in self.getTyPyJson()["word"]:
            if word in w["lemma"]:
                lemmas.append((w["num"],w["lemma"]))

        # self.logging()
        # print(lemmas)
        for l in lemmas:
            msg=f"""---
    wordid:{l[0]} / lemma:{l[1]}
---"""
            print(msg)
        exit()

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

    def init(self):
        init_txt = input(f"{self.getTyPyFile()}の初期化をします。>[Y/n]")
        if init_txt.upper() == "Y":
            # 初期化(self.__json__)
            self.initTyPyJson()
            # wordnet dataからコピー
            data = self.getWordJsonData()
            self.__json__["word"] = data
            with open(self.getTyPyFile(), "wt") as fp:
                fp.write(json.dumps(self.getTyPyJson()))
            msg = """初期化が終了しました。"""
            print(msg)
            print(self.getTyPyJsonData()["name"],self.getTyPyJsonData()["up_to_date"],self.getTyPyJsonData()["word"][:50])

    def modifyROMA(self,typy_data):
        # ローマ字変換 一括
        kks = pykakasi.kakasi()
        print("変換中.... >>")
        for data in typy_data["word"]:
            data["roma"] = kks.convert(data["lemma"])[0]["passport"].upper()
            msg = f'''[確認用]:{data["lemma"]}/{data["roma"]}'''
            print(msg)
    
    def roma(self):
        data = self.getTyPyJsonData()
        if self.isTyPyFilePath() is False:
            print(f'ファイル:{self.isTyPyFilePath()}が存在しないため、新規作成しました。')
            self.saveTyPyJson(data)
            print("ファイルの保存が終了しましたので、再度$ python cmd.py romaを実行してください。")
        else:
            line = input(f"単語にローマ字を追加します。（この変換には時間がかかりますが、実行しますか？）[Y/n]")
            if line.upper() == "Y":
                self.modifyROMA(data)
                self.saveTyPyJson(data)
                print("上書き保存しました。")
            else:
                print("処理を中断しました。")
    
    def ls(self,words):
        option = self.getOption()
        num = 5
        list_word = []
        if len(option)>0:
            try:
                # 数値を代入
                num = int(option[0])
            except ValueError:
                # 例外：その他の場合はそのまま代入
                num = option[0]
            # print(num,type(num))
            if type(num) is str and num == "all" :
                if "y".upper() == input(f"{len(words)}件のデータを閲覧しようとしています。よろしいですか？[Y/n]"):
                    # print(words)
                    list_word = words
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
                list_word = words[nums[0]:nums[1]]

            elif type(num) is int:
                list_word.append(words[num-1])
        else:
            list_word = words[:num]
        for i in range(0,len(list_word)):

            msg = f""" [[ 登録単語 ]]
-----------------------------------------------------------------------
    <num:登録番号>      {list_word[i]["num"]}
    <lemma:単語>       {list_word[i]["lemma"]}
    <roma:ローマ字>     {list_word[i]["roma"]}
    <pos:分類>          {list_word[i]["pos"]}
-----------------------------------------------------------------------
"""
            print(msg)
            input("Enterを押してください。:")
    
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
        word = input("削除したい単語を入力してください。")
        self.search(word)

    def mv(self):
        word = input("変更したい単語を入力してください。")
        self.search(word)

    def help(self):
        cli='($ sh tc or $ python -m tcli)'
        msg = f"""###################################################################################################
###################################################################################################
* [ヘルプ]
    *
    * github: https://github.com/tbor8080/0x00
    * copyright: 0x00@00000000
    * © 0x00 ,2021-2022
    * 
    list/ls: Typyに登録されている単語を表示します。
        [例]
        # 先頭から5件のデータを表示します。
        $ {cli} ls
        # 50番目のデータを表示します。
        $ {cli} ls 50 
        # 先頭から50件のデータを表示します。
        $ {cli} ls :50 
        # 全件表示
        $ {cli} ls all
    ----------------------------------------------------
    count : 登録件数を表示します
    ----------------------------------------------------
    search : 登録ワードの検索(仮実装)
    ----------------------------------------------------
    init : データの初期化を行います
    ----------------------------------------------------
    create : データの作成をします
    ----------------------------------------------------
    add : データの追加をします
    ----------------------------------------------------
    rm : 未実装
    ----------------------------------------------------
    mv : 未実装
===================================================================================================
    単語データには[ WordNet ]を利用しています。
    日本語ワードネット （1.1版）
    © 2009-2011 NICT, 2012-2015 Francis Bond and 2016-2017 Francis Bond, Takayuki Kuribayashi
    URL: http://compling.hss.ntu.edu.sg/wnja/index.ja.html
==================================================================================================
###################################################################################################"""
        print(msg)
        
    def debug(self,txt):
        print("debug>>",txt)
    
    def logging(self):
        logfile = './log/tcli.log'
        txt = f'[{self.getDateNow()}] command:{self.getCommand()}/option:{self.getOption()}'
        with open(logfile, "wt") as fp:
            fp.write(txt)

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
        elif command == "init":
            self.init()
        elif command == "search":
            self.search()
        elif command == "roma":
            self.roma()
        elif command == "help" or command == "h":
            self.help()
        self.logging()
# --------------------------------------------------------------------------------------------------------

if __name__ == "__main__":
    TypyConsole().run()