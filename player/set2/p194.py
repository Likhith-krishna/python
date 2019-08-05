a,b=input().split()
if((a=="R" and b=="P")or (a=="P" and b=="R")):
    print("P")
elif((a=="S" and b=="P") or (a=="P" and b=="S")):
    print("S")
elif((a=="R" and b=="S")or (a=="S" and b=="R")):
    print("R")
else:
    print("D")
