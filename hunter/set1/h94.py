def revers(stre):
    return " ".join(x[::-1] for x in stre.split(" "))
stre=str(input())
print(revers(stre))
