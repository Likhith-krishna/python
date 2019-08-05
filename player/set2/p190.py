x,y,z=map(int,input().split())
x=x*x
y=y*y
z=z*z
k=x+y
if(k==z):
    print("no")
elif((x==y) and (y==z)):
    print("no")
else:
    print("yes")
