# Bubble Sort
buf=[50,44,124,-29,-7,0,-128,87]
for i in range(0,len(buf)):
    for j in range(0,i):
        if(buf[i]>buf[j]):
            buf[i],buf[j]=buf[j],buf[i]
            continue
print(buf)