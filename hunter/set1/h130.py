inetr=int(input())
count=0
lis=[]
a=0
for i in range(2,inetr):
    s=0
    for j in range(2,i):
        if(j%i==0):
            s=1
    if(s==0):
        lis.append(i)
for i in range(0,len(lis)):
    if(lis[i]==3 or lis[i]%10==3):
        a=a+lis[i]
print(a)
    
