class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        start = prices[0]
        res = 0
        for end in range(len(prices)):
            start = min(start, prices[end])
            res = max(res, prices[end] - start)
        return res