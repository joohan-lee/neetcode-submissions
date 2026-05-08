class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        # BFS
        adj = defaultdict(list)
        for u, v, t in times:
            adj[u].append((v, t))
        
        q = deque([(k, 0)])
        dist = {i: 1e6 for i in range(1, n+1)}

        while q:
            node, cost = q.popleft()
            
            # 2. 꺼내보았는데 새로운 cost가 더 작지 않으면 더 이상 탐색하지 않음.
            if dist[node] <= cost:
                continue
            
            dist[node] = cost
            
            for nei_node, cost_to_nei in adj[node]:
                # 1. 일단 모든 노드를 탐색하고,
                q.append((nei_node, cost + cost_to_nei))
        
        # print(f'{dist=}')
        res = max(dist.values()) 
        return res if res < 1e6 else -1