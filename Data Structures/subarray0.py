#subarray with sum 0
def subarray(array,length):
    s=set()
    sum=0
    for i in range(0,length):
        sum+=array[i]
        if(sum==0 or sum in s ==0):
            return True
        s.add(sum)
    return False
array=list(map(int,input().split(',')))
length=len(array)
print(subarray(array,length))
