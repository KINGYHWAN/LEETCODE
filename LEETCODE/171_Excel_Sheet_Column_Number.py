class Solution(object):
    def titleToNumber(self, columnTitle):
        """
        :type columnTitle: str
        :rtype: int
        """
        cnt = 0
        res = 0

        for i in range(len(columnTitle)-1, -1, -1):
            tmp = int(ord((columnTitle[i])) - ord('A')) + 1 # 1 ~ 26 숫자
            res += tmp * (26**cnt)
            cnt += 1

        return res

# a = Solution()
# columnTitle = 'ZY'
# res = a.titleToNumber(columnTitle)
# print(res)