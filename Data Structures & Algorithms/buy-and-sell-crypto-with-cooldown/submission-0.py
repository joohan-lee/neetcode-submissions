class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """
        have coin
            - can sell
        not have coin
            - sold yday -> cannot do anything
            - or can buy
        dfs(i, holding) -> max_profit
        # State: holding or selling?
        # If buy -> i + 1
        # If sell -> i + 2 (cooldown)
        """

        dp = {}
        
        def dfs(i, holding):
            if i >= len(prices):
                return 0
            if (i, holding) in dp:
                return dp[(i, holding)]
            
            max_p = 0
            # do nothing (whether it holds a stock or not)
            cooldown = dfs(i+1, holding)
            if holding:
                # Sell
                sell = dfs(i+2, not holding) + prices[i] # cooldown해야하니 그 다다음으로.
                max_p = max(sell, cooldown)
            else:
                # Buy
                buy = dfs(i+1, not holding) - prices[i]
                max_p = max(buy, cooldown)
            dp[(i, holding)] = max_p
            return max_p
        
        return dfs(0, False)