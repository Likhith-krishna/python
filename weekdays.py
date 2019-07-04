def week(day):
    weekdays=["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday"]
    if(day=="Sunday"):
        return ("Yes")
    elif day in weekdays:
        return ("No")
    else:
        return ("Invalid")
day=str(input())
print(week(day))