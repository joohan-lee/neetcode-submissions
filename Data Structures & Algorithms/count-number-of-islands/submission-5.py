class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])

        # DFS
        def dfs(r,c):
            if (r < 0 or
                c < 0 or
                r >= ROWS or
                c >= COLS or
                grid[r][c] == "0"):
                return
            
            grid[r][c] = "0" # Mark as visit

            dfs(r+1,c)
            dfs(r-1,c)
            dfs(r,c+1)
            dfs(r,c-1)
            
        
        res = 0
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == "1":
                    dfs(r,c)
                    res+=1
        return res
