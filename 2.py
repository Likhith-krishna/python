inter=input()
l=list(map(int,input().split()))
a=sorted(l,reverse=True)
for i in a:
    print(i,end="")
