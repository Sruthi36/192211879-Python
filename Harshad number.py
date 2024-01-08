num = int(input("Enter a number "))
add = 0
temp = num
while temp>0:
    rem = temp%10
    add += rem
    temp = temp//10
if num%add == 0:
    print(num," is a Harshad number")
else:
    print(num," is not a Harshad number")
