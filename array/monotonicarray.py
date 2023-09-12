# Monotonic Array
# Array is Monotonic if it is either monotone increasing or monotone decreasing.
# Return true if and only if the given array nums is monotonic.
#

# Rephrase:
#   Given an array, check if it is monotonic
#   Monotonic means:
#       1. Monotone increasing
#       2. Monotone decreasing
#   Monotone increasing means:
#       1. The array is sorted in non-decreasing order
#   Monotone decreasing means:
#       1. The array is sorted in non-increasing order
#   If the array is monotone increasing or monotone decreasing, return True
#   Else, return False

# Edge Cases:
#   1. Empty array
#   2. Array with one element
#   4. Array with three elements
#   5. Array with similar elements

# Approach:
#  1. Check if the array is empty
#  2. Check if the array has one element
#  3. Create two pointers, i and j
#  4. i points to the first element
#  5. j points to the last element
#  6. Check if i is less than j
#  7. If i is less than j, return True
#  8. Check if j is less than i
#  9. If j is less than i, return True
# 10. Else, return False




# Example:
# [1,2,2,3]->[1,2,2,3]
# i=1
# j=3
# i<j
# return True
# Decrement j by 1
# Increment i by 1
# [1,2,2,3]->[1,2,2,3]
# i=2
# j=2
# i=j
# return True
# Decrement j by 1
# Increment i by 1


# Example:
# [1,3,2]->[1,2,3]
# i=1
# j=2
# i<j
# return True
# Decrement j by 1
# Increment i by 1
# [1,3,2]->[1,2,3]
# i=2


# Solution:
# Time Complexity: O(n)
# Space Complexity: O(1)
# def monotonicarray(nums):
#     if not nums:
#         return False
#     if len(nums)==1:
#         return True
#     i=0
#     j=len(nums)-1
#     while i<j:
#         if nums[i]<nums[j]:
            
#             return True
#         # Check for odd number of elements
#         if len(nums)%2!=0:
#             if i !=0 and j !=len(nums)-1:
#                if  nums[i-1]<nums[i] and nums[j]>nums[j+1]:
#                    return False
               
               
               
#         if nums[j]<nums[i]:
#             return True
#         i+=1
#         j-=1
#     return False


def monotonicarray(nums):
    if not nums:
        return False
    if len(nums)==1:
        return True
    i=1
    decreasing=increasing=True
    while i<len(nums):
        if nums[i-1]<nums[i]:
            decreasing=False
        
        if nums[i-1]>nums[i]:
            increasing = False
        i+=1
    return decreasing or increasing


# Solution 2 Using a for loop:

def monotonicarray(nums):
    if not nums:
        return False
    inc=dec=True
    for i in range(len(nums)-1):
        if nums[i]>nums[i+1]:
            inc=False
        if nums[i]<nums[i+1]:
            dec=False
    return inc or dec
# Example:
output=monotonicarray([1,2,2,3])
out2=monotonicarray([1,3,2])
# print(output)
print(out2)


