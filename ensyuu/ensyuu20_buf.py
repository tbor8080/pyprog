buf=[5,9,-3,11,94,32,105,54,3,11]
ans=[]
for i in range(0,len(buf)):
    count=0
    if buf[i]<100 and buf[i]>=0:
        for j in range(0,len(buf)):
            if buf[i]>buf[j]:
                count+=1
    ans.append(count)
print(buf,ans)

