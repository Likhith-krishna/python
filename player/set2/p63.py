k=int(input())
l=list(map(int,input().split()))
m=list(map(int,input().split()))
d=[]
for i in l:
    if i in m:
        d.append(i)
d.sort()
print(*d)

    
