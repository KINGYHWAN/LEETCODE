# 4
# solution 1
class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """

        if not strs:
            return ""

        new = ""
        strs = sorted(strs)
        first, last = strs[0], strs[-1]
        for i in range(len(first)):
            if i < len(last) and first[i] == last[i]:
                new += first[i]
            else:
                break
        
        return new

# solution 2

class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        prefix = ""
        track = False

        for i in range(len(min(strs, key = len))):
            for j in range(1, len(strs)):
                if strs[0][i] == strs[j][i]:
                    continue
                else:
                    track = True
                    break

            if track == False:
                prefix += strs[0][i]
            
            if bool(track):
                break

        return prefix 





