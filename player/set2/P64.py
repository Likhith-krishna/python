a,b=map(int,input().split())
k=list(map(int,input().split()))
li=[]
for i in range(0,a):
    if k[i] < b:
        li.append(k[i])
li.sort()
print(*li)
        
