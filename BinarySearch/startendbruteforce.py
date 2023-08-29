#  Find First and Last Position of Element in Sorted Array

# Brute force approach
nums = [5,7,7,8,8,8,8,10]
# nums=[5,7,7,8,8,10]
target = 8

def get_inds(nums,target):
    arr=[]
    l,r=0,1
    for num in nums:
        if nums[l]==nums[r] and nums[l]==target:
        
            arr.append(l)
            arr.append(r)
            
            if nums[r+1]==nums[r] and nums[r+1]==target:
                arr.append(r+1)
            return arr
        elif target not in nums:
            return [-1,-1]
        else:
            l+=1
            r+=1
    return [-1,-1]

cd=get_inds(nums,target)
print(cd)
        

