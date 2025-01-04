# Given an array of integers, the goal is to make all the elements in the array to have equal valuees by applying some number operations.
# The rules of operation are:
# 1. To apply an operation, one needs to choose a prefix of the array and an integer x(x can be negative)
# 2. In this operation, add x to each element inside this prefix.
# 3. The cost of this operation is |x| (absolute value of x)

# For example, if the array is [1,4,2,1] and the prefix of the length 2 and x=-3 are chosen, the array would now become [-2,1,2,1] and the cost of this operation would be |x|=|-3|=3

# The total cost is the sum of costs of each operation applied. Find the minimum total cost of making all the elements in the array have equal value.
# Note: It is guaranteed that there always exists a series of operations by which all the elements in an array can b equal.
# These operations can be applied any number of times

# Example   
# Consider n=4 and arr=[1,2,1,5]
# The array can be made equal by applying the following operations:
# 1. Choose the prefix of length 2 and x=1 Hence the array now becomes[0,1,1,5] The cost of this opeation is |1|=1
# 2. Choose the prefix of length 3 and x=4. Hence the array now becomes [4,5,5,5] The cost of this operation is |4|=4
# 3. Choose the prefix of length 1 and x=1. Hence the array now becomes [5,5,5,5] The cost of this operation is |1|=1

# The total cost is 1+4+1=6 which is the minimum possible cost

# Function Description
# Complete the function getMinimumCost below
# getMinimumCost has the following parameter(s):
# int arr[arr[0]...arr[n-1]] : an array of integers
# Returns
# int: an integer denoting the minimum cost to make the array equal
# Constraints
# 1<=n<=2.10^5
# 1<=arr;<=10^4

# Solution
def getMinimumCost(arr):
    n = len(arr)
    arr.sort()
    median = arr[n//2]
    cost = 0
    for i in range(n):
        cost += abs(arr[i]-median)
    return cost