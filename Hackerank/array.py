# For each element of an array, a counter is set to 0.
# The element is compared to each element to its left
# If the element to the left is less, the absolute difference is added to the counter.
# For each element of the array, determine the value of the counter. These values should be stored in an array and returned

# Example
# n= 3 the number of elements
# arr = [2,4, 3]

# For arr[0]=2, there are no elements to the left. The counter is 0
# For arr[1]=4, arr[0]=2. The counter is 2-4=2 
# Testing arr[2]=3 first against 4, counter =0 - [3-4]=-1 and then against 2 counter=-1+[3-2]=0
# The result is [0,2,0] 

# Function Description
# Complete the function arrayChallenge below
# arrayChallenge has the following parameter(s):
# int arr[n]: an array of integers
# Returns 
# int[n]: an array of integers calculated as described  

# Solution
def arrayChallenge(arr):
    result = []
    for i in range(len(arr)):
        counter = 0
        for j in range(i):
            counter += abs(arr[i]-arr[j])
        result.append(counter)
    return result