

# Given a 1-indexed array of integers numbers that is already sorted in non-decreasing order, find two numbers such that they add up to a specific target number. Let these two numbers be numbers[index1] and numbers[index2] where 1 <= index1 < index2 <= numbers.length.

# Return the indices of the two numbers, index1 and index2, added by one as an integer array [index1, index2] of length 2.

# The tests are generated such that there is exactly one solution. You may not use the same element twice.

# Your solution must use only constant extra space.


class Solution(object):
    def (self, numbers, target):
        l, r = 0, len(numbers)-1

        while l < r:
            currSum = numbers[l]+numbers[r]
            if currSum > target:
                r -= 1
            elif currSum < target:
                l += 1
            else:
            return [l+1, r+1]


# Input: numbers = [2,7,11,15], target = 9
# Output: [1,2]
# Explanation: The sum of 2 and 7 is 9. Therefore, index1 = 1, index2 = 2. We return [1, 2].
