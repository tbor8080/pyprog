ary=[1,90,50,2000,800]
num_max=0
for i in range(0,len(ary)):
    if ary[i]==0:
        break
    if ary[i]>0 and num_max<ary[i]:
        num_max=ary[i]
print(num_max)