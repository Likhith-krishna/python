i=int(input())
a=list(map(int,input().split()))
counter=0
num=""
for i in a:
    current=a.count(i)
    if(current>counter):
        counter=current
        num=i
print(num)
    
