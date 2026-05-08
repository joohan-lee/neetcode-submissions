class UnionFind:
    def __init__(self, n, land):
        self.parent = list(range(n))
        self.size = [1] * (n)
        self.components = land
    
    def find(self, node):
        if self.parent[node] == node:
            return node
        self.parent[node] = self.find(self.parent[node])
        return self.parent[node]
    
    def union(self, u, v):
        pu = self.find(u)
        pv = self.find(v)

        if pu == pv:
            return False
        
        self.components -= 1
        if self.size[pu] > self.size[pv]:
            self.parent[pv] = pu
            self.size[pu] += self.size[pv]
        else:
            self.parent[pu] = pv
            self.size[pv] += self.size[pu]
    
    def count_components(self):
        return self.components
        
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # UnionFind
        ROWS, COLS = len(grid), len(grid[0])

        land = 0
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == "1":
                    land += 1
        
        uf = UnionFind(ROWS*COLS, land)
        
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == "1":
                    for dr, dc in [(0,1),(0,-1),(1,0),(-1,0)]:
                        nr = r + dr
                        nc = c + dc
                        if 0<= nr < ROWS and 0 <= nc < COLS and grid[nr][nc] == "1":
                            uf.union(r*COLS + c, nr * COLS + nc)
        
        return uf.count_components()
