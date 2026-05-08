class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS, COLS = len(heights), len(heights[0])
        directions = [(1,0),(-1,0),(0,1),(0,-1)]

        def _is_valid(r,c):
            return 0<=r<ROWS and 0<=c<COLS
        def isPacific(r,c):
            return r < 0 or c < 0
        def isAtlantic(r,c):
            return r >= ROWS or c >= COLS
        def bfs(i,j):
            q = deque([(i,j)])
            canPacific = False
            canAtlantic = False
            visited = set()

            while q:
                r, c = q.popleft()
                
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if isPacific(nr, nc):
                        canPacific = True
                    if isAtlantic(nr, nc):
                        canAtlantic = True
                    if (_is_valid(nr,nc) and 
                        heights[r][c] >= heights[nr][nc] and
                        (nr,nc) not in visited):
                        q.append((nr,nc))
                        visited.add((nr, nc))
                if canPacific and canAtlantic:
                    return True
            return canPacific and canAtlantic

        res = []
        for i in range(ROWS):
            for j in range(COLS):
                if bfs(i,j):
                    res.append([i,j])
        return res
