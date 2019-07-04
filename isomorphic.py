def stre(a,b):
    if(len(a)==len(b)):
        return ("Yes")
    else:
        return ("No")
a,b=map(str,input().split())
print(stre(a,b))