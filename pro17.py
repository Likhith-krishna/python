from itertools import permutations
n,m=map(int,input().split())
d=list(map(int,input().split()))
for i in permutations(d,2):
    if(sum(i)==m):
        print("yes")
        break
else:
    print("no")
