class Solution:
    def climbStairs(self, n: int) -> int:
        """
                0
              /   \
             1    2
           /  \  /  \
           2  3  3  4
           ...
               3
            2     1
        1    0   0
        """
        cache = [-1] * (n+1)
        def dfs(remain):
            if remain < 0:
                cache[remain] = 0
                return 0
            if remain == 0:
                cache[remain] = 1
                return 1
            if cache[remain] != -1:
                return cache[remain]

            cache[remain] = dfs(remain - 1) + dfs(remain - 2)
            return cache[remain]
        
        return dfs(n)
