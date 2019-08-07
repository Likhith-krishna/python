import string
def ispangram(stre):
    alpa="abcdefghijklmnopqrstuvwxyz"
    for x in alpa:
        if x not in stre.lower():
            return False
    return True
stre=input()
if(ispangram(stre)==True):
    print("yes")
else:
    print("no")
