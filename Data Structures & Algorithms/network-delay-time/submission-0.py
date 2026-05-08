class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = defaultdict(list)
        for u, v, t in times:
            adj[u].append((v, t))
        
        dist = [1e6] * (n+1)
        dist[0] = -1
        dist[k] = 0
        pq = []
        heapq.heappush(pq, (0, k))

        while pq:
            time, node = heapq.heappop(pq)

            for nei in adj[node]:
                nei_node = nei[0]
                nei_cost = nei[1]
                if time + nei_cost < dist[nei_node]:
                    dist[nei_node] = time + nei_cost
                    heapq.heappush(pq, (dist[nei_node], nei_node))
        
        # print(f'{dist=}')
        return int(max(dist)) if 1e6 not in dist else -1
