class DSU:
    def __init__(self, n):
        self.parent = list(range(n+1))
        self.size = [1] * (n+1)
        self.count = n
    
    def find(self, node):
        if node != self.parent[node]:
            self.parent[node] = self.find(self.parent[node])
        return self.parent[node]

        # if node == self.parent[node]:
        #     return node
        # self.parent[node] = self.find(self.parent[node])
        # return self.parent[node]
    
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
        self.count -= 1
        return True

class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # Vaid Tree:
        #   - No cycle
        #   - Connected components
        dsu = DSU(n)
        for node1, node2 in edges:
            print(f'{node1=}, {node2=}')
            print(f'{dsu.parent=}')
            print(f'{dsu.size=}')
            if not dsu.union(node1, node2):
                return False
        
        print(f'{dsu.count=}')
        return dsu.count == 1


