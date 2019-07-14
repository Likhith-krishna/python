inter=list(input())
finale=[]
letters=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
for i in inter:
    if i=='X':
        finale.append("A")
    elif i=='Y':
        finale.append("B")
    elif i=="Z":
        finale.append("C")
    else:
        finale.append(letters[letters.index(i)+3])
print("".join(finale))
