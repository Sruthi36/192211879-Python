def happynum(num):
    sum = 0
    temp = num
    while (temp>0):
        rem = temp%10
        sum += (rem%10) ** 2
        temp = temp //10
    return sum


num = int(input("Enter a number"))
result = num
while result!=1 and result != 4:
    result = happynum(result)
