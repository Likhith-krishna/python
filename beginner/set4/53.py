inta=int(input())
sum=0
while(inta!=0):
    sum=sum+inta%10
    inta//=10
print(sum)
