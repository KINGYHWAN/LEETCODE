class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        r = len(word1)+1
        c = len(word2)+1
        if word1 == word2:
            return 0
        if r == 1:
            return c-1
        if c == 1:
            return r-1
        dp = [[0]*c for _ in range(r)]
        for i in range(1, r):
            dp[i][0] = i
        for i in range(1, c):
            dp[0][i] = i
        for i in range(1,r):
            for j in range(1,c):
                if word1[i-1] == word2[j-1]:
                    dp[i][j] = dp[i-1][j-1]
                else:
                    dp[i][j] = 1 + min(dp[i-1][j-1], dp[i-1][j], dp[i][j-1])
        return dp[-1][-1]