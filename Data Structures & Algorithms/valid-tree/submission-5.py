class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        """
        1) no cycle
        2) only one component  (fully connected)
            - if n nodes, only n-1 edges exist

        Way 1. DFS/BFS Traverse from zero and see if there is cycle
        Way 2. Disjoint Set Union. See if there is a cycle
        """
        if len(edges) != n - 1:
            return False 
        # DFS
        
        # 1) Build graph
        g = defaultdict(list)
        for u, v in edges:
            g[u].append(v)
            g[v].append(u)

        visit = set() # to detect cycle
        
        def dfs(node, prev):
            if node in visit:
                return False
            visit.add(node)
            for nei in g[node]:
                if nei == prev:
                    continue
                if not dfs(nei, node):
                    return False
            # visit.remove(node)
            return True
        
        return dfs(0, -1) and len(visit) == n