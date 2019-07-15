st=int(input())
llst=list(map(str,input().split()))
llst.sort()
llst.sort(key=len)
for i in llst:
    print(i,end=" ")
