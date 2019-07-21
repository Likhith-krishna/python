inter=int(input())
intro=list(map(int,input().split()))
count=0
b=[]
for i in intro:
    if(intro.count(i)>1 and i not in b):
        b.append(i)
        b.sort()
        
if(len(b)==0):
    print("unique")
for j in b:
    print(j,end=" ")
