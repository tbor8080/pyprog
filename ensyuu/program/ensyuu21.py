buf=[50,40,124,-29,7,-128,128,87]
buf2=[]
min_num=buf[0]
min_num_2=min_num
print(f"元の配列：{buf}")
for i in range(0,len(buf)):
    for j in range(0,len(buf)):
        if buf[i]<buf[j]:
            buf[i],buf[j]=buf[j],buf[i]
print(f"整列後：{buf}")