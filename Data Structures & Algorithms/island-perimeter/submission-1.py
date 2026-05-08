class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        """
        when land encountered, check 4 adjacent and count no land-connected edges
        """
        N, M = len(grid), len(grid[0])
        
        edges = 0
        for r in range(N):
            for c in range(M):
                if grid[r][c] == 0:
                    continue
                    
                for dr, dc in [(0,1),(0,-1),(1,0),(-1,0)]:
                    nr = r + dr
                    nc = c + dc
                    if not (0 <= nr < N and 0<= nc < M) or grid[nr][nc] == 0:
                        edges += 1
        
        return edges