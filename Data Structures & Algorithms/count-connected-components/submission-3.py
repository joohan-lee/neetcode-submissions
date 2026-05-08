class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        visit = set()
        # Build graph
        g = defaultdict(list)
        for u, v in edges:
            g[u].append(v)
            g[v].append(u)

        def dfs(node, parent):
            if node in visit:
                return
            visit.add(node)
            for nei in g[node]:
                if nei == parent:
                    continue
                dfs(nei, node)

        components = 0
        for node in range(n):
            if node not in visit:
                components += 1
                dfs(node, -1)
        return components