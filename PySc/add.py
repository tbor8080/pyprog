
def InputSchedule():
    msg = """##########
    スケージュール追加を行います。
    下記項目を入力後、Enterを押してください。
##########"""
    print(msg)

    title = input("スケジュールを教えてください。>>")
    subtitle = input("省略可:Press Enter >>")
    # 日付:取得
    sch_date = input("日付を入力してください。> [2022.05.04]>>")
    # くり返し項目なのか？
    # repeat_sch = input("繰り返しますか？[Y/n] >>") 


def main():
    InputSchedule()
    pass

if __name__ == "__main__":
    main()
