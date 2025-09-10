class Solution:
    def reverseVowels(self, s: str) -> str:
        """
        그냥 two pointer로 오면서 바꿔야겠다
        """

        left = 0
        right = len(s) - 1
        a = ['a','e','i','o','u','A','E','I','O','U']
        s = list(s)
        while left < right:
            if s[left] not in a:
                left += 1
            
            if s[right] not in a:
                right -= 1

            if s[left] in a and s[right] in a:
                temp = s[right]
                s[right] = s[left]
                s[left] = temp
                left += 1
                right -= 1

        s = "".join(s)

        return s