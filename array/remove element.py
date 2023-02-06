class Solution(object):
    def __init__(self,nums,val) -> None:
        k=0

        for num in nums:
            if nums[num] !=val:
                nums[k]=nums[num]
                k+=1
            return k