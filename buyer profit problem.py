def maxprofit(price,size):
    profit = [0] * size
    
    max_price = price[size-1]
    for i in range(size-2,0,-1):
        if price[i] > max_price:
            max_price = price[i]
        profit[i] = max(profit[i+1], max_price - price[i])

    min_price = price[0]
    for i in range(1,size):
        if price[i] < min_price:
            min_price = price[i]
        profit[i] = max(profit[i-1], profit[i]+(price[i]-min_price))
    result = profit[size-1]
    return result

def convertintoint(array):
    arr = []
    for i in array:
        i = int(i)
        arr.append(i)
    return arr

array = input().split(" ")
arr = convertintoint(array)
size = len(arr)
print("Max profit is:" , maxprofit(arr,size))
