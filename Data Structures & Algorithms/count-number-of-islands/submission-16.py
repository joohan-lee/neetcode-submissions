class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        
        islands = 0
        ROWS, COLS = len(grid), len(grid[0])
        directions = [(0,1), (0,-1), (1,0), (-1,0)]

        def dfs(i,j):
            if (i < 0 or i >= ROWS
                or j < 0 or j >= COLS
                or grid[i][j] == "0"):
                return
            
            grid[i][j] = "0"
            for dr, dc in directions:
                nr = i + dr
                nc = j + dc
                dfs(nr,nc)

        
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == "1":
                    # island
                    islands += 1
                    dfs(r,c)
        return islands
                    
        