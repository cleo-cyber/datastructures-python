class Solution(object):
    def arrayPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        # Array is Even
   
        # Rephrase:
        #  Given an even array group it n pairs. 
        # Find the min from each pair and add them.
        # Return the Maximum sum from the minimum pairs


        #Approach:
        # Sort the array
        


        # Example:
        # [1,4,3,2]->[1,2,3,4]
        nums.sort()
        # Iterate through the array with a picking even values
        # Add the even values to the sum
        # Return the sum
        # 
        maxSum=0
        for i in range(0,len(nums)-1,2):
            j=i+1
            maxSum+=min(nums[i],nums[j])
        return maxSum
  









            
