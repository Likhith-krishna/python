k=int(input())
l=list(map(int,input().split()))
l.sort(reverse = True)
for i in l:
    print(i,end="->")
