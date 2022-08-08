class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        left=0
        right=len(nums)-1
        while left<=right:
            middle=(left+ right)//2
            if nums[middle]==target:
                return middle
            elif target<nums[middle]:
                right-=1
            else:
                left+=1
        return -1