class DSU:
    def __init__(self, n):
        self.parent = list(range(n))
        self.size = [1] * n
        self.components = n
    
    def find(self, node):
        # Find the most parent
        if self.parent[node] == node:
            return node
        self.parent[node] = self.find(self.parent[node])
        return self.parent[node]
    
    def union(self, u, v):
        pu, pv = self.find(u), self.find(v)
        if pu == pv:
            # already has in same component
            return False
        
        if self.size[pu] >= self.size[pv]:
            # Add pv to pu
            self.parent[pv] = pu
            self.size[pu] += self.size[pv]
        else:
            self.parent[pu] = pv
            self.size[pv] += self.size[pu]
        self.components -= 1
        return True
    
class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        uf = DSU(n)

        for u, v in edges:
            if not uf.union(u, v):
                return False
        return uf.components == 1
        