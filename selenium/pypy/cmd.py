try:
    from selenium.webdriver import Chrome, ChromeOptions
    from selenium.webdriver.common.keys import Keys
except ModuleNotError as e:
    print('Module Not Found, Please Install > "pip install selenium" .')

class WebAppHeadlessCmd:

    AppName='Web Application (Auto|AI) Test Command by Selenium'
    Description="""
    - First Program

    app=WebAppHeadlessCmd(option=['--headless','',''])
    app.command('Dos')

    app.close()
    - or -
    app.quit()

    """

    def __init__(self, option=['--headless']):
        self.options = ChromeOptions()
        if len(option)>0:
            for o in range(0, len(option)):
                self.options.add_argument(option[o])
        self.driver = Chrome(options=self.options)
    
    def close(self):
        self.driver.close()
    def quit(self):
        self.driver.quit()

    def get(self,url):
        self.driver.get(url)
    
    def setUrl(self,url):
        self.url=url
    def getUrl(self):
        return self.url
    
    def DDos(self):
        # 対象のウェブサイトやサーバーに対して複数のコンピューターから大量に行うこと
        pass

    def Dos(self, num=10):
        # 大量のデータや不正なデータを送り付けること
        self.get(self.getUrl())
        count=0
        while True:
            count+=1
            if count<num:
                self.driver.find_element_by_tag_name('html').send_keys(Keys.F5)
    
    def SqlInjection(self):
        Injection=[
            """
            SELECT * FROM users WHERE name = 't' OR 't' = 't';
            """
            ,
            """
            SELECT * FROM users WHERE name = '\'' OR 1=1 --';
            """
        ]
        pass
    
    def Xss(self):
        # 攻撃対象のWebサイトの脆弱性を突き、攻撃者がそこに悪質なサイトへ誘導するスクリプトを仕掛けることで、
        # サイトに訪れるユーザーの個人情報などを詐取する攻撃のことを指します。
        XssScript=[
            """
            <script>
                for(var i=0;i<10000;i++)
                {
                    alert(1);
                }
            </script>
            """
        ]
        pass

    def DirectoryTraversal(self):
        # ファイル名を扱うようなプログラムに対して特殊な文字列を送信することにより、
        # 通常はアクセスできないファイルやディレクトリ（フォルダ）の内容を取得する手法。
        Dt=
        pass

    # 耐久系
    def AutoInsert(self):
        
        pass

    def AutoSelect(self):
        pass

    def AutoUpdate(self):
        pass

    def AutoDelete(self):
        pass



# Test:=
url='http://localhost/'
w=WebAppHeadlessCmd()
w.setUrl(url)
w.Dos()
