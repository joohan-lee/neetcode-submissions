class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        adj = {i: [] for i in range(len(edges)+1)}

        def dfs(node, parent):
            if node in visited:
                return False
            visited.add(node)
            for nei in adj[node]:
                if nei == parent:
                    continue
                if not dfs(nei, node):
                    return False
                        
            return True
        
        # Create undirected graph
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
            visited = set() # Reset everytime
            if not dfs(u, -1):
                return [u, v]
