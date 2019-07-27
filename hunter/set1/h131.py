inte=int(input())
a=list(map(int,input().split()))
d=sorted(a)
k=d[::-1]
p=[]
for i in range(0,len(a)):
    p.append(k[i])
    p.append(d[i])
for j in p[:len(a)]:
    print(j,end=" ")
