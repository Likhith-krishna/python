inpu=int(input())
for x in range(2,inpu+1):
    if(inpu%x==0):
        flag =1
        for y in range(2,(x//2+1)):
            if(x%y==0):
                flag=0
                break
        if(flag==1):
            print(x,end=" ")
            
        
