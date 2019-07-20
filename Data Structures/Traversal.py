#sort a binary array with one traversal
def tracv(array,length):
    j=-1
    for i in range(0,length):
        if(array[i]<1):
            j=j+1
            array[i],array[j]=array[j],array[i]
array=list(map(int,input().split(',')))
length=len(array)
tracv(array,length)
for i in range(length):
    print(array[i],end=" ")
