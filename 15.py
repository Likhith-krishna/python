stre=input()
count=0
for i in stre:
    if stre.count(i)>count:
        count=stre.count(i)
        final=i
print(final)
