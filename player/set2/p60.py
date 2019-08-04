m,n=map(str,input().split())
flag=0
for i in m:
    for j in n:
        if i==j:
            flag=flag+1
if(flag>=1):
    print("yes")
else:
    print("no")
