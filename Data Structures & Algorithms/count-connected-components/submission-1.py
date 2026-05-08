class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        res = 0
        visited = set()

        adj = {i: [] for i in range(n)}
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        def dfs(node, parent):
            if node in visited:
                return
            visited.add(node)
            for nei in adj[node]:
                if nei == parent:
                    continue
                if nei not in visited:
                    dfs(nei,node)

        for node in range(n):
            if node not in visited:
                res += 1
                dfs(node, -1)
        
        return res