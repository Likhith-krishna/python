n=int(input())
a=list(map(int,input().split()))
result=1
for i in range(0,n):
    result=result*a[i]
print(result)
