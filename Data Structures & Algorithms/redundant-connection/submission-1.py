class DSU:
    def __init__(self, n):
        self.parent = list(range(n))
        self.size = [1] * (n)
    
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
        
        self.parent[pu] = pv
        self.size[pv] += self.size[pu]
        
        return True

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        adj = {i: [] for i in range(len(edges)+1)}

        dsu = DSU(len(edges) + 1)
        for u, v in edges:
            if not dsu.union(u, v):
                return [u,v]
        