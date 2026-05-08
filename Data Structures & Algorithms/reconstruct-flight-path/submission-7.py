class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        adj = defaultdict(list)
        edge_cnt = defaultdict(int)
        tickets.sort()
        for src, dst in tickets:
            adj[src].append(dst)
            edge_cnt[(src,dst)] += 1
        # # Sort
        # for k, l in adj.items():
        #     adj[k] = sorted(l)
        # print(f'{adj=}')
        
        res = []
        N = len(tickets)

        def dfs(i, curr, node):
            # print(f'{i=}, {curr=}, {node=}')
            # if len(res) > 0:
            #     return
            if i == N:
                res.append(curr.copy())
                return True
            
            for nei in adj[node]:
                if not (edge_cnt[(node,nei)] == 0):
                    edge_cnt[(node, nei)] -= 1
                    curr.append(nei)
                    if dfs(i+1, curr, nei): return True
                    curr.pop()
                    edge_cnt[(node, nei)] += 1
        
        dfs(0, ["JFK"], "JFK")
        # print(f'{res=}')
        return res[0]

        