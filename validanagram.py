class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        s_length=len(s)
        t_length=len(t)
        
        
        if s_length!=t_length:
            return False
        if sorted(s)==sorted(t):
            return True
        else:
            return False