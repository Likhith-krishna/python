inter=int(input())
intro=list(map(int,input().split()))
te=max(intro)
c1,d1=0,0
for i in range(0,len(intro)-1):
    for j in range(1,len(intro)):
        if abs(intro[i]+intro[j])<te:
            c1,d1=intro[i],intro[j]
            te=abs(c1+d1)
print(c1,d1)

