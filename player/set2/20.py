stri=str(input())
arr="0ABCDEFGHIJKLMNOPQRSTUVWXYZ"
naya=""
for x in stri:
    if x in arr:
        temp=arr.index(x)
        temp=temp+3
        naya=naya+arr[temp]
print(naya)
