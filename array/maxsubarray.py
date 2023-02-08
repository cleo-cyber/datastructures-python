class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        currSum=0
        maxSub=nums[0]

        for i in nums:
            if currSum<0:
                currSum=0
            currSum=currSum+i
            maxSub=max(currSum,maxSub)
        return maxSub