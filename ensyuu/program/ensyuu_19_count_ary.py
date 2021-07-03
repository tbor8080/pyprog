ary=[3,7,1,6,1,1,1,1,1,1,5,1,1,1,99,1,1,88,1,1,1,1,1,2]
one_is_count=0
count=0
for i in range(0,len(ary)):
    if ary[i]==1:
        one_is_count+=1
        if one_is_count%3==0:
            count+=1
    if ary[i]==99:
        break

print(count)