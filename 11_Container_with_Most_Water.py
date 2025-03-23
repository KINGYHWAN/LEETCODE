class Solution:
    def maxArea(self, height: List[int]) -> int:
        """
        

        left = 0
        right = len(List) - 1

        
        """
        left = 0
        right = len(height) - 1
        res = 0
        while left < right:
            a = height[left]
            b = height[right]
            min_height = min(a, b)
            area = (right - left) * min_height
            
            if area > res:
                res = area

            if min_height == a:
                left += 1
            else:
                right -= 1

        return res