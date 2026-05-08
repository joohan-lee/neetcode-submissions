class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        INF = 2**31-1
        ROWS, COLS = len(grid), len(grid[0])
        
        
        def _is_valid(r,c):
            return 0<= r < ROWS and 0<=c <COLS and grid[r][c] != -1

        def bfs(i,j):
            visited=set()
            q = deque([(i,j)])
            min_dist = INF
            curr_dist = -1
            while q:
                len_q = len(q)
                curr_dist += 1
                for i in range(len_q):
                    r, c = q.popleft()
                    visited.add((r,c))
                    if grid[r][c] == 0:
                        return curr_dist

                    for dr, dc in [(0,1),(0,-1),(1,0),(-1,0)]:
                        nr, nc = r + dr, c + dc
                        if _is_valid(nr,nc) and (nr, nc) not in visited:
                            q.append((nr,nc))
                            visited.add((nr,nc))

        
        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == INF:
                    grid[i][j] = bfs(i,j)