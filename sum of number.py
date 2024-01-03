num = int(input("Enter a number"))
sum = 0
temp = num
while temp > 0:
    rem = temp%10
    sum += rem 
    temp = temp//10
print("sum of digits",sum)
