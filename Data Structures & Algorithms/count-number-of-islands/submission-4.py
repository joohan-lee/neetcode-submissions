class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])

        def is_valid(r,c):
            return 0<=r<ROWS and 0<=c<COLS and grid[r][c] == "1"
        # BFS
        def bfs(i,j):
            q = deque([(i,j)])

            while q:
                r, c = q.popleft()

                grid[r][c] = "0" # Mark as visit

                for dr, dc in [(0,1),(0,-1),(1,0),(-1,0)]:
                    nr = r + dr
                    nc = c + dc

                    if is_valid(nr,nc):
                        q.append((nr,nc))
                        grid[nr][nc] = "0"

        

        res = 0
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == "1":
                    bfs(r,c)
                    res += 1
        
        return res