# class Solution(object):
#     '''
#     Works but it is not optimised for larger inputs
#     '''
#     def vowelStrings(self,words,queries):
#         if words is None:
#             return
#         vowels=['a','e','i','o','u']
#         ans=[]
#         for i in range(len(queries)):
#             l=queries[i][0]
#             r=queries[i][1]
#             print(r)
#             words_array=words[l:r+1]
#             count=0

#             for j in range(len(words_array)):

#                 left=words_array[j][0]
#                 right=len(words_array[j])-1
#                 right_v=words_array[j][right]

#                 if left in vowels and right_v in vowels:
#                     count+=1
#             ans.append(count)
                
#         return ans
            
            

class Solution(object):
    """
    Not optimised for larger inputs
    """
    def vowelStrings(self,words,queries):
        ans=[]
        vowels={'a','e','i','o','u'}

        for l,r in queries:
            count=0
            for i in range(l,r+1):
                if words[i][0] in vowels and words[i][-1] in vowels:
                    count+=1
            ans.append(count)
        return ans
words=["aba","bcb","ece","aa","e"]
queries=[[0,2],[1,4],[1,1]]

vstr=Solution()

res=vstr.vowelStrings(words,queries)
print(res)



# Optimised solution
class Solution(object):
    def vowelStrings(self, words, queries):
        if words is None or not queries:
            return []
        
        vowels = {'a', 'e', 'i', 'o', 'u'}  # Use a set for faster lookups
        n = len(words)
        
        # Step 1: Precompute whether each word is a vowel string
        is_vowel_string = [
            word[0] in vowels and word[-1] in vowels
            for word in words
        ]
        
        # Step 2: Precompute prefix sum of vowel-valid words
        prefix_sum = [0] * (n + 1)
        for i in range(n):
            prefix_sum[i + 1] = prefix_sum[i] + (1 if is_vowel_string[i] else 0)
        
        # Step 3: Process each query
        ans = []
        for l, r in queries:
            ans.append(prefix_sum[r + 1] - prefix_sum[l])
        
        return ans

