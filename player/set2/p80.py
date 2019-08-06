a=int(input())
k=list(map(int,input().split()))
z=10**10
for i in range(a-1):
    for j in range(i+1,a):
        if abs(k[i]-k[j])<z:
            z=abs(k[i]-k[j])
print(z)
