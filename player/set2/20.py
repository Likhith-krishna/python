inter=list(input())
finale=[]
letters=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
for i in inter:
    if i=='X':
        final.append("A")
    elif i=='Y':
        final.append("B")
    elif i=="Z":
        final.append("C")
    else:
        final.append(letters[letters.index(i)+3])
print("".join(finale))
