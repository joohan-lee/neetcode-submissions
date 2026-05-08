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
            
            if dist[node] > cost:
                dist[node] = cost
            
            for nei_node, cost_to_nei in adj[node]:
                # 다음 노드로 가는게 더 최단 거리이면 탐색.
                if cost + cost_to_nei < dist[nei_node]:
                    q.append((nei_node, cost + cost_to_nei))
        
        # print(f'{dist=}')
        res = max(dist.values()) 
        return res if res < 1e6 else -1