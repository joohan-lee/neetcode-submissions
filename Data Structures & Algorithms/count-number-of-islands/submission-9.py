class UnionFind:
    def __init__(self, size):
        self.parents = [i for i in range(size)]
        self.size = [1] * size
        self.components = size
    
    def count_components(self):
        return self.components
    
    def find(self, node):
        if node == self.parents[node]:
            return self.parents[node]
        self.parents[node] = self.find(self.parents[node])
        return self.parents[node]
    
    def union(self, u, v):
        pu = self.find(u)
        pv = self.find(v)
        if pu == pv:
            return False
        # Connect two components
        self.components -= 1
        if self.size[pu] > self.size[pv]:
            self.parents[pv] = pu
            self.size[pu] += self.size[pv]
        else:
            self.parents[pu] = pv
            self.size[pv] += self.size[pu]

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # Disjoint Set Union
        ROWS, COLS = len(grid), len(grid[0])

        uf = UnionFind(ROWS*COLS)
        
        def _index(r,c):
            return r * COLS + c

        water = 0
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == "0":
                    water += 1
                if grid[r][c] == "1":
                    for dr, dc in [(0,1),(-1,0),(1,0),(-1,0)]:
                        nr = r + dr
                        nc = c + dc
                        if 0 <= nr < ROWS and 0 <= nc < COLS and grid[nr][nc] == "1":
                            uf.union(_index(r,c), _index(nr,nc))
        
        return uf.count_components() - water