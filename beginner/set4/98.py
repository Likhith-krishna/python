aw=int(input())
dd=list(map(int,input().split()))
for i in range(aw-1):
    if(dd[i]>dd[i+1]):
        print(i)
        break

