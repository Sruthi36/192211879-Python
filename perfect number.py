num = int(input())
sum = 0
for i in range(1,num):
    if (num % i == 0):
        sum += i
if (sum == num):
    print(str(num) + " is a perfect number")
else:
    print(str(num) + " is not a perfect number")
