nume=int(input())
value=list(map(int,input().split()))
flags=[]
for  i in value:
    if value.count(i)==1:
        if i not in flags:
            flags.append(i)
for p in flags:
    print(p,end=" ")
        
