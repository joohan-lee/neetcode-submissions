class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        adj = defaultdict(list)

        for i in range(len(points)-1):
            for j in range(i+1, len(points)):
                p1, p2 = tuple(points[i]), tuple(points[j])
                cost = abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])
                adj[p1].append((p2, cost))
                adj[p2].append((p1, cost))
        
        # print(f'{adj=}')
        pq = [(0, tuple(points[0]))]

        total_cost = 0
        visited = set()
        while pq:
            # print(f'{pq=}, {total_cost=}, {visited=}')
            cost, node = heapq.heappop(pq)
            # print(f'{cost=}, {node=}')

            if node in visited:
                continue
            visited.add(node)
            total_cost += cost

            for nei in adj[node]:
                # print(f'{nei=}, {visited=}')
                nei_node, nei_cost = nei
                if nei_node not in visited:
                    heapq.heappush(pq, (nei_cost, nei_node))
        return total_cost