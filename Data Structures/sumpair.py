#program to print the pair having given sum in array
def arraysum(ls,n,sum):
    for i in range(0,n):
        for j in range(i+1,n):
            if(ls[i]+ls[j]==sum):
                print("(", ls[i],  
                      ", ", ls[j],  
                      ")")
                break
  
            
ls=list(map(int,input().split(',')))
sum=int(input())
n=len(ls)
print(arraysum(ls,n,sum))
