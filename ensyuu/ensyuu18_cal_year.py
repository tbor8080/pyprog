import sys
month=[31,28,31,30,31,30,31,31,30,31,30,31]
line_month=int(input("月：＞＞"))
line_day=int(input("日：＞＞"))
one_year=0
if line_month == 0:
    print("終了します")
    sys.exit()
for m in range(0,line_month):
    if line_month-1 == m and line_day < month[m]:
        one_year+=line_day
    else:
        one_year+=month[m]

print(one_year)