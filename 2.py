n = int(input())
k = int(input())
l = []
while(n>0):
    l.append(n%10)
    n = n//10
a = -1
b = -2
while(k):
    if(l[a]>l[b]):
        del[l[-1]]
        k = k-1
    else:
        a = a-1
        b = b-1
    if( a == -1*len(l)):
        break
while(k):
    maxi_i = 0
    maxi = l[0]
    for i in range(len(l)):
        if(l[i]>maxi):
            maxi = l[i]
            maxi_i = i
    del(l[maxi_i])
    k = k-1
n = 0
for i in range(len(l)-1,-1,-1):
    n = n*10 + l[i]
print(n)
