from typing import List
class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:

        cash = 0
        hold = -prices[0]

        for price in prices[1:]:
            cash = max(cash, hold + price - fee) # 파는 경우
            hold = max(hold, cash - price) # 사는 경우

        return cash