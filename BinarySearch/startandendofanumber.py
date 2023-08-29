

def get_first(nums,target):
   l,r=0,len(nums)-1
   while l<=r:
        mid=(l+r)//2
        if nums[mid]==target:
             if nums[mid-1]==target and mid>0:
                r=mid-1
             else:
                return mid
        elif target>nums[mid]:
             l=mid+1
        elif target<nums[mid]:
             r=mid-1
        else:
             return -1
def get_last(nums,target):
    l,r=0,len(nums)-1
    while l<=r:
        mid=(l+r)//2
        if nums[mid]==target:
            if nums[mid+1]!=target and nums[mid-1]!=target and mid>0 and mid<len(nums)-1:
                return mid
            elif nums[mid+1]==target and mid<len(nums)-1:
                l=mid+1
            else:
                return mid
        elif target>nums[mid]:
            l=mid+1
        elif target<nums[mid]:
            r=mid-1
        else:
            return -1
def get_num(nums,target):
   if len(nums)<0:
       return [-1,-1]
   if target not in nums:
         return [-1,-1]
   
   
   left=get_first(nums,target)
   right=get_last(nums,target)
   return[left,right]

nums = [5,7,7,8,8,8,8,10]
target = 10
out=get_num(nums,target)
print(out)


