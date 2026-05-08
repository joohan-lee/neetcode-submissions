class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        adj = {i: [] for i in range(n)}
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
        
        q = deque([(0, -1)]) # curr_node, prev_node
        visited = set()
        while q:
            curr_node, prev_node = q.popleft()
            visited.add(curr_node)
            for nei in adj[curr_node]:
                if nei == prev_node:
                    continue
                if nei in visited:
                    return False
                q.append((nei, curr_node))

        return True if len(visited) == n else False
