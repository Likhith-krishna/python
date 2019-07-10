number=int(input())
values=list(map(int,input().split()))
flag=[]
for  i in values:
    if values.count(i)==1:
        if i not in flag:
            flag.append(i)
for z in flag:
    print(z,end=" ")
        
