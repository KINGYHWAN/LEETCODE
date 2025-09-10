class Solution:
    def reverseWords(self, s: str) -> str:
        # res = ""
        # list_s = s.split()
        # for i in range(len(list_s)-1, 0, -1):
        #     res += list_s[i]+ " "

        # res += list_s[0]

        # return res

        s = s.split()
        s = s[::-1]
        s = " ".join(s)
        return s