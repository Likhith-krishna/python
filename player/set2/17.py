def greaterdiv(x, y):
    if x > y:
        smaller = y
    else:
        smaller = x
    for i in range(1, smaller+1):
        if((x % i == 0) and (y % i == 0)):
            greater = i
            
    return greater
def lcm(x,y):
    return int((x*y) / greaterdiv(x,y))

numbe1,numbe2=map(int,(input().split()))
print(lcm(numbe1, numbe2))
