a,b=map(int,input().split())
c=list(input().split())
d=list(input().split())
for i in range (len(c)):
    for j in range (len(d)):
        if(c[i]==d[j]):
            print(c[i],end=" ")
