
import math

class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        """
        곱한거 받고
        sort하고
        success보다 큰 숫자가 시작하는 위치 찾으면 되겠네 그러면 그 뒤에 있는 애들 갯수는 다 success한 애들이니까
        
        3, 4, 6, 8, 9, 10 이곳에 7
        
        start end 두고 만약 mid구해서 같으면 mid => len() - mid
        start end 두고 mid 구하면 start = end 같아질때까지 반복하면 되나
        
        나눗셈이라,, 흠..
        """

        n = len(spells)
        potions.sort()
        res = [0] * n

        def binary_search(data, success):
            start, end = 0, len(data) - 1

            while start <= end:
                mid = (start + end) // 2
                if data[mid] == success:
                    return mid
                elif data[mid] < success:
                    start = mid + 1
                elif data[mid] > success:
                    end = mid - 1

            return start

        for i in range(n):
            thresh = math.ceil(success / spells[i])
            index = binary_search(potions, thresh)
            res[i] = len(potions) - index

        return res
