
# solution 1

class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l,r=0,len(nums)-1
        res=nums[0]
        while l<=r:
            if nums[l]<nums[r]:
                res=min(res,nums[l])
                break
            median=(l+r)//2
            res=min(res,nums[median])
            if nums[median]>=nums[l]:
                l=median+1
            else:
                r=median-1
        return res

        # Solution2
        nums.sort()
        return min(nums)