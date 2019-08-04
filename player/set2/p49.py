inter=int(input())
if inter>=-2**15+1 and inter<=2**15+1:
    print("INT")
elif inter>=-2**31+1 and inter<=2**31+1:
    print("LONG")
else:
    print("LONG LONG")
