def factorial(n):
    if(n<=20):
        if(n>0):
            n= n*factorial(n-1)
            return n
        else:
            return 1
    else:
        return ("give value less tahn 20")
number=int(input())
print(factorial(number))
