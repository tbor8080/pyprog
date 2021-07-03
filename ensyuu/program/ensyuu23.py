import random
counter=0
num=77
while True:
    counter+=1
    line=int(input("(整数の入力をしてください＞＞)"))
    if num==line:
        print("WIN!")
        break
    elif num>line:
        print("LOW")
    elif num<line:
        print("HIGH")
    elif counter==10:
        print("GAME OVER")
        break