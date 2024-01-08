a = int(input("Enter lower limit"))
b = int(input("Enter upper limit"))
for i in range(a,b+1):
    temp = i
    sum = 0
    while temp>0:
        rem = temp %10
        sum += rem
        temp = temp // 10
    if i % sum == 0:
        print(i)
    else:
        continue
