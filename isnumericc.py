def verify(user):
    if (user.isnumeric() == True):
        return ("yes")
    else:
        return ("no")
user=input()
print(verify(user))
