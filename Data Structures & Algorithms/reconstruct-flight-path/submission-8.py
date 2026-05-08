class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        adj = defaultdict(list)
        tickets.sort()
        for src, dst in tickets:
            adj[src].append(dst)
        
        res = ["JFK"]
        N = len(tickets)

        def dfs(node):
            if len(res) == N+1:
                return True
            
            temp = list(adj[node])
            for i, nei in enumerate(temp):
                adj[node].pop(i)
                res.append(nei)
                if dfs(nei): return True
                adj[node].insert(i, nei)
                res.pop()
        
        dfs("JFK")
        
        return res

        