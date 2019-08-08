inter=input()
sum=0
for i in inter:
    sum=sum+int(i)
k=str(sum)[::-1]
if(sum==int(k)):
    print("YES")
else:
    print("NO")
