inpu=int(input())
suma=0
temp=inpu
while temp>0:
    digits=temp%10
    cube=digits*digits*digits
    suma=suma+cube
    temp//=10
if(inpu==suma):
    print("yes")
else:
    print("no")
    
