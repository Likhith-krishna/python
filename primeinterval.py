input1=int(input())
input2=int(input())
for number in range(input1,input2+1):
    if(number > 1):
        for x in range(2,number):
            if((number%x)==0):
                break
        else:
            print(number)
