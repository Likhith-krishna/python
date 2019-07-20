def median(ls):
    ls.sort()
    median =0
    length = len(ls)
    if(length % 2==0):
        median =((ls[length//2-1])+(ls[length//2]))/2
    else:
        median=(ls[length//2])
    return median
#print(median(list(input())))
ls1=list(map(int,input().strip().split()))
print(median(ls1))
