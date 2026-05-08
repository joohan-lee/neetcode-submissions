class DSU:
    def __init__(self, n):
        self.parent = list(range(n+1))
        self.size = [1 for _ in range(n+1)]
        
    
    def find(self, node):
        p = self.parent[node]
        while p != self.parent[p]:
            p = self.parent[p]
        return p
            

        # if node == self.parent[node]:
        #     return node
        # self.parent[node] = self.find(self.parent[node])
        # return self.parent[node]

        # if self.parent[node] != node:
        #     self.parent[node] = self.find(self.parent[node])
        # return self.parent[node]
    
    def union(self, u, v):
        pu = self.find(u)
        pv = self.find(v)
        if pu == pv:
            # Means already same parent. No need to union.
            return False
        if self.size[pu] >= self.size[pv]:
            self.size[pu] += self.size[pv]
            self.parent[pv] = pu
        else:
            self.size[pv] += self.size[pu]
            self.parent[pu] = pv
        return True
        

class Solution:
    def _is_valid(self, r, c, grid):
        return 0 <= r < len(grid) and 0 <= c < len(grid[0]) and grid[r][c] == '1'
    def _index(self, r, c, grid):
        return r * len(grid[0]) + c
    def numIslands(self, grid: List[List[str]]) -> int:
        # Disjoint Set Union

        directions = [(0,1), (0,-1), (1,0), (-1,0)]
        island = 0
        dsu = DSU(len(grid)*len(grid[0]))
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == '1':
                    island += 1 

                    for dr, dc in directions:
                        nr = dr + r
                        nc = dc + c
                        if not self._is_valid(nr, nc, grid):
                            continue
                        
                        if dsu.union(self._index(r,c, grid), self._index(nr,nc, grid)):
                            island -= 1 # # You can think as we are decrementing as num of unions.
        
        return island


        