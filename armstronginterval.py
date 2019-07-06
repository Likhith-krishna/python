inpu1,inpu2=map(int,input().split())
for inpu in range(inpu1,inpu2):
    suma=0
    temp=inpu
    while temp>0:
        digits=temp%10
        cube=digits*digits*digits
        suma=suma+cube
        temp//=10
    if(inpu==suma):
        print(inpu,end=" ")

    
