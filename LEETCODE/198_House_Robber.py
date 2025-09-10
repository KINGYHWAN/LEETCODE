from typing import List

class Solution:
    def rob(self, nums: List[int]) -> int:
        
        """
        
        1, 2, 5, 1, 3, 20, 8
        1, 2, 6, 3, 9, 26, 17 

        그러면 바로 옆 친구 제외하고 이전 값 중에 제일 큰거랑 더해야겠네

        dp[0] = nums[0]
        dp[1] = nums[1]
        n >= 2 -> dp[n] = max(dp[0:n-1] + nums[n])       
        """
        
        n = len(nums)
        
        if n == 1:
            return nums[0]

        if n == 2:
            return max(nums)

        dp = [0] * n 
        dp[0], dp[1] = nums[0], nums[1]
        for i in range(2, n):
            temp_dp = dp[0:i-1]
            dp[i] = max(temp_dp) + nums[i]

        return max(dp)