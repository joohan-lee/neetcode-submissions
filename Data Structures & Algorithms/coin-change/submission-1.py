class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        """
        [1,3,4,5] / 7
        5+1+1=7, 3+4=7

              1
          /.     \
        1 3 4 5   1 3 4 5
       
        """
        coins.sort()

        memo = {}
        def dfs(left):
            if left < 0:
                return float('inf')
            if left == 0:
                return 0
            if left in memo:
                return memo[left]
            
            # 현재 지점의 자식들 중 minimum을 memoization.
            res = float('inf')
            for i in range(len(coins)):
                res = min(res,  1 + dfs(left - coins[i]))
            
            memo[left] = res
            return res
        
        
        ret = dfs(amount)
        return ret if ret != float('inf') else -1
        