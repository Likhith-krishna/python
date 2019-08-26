inter=int(input())
for num in range(2,inter):
    for i in range(2,num):
        if num%i==0:
            break
    else:
        print(num,end=" ")
