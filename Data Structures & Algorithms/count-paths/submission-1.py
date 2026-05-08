class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        """
            dfs(0,0)
            /       \
        dfs(1,0)     dfs(0,1)
        ...
       /
  1=dfs(m-1,0)
        """
        memo = defaultdict(int)
        def dfs(i, j):
            if i > m-1 or j > n-1:
                return 0
            if i == m-1 or j == n-1:
                return 1
            if (i,j) in memo:
                return memo[(i,j)]
            memo[(i,j)] = dfs(i+1, j) + dfs(i, j+1)
            return memo[(i,j)]
        
        return dfs(0,0)