class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if target not in nums:
            return -1
        if len(nums)<=0:
            return -1
        # Brute force
        # Iterate through the array
        # Check if target in array
        # Return index else return -1

        l,r=0,len(nums)-1
        while l<=r:
            if nums[l]==target:
                return l
            l+=1
    
# Timecomplexity:O(n)
# Spacecomplexity:O(1)