def getMinimumCost(arr):
    arr.sort()  # Sort the array
    n = len(arr)
    
    if n % 2 == 0:  # If the array length is even
        median = (arr[n // 2] + arr[n // 2 - 1]) / 2
    else:  # If the array length is odd
        median = arr[n // 2]
    
    median = round(median)  # Round the median to the nearest integer
    
    min_cost = 0
    
    for num in arr:
        min_cost += abs(num - median)
    
    return min_cost


# 512312
    arr=[5,1,2,3,1,2]
out = getMinimumCost(arr)
print(out)