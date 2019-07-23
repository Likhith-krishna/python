def check_pow(N, k):
    if k < 0 or N < 0:
        return ("no")
    if k == 0 and N == 1:
        return ("yes")
    if k in (0, 1) and N != 1:
        return ("no")

    num = k
    while num < N:
        num *= k
    return num == N
num,po=map(int,input().split())
print(check_pow(num,po))
