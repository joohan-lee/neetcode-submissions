class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = defaultdict(list)
        for u, v, t in times:
            adj[u].append((v, t))
        
        visited = set()
        pq = []
        heapq.heappush(pq, (0, k))

        t = -1
        while pq:
            time, node = heapq.heappop(pq)
            if node in visited:
                continue
            
            t = time # 최단거리일 때만 pop이 됨.
            visited.add(node)

            for nei in adj[node]:
                nei_node = nei[0]
                nei_cost = nei[1]
                # 우선순위 큐를 사용중이므로 모든 노드는 한번만 방문됨.
                if nei_node not in visited:
                    heapq.heappush(pq, (time + nei_cost, nei_node))
        
        # print(f'{dist=}')
        return t if len(visited) == n else -1
