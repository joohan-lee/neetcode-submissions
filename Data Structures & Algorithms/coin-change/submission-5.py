class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        memo = {}
        def dfs(remain):
            if remain < 0:
                return float('inf')
            if remain == 0:
                return 0
            if remain in memo:
                return memo[remain]
            
            min_cnt = float('inf')
            for c in coins:
                min_cnt = min(min_cnt, dfs(remain - c))
            
            memo[remain] = min_cnt + 1
            return memo[remain]
        
        res = dfs(amount)
        return res if res != float('inf') else -1