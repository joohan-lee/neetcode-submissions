class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS, COLS = len(heights), len(heights[0])
        pac = set()
        atl = set()
        
        def _is_valid(r,c):
            return 0<= r < ROWS and 0<= c < COLS
        def dfs(i,j,visit):
            if ((i,j) in visit or
                i < 0 or i >= ROWS or
                j < 0 or j >= COLS):
                return

            visit.add((i,j))
            for dr, dc in [(0,1), (0,-1), (1,0), (-1,0)]:
                nr, nc = i + dr, j + dc
                if _is_valid(nr,nc) and heights[nr][nc] >= heights[i][j]:
                    dfs(nr,nc,visit)
        
        # First row goes to pac and last row goes to atl
        for c in range(COLS):
            dfs(0, c, pac)
            dfs(ROWS-1, c, atl)
        
        # First column goes to pac and last column goes to pac
        for r in range(ROWS):
            dfs(r, 0, pac)
            dfs(r, COLS-1, atl)

        res = []
        for i in range(ROWS):
            for j in range(COLS):
                if (i,j) in pac and (i,j) in atl:
                    res.append((i,j))
        
        return res
                

        