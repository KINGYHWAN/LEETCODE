class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        
        res = ""
        i, j = 0, 0
        while word1 and word2:
            res += word1[i]
            res += word2[j]
            i += 1
            j += 1
            
            if (i > len(word1)-1) or (j > len(word2)-1):
                break
        
        if word1:
            res += word1[i:]
        
        if word2:
            res += word2[j:]

        return res

# a = Solution()
# word1 = "ab"
# word2 = "pqrs"
# res = a.mergeAlternately(word1, word2)
# print(res)