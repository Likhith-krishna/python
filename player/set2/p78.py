c,d=map(int,input().split())
a=list(map(int,input().split()))
b=list(map(int,input().split()))

d=a+b
x=sorted(d)
for i in x:
    print(i,end=" ")
