ar=int(input())
lis=[]
while ar>0:
    k=ar%10
    lis.append(k)
    ar=ar//10
addi=lis[0]+lis[-1]
print(addi)
