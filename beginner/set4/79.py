import math
a,b=map(int,input().split())
c=a*b
d=math.sqrt(c)
if(d==a):
    print("yes")
else:
    print("no")
