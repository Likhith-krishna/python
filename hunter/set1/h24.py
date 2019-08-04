v,n=map(int,input().split())
k=[int(x) for x in input().split()]
flag=0
for i in range(0,v):
    for j in range(i+1,v):
        b=int(k[i]+k[j])
        if(b==n):
            flag=flag+1
if(flag==1):
    print("YES")
else:
    print("NO")
        
