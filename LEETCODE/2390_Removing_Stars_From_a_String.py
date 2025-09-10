class Solution:
    def removeStars(self, s: str) -> str:
        
        stack = []
        s_list = list(s)
        for i in range(len(s_list)):
            if s_list[i] == '*':
                stack.pop()
            else:
                stack.append(s_list[i])

        res = "".join(stack)
        return res
    