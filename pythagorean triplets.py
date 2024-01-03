limit = int(input("Enter limit "))
c,m = 0,2
while c < limit:
    for i in range(1,m):
        a = m * m - i * i
        b = 2 * m * i
        c = m * m + i * i
        if c > limit:
            break
        if (a ==0 or b==0 or c==0):
            break
        print(a,b,c)
    m = m+1
