nm,nn=map(int,input().split())
pp=list(map(int,input().split()))
for i in range(0,nn):
    pp=(pp[-1:]+pp[:-1])
for x in pp:
    print(x,end=" ")
