class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        # Multi-source BFS. Start from treasures
        INF = 2**31 - 1
        ROWS, COLS = len(grid), len(grid[0])

        visited = set()
        q = deque()
        # Store treasure points
        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == 0:
                    q.append((i,j))
                    visited.add((i,j))

        def _is_valid(r,c):
            return 0<= r < ROWS and 0<= c < COLS and grid[r][c] != -1
        
        # BFS from treasures
        curr_dist = 0
        while q:
            len_q = len(q)
            for _ in range(len_q):
                r, c = q.popleft()
                grid[r][c] = curr_dist
                for dr, dc in [(0,1),(0,-1),(1,0),(-1,0)]:
                    nr, nc = r + dr, c + dc
                    if _is_valid(nr, nc) and (nr, nc) not in visited:
                        q.append((nr,nc))
                        visited.add((nr,nc))
            curr_dist += 1
