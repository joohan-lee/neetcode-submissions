class DSU:
    def __init__(self, n):
        self.parent = list(range(n+1))
        self.size = [1] * (n+1)
    
    def find(self, node):
        if node == self.parent[node]:
            return node
        self.parent[node] = self.find(self.parent[node])
        return self.parent[node]
    
    def union(self, u, v):
        pu = self.find(u)
        pv = self.find(v)
        if pu == pv:
            return
        if self.size[pu] >= self.size[pv]:
            self.size[pu] += self.size[pv]
            self.parent[pv] = pu
        else:
            self.size[pv] += self.size[pu]
            self.parent[pu] = pv
    
    def getSize(self, node):
        parent = self.find(node)
        return self.size[parent]


class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        def _is_valid(r,c):
            return 0<=r<N and 0<=c<M and grid[r][c] == 1

        def _index(r,c):
            return r * M + c
        directions = [(0,1), (0,-1), (1,0), (-1,0)]
        N = len(grid)
        M = len(grid[0])

        dsu = DSU(N*M)
        
        max_area = 0
        for r in range(N):
            for c in range(M):
                if grid[r][c] == 1:
                    for dr, dc in directions:
                        nr, nc = r + dr, c + dc
                        if _is_valid(nr, nc):
                            dsu.union(_index(r,c), _index(nr,nc))
                    max_area = max(max_area, dsu.getSize(_index(r,c)))
        # print(f'{dsu.size=}')
        return max_area