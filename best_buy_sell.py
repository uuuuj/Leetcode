from typing import List
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        max_profit = 0
        min_prices = prices[0]
        for price in prices:
            if price < min_prices:
                min_prices = price
            elif price - min_prices > max_prices:
                max_prices = price - min_prices
        return max_prices
sol = Solution()
prices = [7,1,5,3,6,4]
result = sol.maxProfit(prices)
print(result)
