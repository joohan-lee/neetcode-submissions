class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        
        islands = 0
        ROWS, COLS = len(grid), len(grid[0])
        directions = [(0,1), (0,-1), (1,0), (-1,0)]

        def bfs(i,j):
            q = deque([(i,j)])
            grid[i][j] = "0"

            while q:
                r, c = q.popleft()

                for dr, dc in directions:
                    nr = r + dr
                    nc = c + dc
                    if 0 <= nr < ROWS and 0 <= nc < COLS and grid[nr][nc] == "1":
                        q.append((nr,nc))
                        grid[nr][nc] = "0"

        
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == "1":
                    # island
                    islands += 1
                    bfs(r,c)
        return islands
                    
        