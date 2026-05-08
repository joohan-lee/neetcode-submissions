class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        min_start = 101
        for i in range(len(prices)):
            if (min_start > prices[i]):
                min_start = prices[i]
            max_profit = max(max_profit, prices[i] - min_start)
        return max_profit
