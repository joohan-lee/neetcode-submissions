class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        start = 0
        for end in range(len(prices)):
            if prices[end] < prices[start]:
                start = end
            max_profit = max(max_profit, prices[end] - prices[start])
        
        return max_profit
