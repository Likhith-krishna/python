number=input()
if "." in number:
    val=float(number)
    print("Yes")
elif(number.isnumeric()==True):
    print("Yes")
else:
    print("No")
    
