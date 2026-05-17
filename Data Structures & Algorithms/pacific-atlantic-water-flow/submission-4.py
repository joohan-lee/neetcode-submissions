class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        # bfs
        # Get all points starting from pacific (uphill)
        # Get all points starting from atlantic (uphill)
        # Get common points = points that can reach both oceans

        pac, atl = set(), set()
        pac_q, atl_q = [], []
        ROWS, COLS = len(heights), len(heights[0])

        for c in range(COLS):
            pac_q.append((0, c))
            atl_q.append((ROWS-1, c))
        
        for r in range(ROWS):
            pac_q.append((r, 0))
            atl_q.append((r, COLS-1))
        
        def bfs(source, visit):
            q = deque(source)
            while q:
                r, c = q.popleft()
                visit.add((r,c))
                for dr, dc in [(0,1), (0,-1), (1,0), (-1,0)]:
                    nr = r + dr
                    nc = c + dc
                    if 0 <= nr < ROWS and 0 <= nc < COLS and heights[nr][nc] >= heights[r][c] and (nr,nc) not in visit:
                        q.append((nr,nc))
                        visit.add((nr,nc))
        
        bfs(pac_q, pac) # while bfs, add points to the pac set
        bfs(atl_q, atl)
        
        res = []
        for r in range(ROWS):
            for c in range(COLS):
                if (r,c) in pac and (r,c) in atl:
                    res.append([r,c])
        return res