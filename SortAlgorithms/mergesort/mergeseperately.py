class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        # CHECK LEN
    # IF LEN EQUALS iterate both using one
        # merged=""
        # if len(word1)>len(word2):
        #     for i in range(len(word2)):
        #         merged+=str(word1[i])+str(word2[i])
        #     merged+=word1[len(word2):]
        #     return merged
        # if len(word1)<len(word2):
        #     for i in range(len(word1)):
        #         merged+=str(word1[i])+str(word2[i])
        #     merged+=word2[len(word1):]
        #     return merged
        # if len(word1)==len(word2):
        #     for i in range(len(word1)):
        #         merged+=str(word1[i])+str(word2[i])
        #     return merged

        merged=""
        for i in range(min(len(word1),len(word2))):
            merged+=word1[i] +word2[i]

        if len(word1)>len(word2):
            merged+=word1[len(word2):]
        if len(word2)>len(word1):
            merged+=word2[len(word1):]
        return merged
