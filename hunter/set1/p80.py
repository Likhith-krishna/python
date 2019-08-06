a=int(input())
k=list(map(int,input().split()))
d=10**10
for i in range(a-1):
    for j in range(i+1,a):
        if (k[i]-k[j])<d:
            z=(k[i]-k[j])
            if z<0:
                z=z*-1
            if z<d and z!=0:
                d=z
          
print(z)
