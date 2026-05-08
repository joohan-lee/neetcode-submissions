class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # DFS
        directions = [(0,1),(0,-1),(1,0),(-1,0)]
        def _is_valid_point(p):
            i,j = p
            return 0<=i<len(grid) and 0<=j<len(grid[0])
        def dfs(i,j):
            if not _is_valid_point((i,j)) or grid[i][j] == '0':
                return
            
            grid[i][j] = '0'
            for dr, dc in directions:
                dfs(i+dr, j+dc)
            

        
        
        res = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    dfs(i,j)
                    res += 1
        return res