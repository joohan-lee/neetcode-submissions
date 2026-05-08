class Solution:
    def climbStairs(self, n: int) -> int:
        '''
            0
        1       2
    2.    3.  3.  4
        '''
        memo = {}
        def dfs(i):
            if i > n:
                return 0
            if i == n:
                return 1
            if i in memo:
                return memo[i]
            
            a = dfs(i + 1)
            b = dfs(i + 2)

            memo[i] = a + b

            return a + b
        
        return dfs(0)
        