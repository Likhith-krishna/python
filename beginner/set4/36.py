import string
a=input()
count=0
for i in a:
    if i in set(string.punctuation):
        count=count+1
print(count)
        
