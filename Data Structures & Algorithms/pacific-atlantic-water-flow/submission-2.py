class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        res = []
        pac, atl = set(), set()
        ROWS, COLS = len(heights), len(heights[0])

        def dfs(r, c, visit):
            if (
                (r,c) in visit
            ):
                return
            visit.add((r,c)) #방문처리
            for dr, dc in [(0,1), (0,-1), (1,0), (-1,0)]:
                nr = r + dr
                nc = c + dc
                if (0<=nr<ROWS) and (0<=nc<COLS) and heights[r][c] <= heights[nr][nc]:
                    dfs(nr, nc, visit)

        # First row goes to pac, last row goes to atl
        for c in range(COLS):
            dfs(0, c, pac)
            dfs(ROWS-1,c, atl)
        # First col goes to pac, last col goes to atl
        for r in range(ROWS):
            dfs(r, 0, pac)
            dfs(r, COLS-1, atl)
        
        # If a certain point can go both, add it to res
        for r in range(ROWS):
            for c in range(COLS):
                if (r,c) in pac and (r,c) in atl:
                    res.append((r,c))
        return res
