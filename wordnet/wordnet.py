# from select import *
from importlib.resources import path
import sys,os,sqlite3,json,datetime

class WordNet:
    def __init__(self):
        
        self.__version = '0.1b'
        self.__file = './wnjpn.db'
        self.__lang = 'jpn'
        self.__pos = 'n'
        self.__word = ''
        self.__args__=[]
        self.__command__=""
        self.__option__=[]
        self.__json_file__ = './json/data.json'
        self.__log_file = './log/wn.log'
        self.__pos = {('n','名詞'),('v','動詞'),('r','副詞'),('a','形容詞')}

    def getVersion(self):
        return self.__version

    # ファイルなどの存在確認
    def isFile(self,path="./"):
        return os.path.isfile(path)
    
    def isDir(self,path="./"):
        return os.path.isdir(path)
    
    def exists(self,path="./"):
        return os.path.exists(path)

    def getFilePath(self):
        return self.__file

    # Log
    def getLogFile(self):
        return self.__log_file
    
    def setLogFile(self, file):
        self.__log_file = file

    # Json File
    def getJsonFile(self):
        return self.__json_file__
    
    def setJsonFile(self, file=None):
        self.__json_file__ = file

    # Part of Speech(POS) URL:https://qiita.com/kei_0324/items/400f639b2f185b39a0cf
    def getPos(self):
        return self.__pos
    
    def setPos(self, pos='n'):
        self.__pos = pos

    # 検索言語
    def getLang(self):
        return self.__lang
    
    def setLang(self,lang='jpn'):
        self.__lang = lang
    
    # 検索ワードの生成
    def getWord(self):
        return self.__word
    
    def setWord(self,word=''):
        self.__word = word

    def __c(self):
        return sqlite3.connect(self.getFilePath())
    
    def __cur(self):
        return self.__c().cursor()

    def _c(self):
        return sqlite3.connect(self.getFilePath())
    
    def _cur(self):
        return self._c().cursor()

    # cli interface 引数の取得
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
    
    def abort(self):
        print(f'処理を中断しました。')
        exit()

    def logging(self,file='', text='', mode='a'):
        msg = f""
    
    def getDateNow(self):
        return datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    def word_count(self):
        word_count={}
        cur = self.__cur()

        select_txt = "select count(lemma) from word"
        cur.execute(select_txt)

        result = cur.fetchone()[0]
        word_count["all"] = result
        print(f"総単語数：{result}件")
        
        print('======================================')
        # 単語(Japanese)
        select_txt = "select count(lemma) from word where lang='jpn'"
        cur.execute(select_txt)
        result = cur.fetchone()[0]
        word_count["japanese"] = {"all":result}
        print(f"* 日本語：{result}件")

        # pos(a:形容詞/r:副詞/n:名詞/v:動詞)
        print('======================================')
        for p in self.__pos:
            select_txt = f"select count(lemma) from word where lang='jpn' AND pos='{p[0]}'"
            cur.execute(select_txt)
            result = cur.fetchone()[0]
            word_count["japanese"][p[0]] = result
            print(f"    {p[1]}：{result}件")

        print('======================================')

        # 単語(English)
        select_txt = "select count(lemma) from word where lang='eng'"
        cur.execute(select_txt)
        result = cur.fetchone()[0]
        word_count["english"] = {"all":result}
        print(f"* English：{result}件")

        # pos(a:形容詞/r:副詞/n:名詞/v:動詞)
        print('======================================')
        for p in self.__pos:

            select_txt = f"select count(lemma) from word where lang='eng' AND pos='{p[0]}'"
            cur.execute(select_txt)
            result = cur.fetchone()[0]
            word_count["english"][p[0]] = result
            print(f"    {p[1]}：{result}件")

        print('======================================')
        print(word_count)

        cur.close()

        self.logging(f"[処理]:メソッド:(l{sys._getframe().f_code.co_name}) : [内容]:単語数の一覧表示")

    def word_search(self):
        # inner join :word + sense
        # lang:jpn / pos:n
        search_word = input('- 検索単語を入力してください>>')
        if len(search_word) > 0:
            relational_words = {"lemma":search_word,'date':self.getDateNow()}
            cur = self.__cur()

            # 検索
            word_synset_join_serect = f"""select * from word INNER JOIN sense 
ON word.wordid=sense.wordid 
AND word.lang='{self.getLang()}'
AND sense.lang='{self.getLang()}'
AND word.lemma='{search_word}'
JOIN synset_def
ON  sense.synset=synset_def.synset
AND synset_def.lang='{self.getLang()}';
"""
            cur.execute(word_synset_join_serect)
            self.logging(f"[処理]:メソッド:({sys._getframe().f_code.co_name}) / [内容]単語検索:{search_word}({self.getLang()})")
            rows = cur.fetchall()
            print(f"検索単語:{search_word}")
            # 関連ID => 関連ワード
            result_list = []
            result_txt = ''

            count=0
            relational_words['wordid'] = rows[0][0]
            relational_words['synset']=[]
            relational_words['related_words_list']=[]
            for row in rows:

                # ID取得
                result_list.append(row[12])
                relational_words['synset'].append(row[12])

                # 関連IDの文字連結
                result_txt += f"'{row[12]}'"
                if count < len(rows)-1:

                    # 関連IDの文字連結
                    result_txt += ','
                count+=1

            # 関連ワードの抽出
            relational_word = f"""select * from word INNER JOIN sense 
ON word.wordid=sense.wordid 
AND word.lang='{self.getLang()}'
WHERE sense.synset in ({result_txt})
"""
            cur.execute(relational_word)
            self.logging(f"[処理]:メソッド:({sys._getframe().f_code.co_name}) / [内容]関連単語抽出({self.getLang()})/rid:[{result_txt}]")

            related_words = cur.fetchall()
            relational_words['related_words']=[]
            for related_word in related_words:
                relational_words['related_words_list'].append(related_word[:3])
                relational_words['related_words'].append({"wordid":related_word[0],"lang":related_word[1],"lemma":related_word[2]})
                # 画面表示
                print(f'類似・関連単語>>:WORD ID:{related_word[0]}')
                print(f"            >>:利用言語:{related_word[1]}")
                print(f'　　　　　　　>>:単語:{related_word[2]}')
                # logging
                self.logging(f"[処理]:メソッド:({sys._getframe().f_code.co_name}) / [内容]関連単語({related_word[0]}/{related_word[1]}/{related_word[2]})")
            # 集合演算
            relational_words['related_words_list']= set(relational_words['related_words_list'])
            cur.close()

    def export(self):
        self.logging(f"[処理]:メソッド:({self.getFunction()}) : [内容]:JSONファイルに書き出す。")
        cur=self.__cur()
        # 日本語　INNER JOIN
        select_txt="select wordid,lemma from word where lang='jpn';"
        self.logging(f"[処理]:メソッド:({sys._getframe().f_code.co_name}) / [内容]単語全検索({self.getLang()}):SQL文:{select_txt}")
        cur.execute(select_txt)
        rows = cur.fetchall()
        # print(rows)
        word_related={'date':self.getDateNow(),"word":[]}
        count=0
        for row in rows:
            # if count<10:
            if count%(100*60) == 0:
                print(f'{count}件進行中...')
            wordid = row[0]
            word_related["word"].append({"wordid":wordid,"lemma":row[1],"related":[]})
            select_txt=f"""select * from word
INNER JOIN sense
ON word.wordid=sense.wordid
WHERE word.lang='jpn' AND sense.lang='jpn' AND word.wordid='{wordid}';"""
            # print(select_txt)
            cur.execute(select_txt)
            self.logging(f"[処理]:メソッド:({sys._getframe().f_code.co_name}) / [内容]:関連ID抽出({count}) wordid:{wordid}/lemma:{row[1]}")
            related = cur.fetchall()
            # ridの取得
            result_txt=''
            rid_count=0
            for r in related:
                rid=r[5]
                word_related["word"][count]["related"].append(rid)
                result_txt += f"'{rid}'"
                if rid_count < len(related)-1:
                    # 関連IDの文字連結
                    result_txt += ','
                rid_count+=1
            select_text_relations = f"""select word.wordid,word.lang,word.lemma from word INNER JOIN sense 
ON word.wordid=sense.wordid 
AND word.lang='{self.getLang()}'
WHERE sense.synset in ({result_txt})
"""
            cur.execute(select_text_relations)
            self.logging(f"[処理]:メソッド:({sys._getframe().f_code.co_name}) / [内容]:関連単語抽出(lemma:{row[1]}/{count})")
            related_words=cur.fetchall()
            word_related["word"][count]["related_words"]=related_words
            # カウンター
            count+=1
        self.saveJson(self.getJsonFile(),word_related,mode='wt')
        print('ファイルを書き込みました。')

    def help(self):
        msg = '''---
検索 :
    $ sh wn search
    $ sh wn s
データ出力 :
    $ sh wn export
    $ sh wn ex
カウント : 
    $ sh wn count
    $ sh wn c
---'''
        print(msg)
        self.logging(f"[処理]:メソッド:({sys._getframe().f_code.co_name}) / [内容]:ヘルプ表示")

    def getFunction(self):
        return sys._getframe().f_code.co_name

    def logging(self, log):
        msg = f"[{self.getDateNow()}] {log}"
        self.save(self.__log_file, msg, mode='a')

    def save(self, file=None, data="", mode='wt',encoding='utf-8'):
        if file is not None:
            with open(file,mode,encoding=encoding) as fp:
                if mode == 'a':
                    fp.writelines('\n')
                fp.write(data)
        else:
            print('ファイルが指定されていません。保存を中断しました。')

    def saveJson(self, file=None, data="", mode='wt',encoding='utf-8'):
        if file is not None:
            with open(file,mode,encoding=encoding) as fp:
                fp.write(json.dumps(data))
        else:
            print('ファイルが指定されていません。保存を中断しました。')
    
    def create(self):
        cur = self.__cur()
        cur.close()
    
    def version(self):
        print(self.getVersion())

    def run(self):
        wnjpn_argv = self.getArgv()
        
        if len(wnjpn_argv) > 1:
            self.setCommand(wnjpn_argv[1])
        if len(wnjpn_argv) > 2:
            self.setOption(wnjpn_argv[2])
        
        command = self.getCommand()

        msg="""---------------------------------------------------------------------------------------------
    wordnet 検索
    日本語ワードネット （1.1版）
    © 2009-2011 NICT, 2012-2015 Francis Bond and 2016-2017 Francis Bond, Takayuki Kuribayashi
    URL: http://compling.hss.ntu.edu.sg/wnja/index.ja.html
---------------------------------------------------------------------------------------------"""
        print(msg)
        # logging
        self.logging(f"[処理]:メソッド:({sys._getframe().f_code.co_name}) / [内容]:コマンド呼び出し > {command}")
        
        if command == 'w' or command == 'search':
            # ワード検索
            self.word_search()
        elif command == 'c' or command == 'count':
            # 単語数一覧
            self.word_count()
        elif command == 'p' or command == 'export':
            # 関連単語書き出し。
            self.export()

        elif command == 'create':
            # 単語書き出し
            self.create()

        elif command == 'help':
            self.help()

        elif command == 'version':
            self.version()

class WordNetExtension(WordNet):
    def __init__(self):
        super().__init__()

    def getJson(self):
        with open(self.getJsonFile(),'rt') as fp:
            return json.load(fp)

    def searchWordPlus(self):
        
        word = input(">>")
        select_txt = f"""select word.wordid,word.lemma,sense.synset from word inner join sense
on word.wordid=sense.wordid
and word.lemma='{word}'
"""
        cur = self._cur()
        cur.execute(select_txt)
        rows = cur.fetchall()
        
        cur.close()
    
    def run(self):
        argv = self.getArgv()
        self.setCommand(argv[1])
        command = self.getCommand()
        self.logging(f"[処理]:メソッド:({sys._getframe().f_code.co_name}) / [内容]:コマンド呼び出し > {command}")
        if command == 'plus':
            self.searchWordPlus()
        
# -------------------------------------------------------
if __name__ == '__main__':
    WordNet().run()
    WordNetExtension().run()