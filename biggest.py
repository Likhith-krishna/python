inw=[]
n=int(input())
for x in range (0,n):
    b=int(input())
    inw.append(b)
    inw.sort()
    
print(inw[-1])
