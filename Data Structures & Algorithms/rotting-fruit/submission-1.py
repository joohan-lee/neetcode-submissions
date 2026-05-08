class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        
        q = deque()

        num_of_fruits = 0
        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == 2:
                    q.append((i,j))
                    num_of_fruits += 1
                elif grid[i][j] == 1:
                    num_of_fruits += 1
            
        
        def _is_valid(r,c):
            return 0 <= r < ROWS and 0 <= c < COLS and grid[r][c] == 1
        num_of_rotten_fruits = len(q)
        minutes = 0
        visited = set()
        while num_of_rotten_fruits < num_of_fruits and q:
            len_q = len(q)
            for _ in range(len_q):
                r, c = q.popleft()
                for dr, dc in [(0,1),(0,-1),(1,0),(-1,0)]:
                    nr, nc = r + dr, c + dc
                    if _is_valid(nr, nc) and (nr, nc) not in visited:
                        grid[nr][nc] = 2
                        q.append((nr,nc))
                        visited.add((nr,nc))
                        num_of_rotten_fruits += 1
            minutes += 1

        return minutes if num_of_rotten_fruits == num_of_fruits else -1
