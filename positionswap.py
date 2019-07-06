stringg=list(input())
flag=0
while(flag<len(stringg)):
    flag=stringg[flag]
    stringg[flag]=stringg[flag+1]
    stringg[flag+1]=flag
    flag+=2
print("".join(stringg))
