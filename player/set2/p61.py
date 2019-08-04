c,d=map(int,input().split())
l=list(map(int,input().split()))
flag=0
for i in range(0,c):
    for j in range(i+1,c):
        if l[i]+l[j]==d:
            flag=flag+1
if(flag>=1):
    print("yes")
else:
    print("no")
