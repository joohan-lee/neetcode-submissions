class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        visit = set()
        # Build graph
        g = defaultdict(list)
        for u, v in edges:
            g[u].append(v)
            g[v].append(u)

        def bfs(i):
            q = deque()
            visit.add(i)
            q.append((i, -1))

            while q:
                node, parent = q.popleft()
                
                for nei in g[node]:
                    if nei == parent:
                        continue
                    if nei not in visit:
                        visit.add(nei)
                        q.append((nei, node))


        components = 0
        for node in range(n):
            if node not in visit:
                components += 1
                bfs(node)
        return components