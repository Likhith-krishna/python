inter=int(input())
diag=0
lis=[[int(i)for i in input().split()]for j in range(inter)]
for i in range(inter):
    diag=diag+lis[i][(inter-1)-i]
print(diag)
