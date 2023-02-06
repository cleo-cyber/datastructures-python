class Solution(object):
    def __init__(self,nums) -> None:
        
        k=1

        for i in range(1,len(nums)):
            if nums[i]==nums[i-1]:
                continue
            else:
                nums[k]=nums[i]
                k+=1
            return k


# Use pointer 
# get the index of the next element 
# check if next ==previous if true skip second
# else swap next with previous
# return number of swaps