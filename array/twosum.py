class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        hashmap={} #dictionary
        for i,n in enumerate(nums):
            difference=target-n
            
            if difference in hashmap:
                return [hashmap[difference],i] #get the index of the values
            hashmap[n]=i #update the index if the value is not found
                