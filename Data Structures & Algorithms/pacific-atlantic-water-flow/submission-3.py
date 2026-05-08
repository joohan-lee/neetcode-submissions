class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        res = []
        pac, atl = set(), set()
        ROWS, COLS = len(heights), len(heights[0])

        def bfs(r, c, visit):
            q = deque()
            visit.add((r,c))
            q.append((r,c))

            while q:
                x, y = q.popleft()
                for dx, dy in [(0,1), (0,-1), (1,0), (-1,0)]:
                    nx = x + dx
                    ny = y + dy
                    if 0<=nx<ROWS and 0<=ny<COLS and (nx, ny) not in visit and heights[nx][ny] >= heights[x][y]:
                        visit.add((nx, ny))
                        q.append((nx, ny))


        # First row goes to pac, last row goes to atl
        for c in range(COLS):
            bfs(0, c, pac)
            bfs(ROWS-1,c, atl)
        # First col goes to pac, last col goes to atl
        for r in range(ROWS):
            bfs(r, 0, pac)
            bfs(r, COLS-1, atl)
        
        # If a certain point can go both, add it to res
        for r in range(ROWS):
            for c in range(COLS):
                if (r,c) in pac and (r,c) in atl:
                    res.append((r,c))
        return res
