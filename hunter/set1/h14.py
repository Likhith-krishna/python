from itertools import permutations
def permu(stre):
    aList=permutations(stre)
    for i in list(aList):
        print(''.join(i))
if __name__ == "__main__": 
    stre = input()
    permu(stre) 
