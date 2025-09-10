# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        """
        
        n // 2 해서 물어보고 결과 보고
        그거에 대해 또 n // 2 해서 물어보고
        이렇게 하면 될텐데
        
        """
        start = 1
        end = n

        while start <= end:
            mid = (start + end) // 2 

            # num == pick
            if guess(mid) == 0:
                return mid
            # num > pick
            elif guess(mid) == -1:
                end = mid -1

            elif guess(mid) == 1:
                start = mid + 1