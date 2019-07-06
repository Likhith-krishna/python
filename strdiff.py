def strdifference(a,b):
    count=0
    if(len(a)==len(b)):
        for i in range(0,len(a)):
            if(a[i]==b[i]):
                continue
            else:
                count=count+1
        if(count==1):
            return ("yes")
        else:
            return ("no")
a,b=map(str,input().split())
print(strdifference(a,b))
