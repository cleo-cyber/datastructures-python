class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """

        # Iterate through the array checking the nums==k
        # if nums ==k get the index
        # subtract the indexes and check if the solution is less than 
        # or equal to k
        hashmap={}

        for i,n in enumerate(nums):
            if n in hashmap:
                diff=i-hashmap[n]
                if diff<=k:
                    return True
            hashmap[n]=i
        return False

# Time complexity - O(n)
# Optimal solution