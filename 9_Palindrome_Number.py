class Solution(object):
    def isPalindrome(self, x):
        """
        rev = str(x)[::-1]

        :type x: int
        :rtype: bool
        
        """
        x_list = list(map(str, str(x)))
        rtype = True
        for i in range(len(x_list)):
            if x_list[i] != x_list[len(x_list)-i-1]:
                rtype = False

        return rtype  

        