class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = defaultdict(list)
        for u, v, t in times:
            adj[u].append((v, t))

        dist = [1e6] * (n+1)
        def dfs(node, curr_cost):
            if dist[node] > curr_cost:
                dist[node] = curr_cost

            for nei_node, cost_to_nei in adj[node]:
                if curr_cost + cost_to_nei < dist[nei_node]:
                    dfs(nei_node, curr_cost + cost_to_nei)
        
        dist[k] = 0
        dist[0] = -1
        dfs(k, 0)
        # print(f'{dist=}')
        return max(dist) if 1e6 not in dist else -1