class Solution:
    def isValid(self, s):
        stack = []
        for c in s:
            if c in "([{":
                stack.append(c)
            else:
                if not stack or \
                   (c == ')' and stack.pop() != '(') or \
                   (c == ']' and stack.pop() != '[') or \
                   (c == '}' and stack.pop() != '{'):
                    return False
        return not stack