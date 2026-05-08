class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        g = defaultdict(list)
        for u, v, w in times:
            g[u].append((v, w))
        
        distances = [float('inf')] * (n+1)
        distances[0] = distances[k] = 0

        min_heap = [(0, k)]
        while min_heap:
            d, node = heapq.heappop(min_heap)

            for adj, w in g[node]:
                if distances[adj] > distances[node] + w:
                    distances[adj] = distances[node] + w
                    heapq.heappush(min_heap, (d + w, adj))
        
        res = max(distances) 
        return res if res != float('inf') else -1