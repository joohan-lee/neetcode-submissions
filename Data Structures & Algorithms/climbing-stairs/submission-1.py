class Solution:
    def climbStairs(self, n: int) -> int:
        '''
        dp[i] = dp[i-2] + dp[i-1] (i > 2)
        dp[0] = 0
        dp[1] = 1
        dp[2] = 2

        '''
        dp = [0] * (n+1)
        if n == 0:
            return 0
        if n == 1:
            return 1
        if n == 2:
            return 2
        dp[0], dp[1], dp[2] = 0, 1, 2

        for i in range(3, n+1):
            dp[i] = dp[i-2] + dp[i-1]
        
        return dp[n]