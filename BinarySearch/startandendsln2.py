class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if len(nums)<=0:
            return [-1,-1]
        elif target not in nums:
            return [-1,-1]
        
        def locate_targ(nums,target,Lbias):
            l,r=0,len(nums)-1
            i=-1
            while l<=r:
                mid=(l+r)//2
                if target> nums[mid]:
                    l=mid+1
                elif target<nums[mid]:
                    r=mid-1
                else:
                    i=mid
                    if Lbias:
                        r=mid-1
                    else:
                        l=mid+1
            return i
        left=locate_targ(nums,target,True)
        right=locate_targ(nums,target,False)
        return [left,right]

    # Timecomplexity:O(logn)
    # Spacecomplexity:O(1)