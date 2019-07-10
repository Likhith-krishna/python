stre=input()
vowels=('a','e','i','o','u')
for x in stre:
    if x in vowels:
        stre=stre.replace(x,"")
print(stre[::-1])
