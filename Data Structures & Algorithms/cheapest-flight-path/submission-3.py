class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        """
        k stops로 갈 수 있는 최단거리라 함은 즉, k+1 edges로 갈 수 있는 최단거리와 같음.
        즉, k+1 순회하는 벨맨포드를 하면 답을 구할 수 있음.
        """
        distance = [float('inf')] * n
        distance[src] = 0

        for i in range(k+1):
            prev = distance[:]
            for u, v, w in flights:
                if prev[u] + w < distance[v]:
                    distance[v] = prev[u] + w
        
        return distance[dst] if distance[dst] != float('inf') else -1










        # Graph 생성
        g = defaultdict(list)
        for f, t, p in flights:
            g[f].append((t, p)) # (dst, weight)

        # Dijkstra with k stops
        # stops 배열: 각 노드에 도달한 최소 stops 수
        min_stops = [float('inf')] * n
        min_stops[src] = 0
        min_heap = [(0, src, 0)] # (weight, node, stops)

        while min_heap:
            curr_distance, curr_node, stops = heapq.heappop(min_heap)
            
            if curr_node == dst:
                return curr_distance

            if stops > k:
                continue
            
            for adj, weight in g[curr_node]:
                new_distance = curr_distance + weight
                if stops + 1 < min_stops[adj]:
                    min_stops[adj] = stops+1
                    heapq.heappush(min_heap, (new_distance, adj, stops + 1))

        return -1