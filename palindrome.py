n=int(input())
temporary=n
reverse=0
while(n>0):
    tens=n%10
    reverse=reverse*10+tens
    n=n//10
if(temporary==reverse):
    print("yes")
else:
    print("not")
    