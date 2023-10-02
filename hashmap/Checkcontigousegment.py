class Solution(object):
    def checkOnesSegment(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # Contagous/adjacent 
        # Two pointers fast forward.
        
        # Check if s[0] is 0 return false else continue

        if s[0]=='0':
            return False
        # if len(s)==1 and s[0]=='1':
        #     return True
        # if s.count('1')==1:
        #     return True
        # for i in range(len(s)-1):
        #     j=i+1

        #     if s[i] == s[j] and s[i]=='1':
        #         return True
        # return False

        for i in range(s.count('1')):
            if s[i]!='1':
                return False
        return True