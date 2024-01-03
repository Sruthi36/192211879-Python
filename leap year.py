date = input("Enter date").split("/")
converted_date = list(map(int,date))
year = converted_date[2]
if (year%4 == 0):
    if (year%100 == 0):
        if (year%400 == 0):
            print(str(year) + " is a leap year")
        else:
            print(str(year) + " is not a leap year")
    else:
        print(str(year) + " is a leap year")
else:
    print(str(year) + " is not a leap year")

x = year % 4
if (x != 0):
    print("Previous leap year " + str(year-x))
else:
    print("Next leap year " + str(year + 4))
