c=int(input())
for i in range(1,c+1):
    k=c//i
    if (k%2==1 and c%i==0):
        print(i)
        break
