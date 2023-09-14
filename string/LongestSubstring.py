# Longest non repeating substring

def longestSubstring(s):
    
    # Approach 1: 
    # Create a set to store the characters in the string
    # Create two variables, start and maxSubstr
    # Iterate through the string
    # If the character is not in the set, add it to the set
    # Else, remove the character from the set and increment start by 1
    # MaxSubstr is the maximum of maxSubstr and the length of the set
    # Return maxSubstr
    # Time Complexity: O(n)
    # Space Complexity: O(n)
    myset=set()
    start=0
    maxSubstr=0
    for i in range(len(s)):
        if s[i] not in myset:
            myset.add(s[i])
        else:
            while s[i] in myset:
                myset.remove(s[start])
                start+=1
            myset.add(s[i])
        maxSubstr=max(maxSubstr,len(myset))
    return maxSubstr