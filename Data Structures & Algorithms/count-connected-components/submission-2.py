class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        res = 0
        visited = set()

        adj = {i: [] for i in range(n)}
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        def bfs(node):
            q = deque([(node, -1)])
            while q:
                curr_node, prev_node = q.popleft()
                visited.add(curr_node)
                for nei in adj[curr_node]:
                    if nei == prev_node:
                        continue
                    if nei not in visited:
                        q.append((nei, curr_node))

        for node in range(n):
            if node not in visited:
                res += 1
                bfs(node)
        
        return res