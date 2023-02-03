class ThreeSum():
    def threesum(self,nums):
        results=[]
        nums.sort()

        for i,n in enumerate(nums):
            if i>0 and n=nums[i-1]:
                continue
            l,r=i+1,len(nums)-1

            while l<r:
                currSum=n+nums[l]+nums[r]

                if currSum>0:
                    r-=1
                elif currSum<0:
                    l+=1

                else:
                    results.append(n,nums[l],nums[r])
                    l+=1
                    while nums[l]==nums[l+1] and l<r:
                        l+=1