class Solution(object):
    def reverseString(self, s):
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """

        # Solution 1
        l=0
        r=len(s)-1
        
        while l<r:
            s[l],s[r]=s[r],s[l]
            
            l+=1
            r-=1
            
        # Solution 2

        stack=[]

        for i in s:
            s.append(i)

        index=0
        while stack:
            s[index]=s.pop()
            index+=1