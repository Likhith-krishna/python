inter=int(input())
count=0
for i in range(2,inter):
    if (inter%i==0):
        count=count+1
if count>=1:
    print("yes")
else:
    print("no")
