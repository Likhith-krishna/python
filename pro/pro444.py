str1=input()
str2=input()
a1=[]
b1=[]
c1=[]
for i in str1:
    a1.append(ord(i)-ord('a1'))
for i in str2:
    b1.append(ord(i)-ord('a1'))
for i,j in zip(a1,b1):
    c1.append((chr((i+j)%26+ord('a1')+1)))
print("".join(c1))
