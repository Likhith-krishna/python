a=input()
b=input()
li=[]
new=[]
for i in range(0,len(a)):
    if a[i] in b:
        li.append(a[i])
for num in li:
    if num not in new:
        new.append(num)
for i in new:
    print(i,end="")
        
