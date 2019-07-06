number=int(input())
prefix=input()
for i in range(number-1):
    string=input()
    small=len(string)
    if(len(prefix)<len(string)):
        small=len(prefix)
    for j in range(small):
        if(prefix[j]!=string[j]):
            prefix=prefix[:j]
            break
print(prefix)
