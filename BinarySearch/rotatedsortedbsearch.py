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
        # # Brute force
        # # Check if array is empty
        # # Check if array is rotated
        # # Iterate through the array
        # # Check if target in array
        # # Return index else return -1

        l,r=0,len(nums)-1
        # while l<=r:
        #     if nums[l]==target:
        #         return l
        #     l+=1

        # Binary Search
        # Create Right and left pointer
        # Compute mid
        # Check if mid is equal to target=return mid else
        # Chcke porrtion of the list we are in
        # Check if value[mid] is greater than left/right
        # If greater than mid, Seearch Left,Check if leftmost value is greater than target target if yes search right else search left

        while l<=r:
            mid=(l+r)//2
            if nums[mid]==target:
                return mid
            if nums[mid]>=nums[l]:
                if target<nums[l] or target >nums[mid]:
                    l=mid+1
                else:
                    r=mid-1
            elif nums[mid]<=nums[l]:
                if target>nums[r] or target < nums[mid]:
                    r=mid-1
                else:
                    l=mid+1
        return -1
                



