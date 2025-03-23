class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        m = len(s)
        n = len(t)
        p1, p2 = 0, 0

        while p1 < m and p2 < n:
            if s[p1] == t[p2]:
                p1 += 1
            p2 += 1
        
        return p1 == len(s)
