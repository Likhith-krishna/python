input1,input2=map(int,input().split())
count=0
for number in range(input1+1,input2):
    if(number > 1):
        for x in range(2,number):
            if((number%x)==0):
                break
        else:
            count=count+1

print(count)
