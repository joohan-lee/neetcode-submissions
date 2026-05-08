class DSU:
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.size = [1] * n
        self.components = n
    
    def find(self, node):
        if node == self.parent[node]:
            return node
        self.parent[node] = self.find(self.parent[node])
        return self.parent[node]

    def union(self, u, v):
        pu = self.find(u)
        pv = self.find(v)

        if pu == pv:
            return False
        
        if self.size[pu] >= self.size[pv]:
            self.parent[pv] = pu
            self.size[pu] += self.size[pv]
        else:
            self.parent[pu] = pv
            self.size[pv] += self.size[pu]
        self.components -= 1
        return True



class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # Union-Find
        ROWS, COLS = len(grid), len(grid[0])
        
        uf = DSU(ROWS * COLS)
        def _index(r,c):
            return r*COLS + c
        
        water = 0
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == "0":
                    water += 1
                if grid[r][c] == "1":
                    for dr, dc in [(0,1), (0,-1),(1,0),(-1,0)]:
                        nr = r + dr
                        nc = c + dc
                        if 0<=nr<ROWS and 0<=nc<COLS and grid[nr][nc] == "1":
                            uf.union(_index(r,c), _index(nr,nc))
        return uf.components - water


        