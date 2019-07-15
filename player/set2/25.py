st=int(input())
llst=list(map(str,input().split()))
a=sorted(llst,key=len)
for i in a:
    print(i,end=" ")
