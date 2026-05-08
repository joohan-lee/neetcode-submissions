class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        directions = [(0,1), (0,-1), (1,0), (-1,0)]
        def _is_valid(r, c):
            return 0<=r<len(grid) and 0<=c < len(grid[0]) and grid[r][c] == 1
        def dfs(i,j):
            if not _is_valid(i,j):
                return 0
            grid[i][j] = 0
            return 1 + (dfs(i + 1, j)
                + dfs(i - 1, j)
                + dfs(i, j + 1)
                + dfs(i, j - 1))



        N = len(grid)
        M = len(grid[0])
        max_size = 0
        for r in range(N):
            for c in range(M):
                if grid[r][c] == 1:
                    max_size = max(max_size, dfs(r,c))
        return max_size