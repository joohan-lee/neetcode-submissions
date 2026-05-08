class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        # 1) Build graph
        # Nodes
        # Use set() to avoid creating duplicated edges
        g = {c: set() for word in words for c in word}
        indegree = {c: 0 for c in g}

        # Edges
        for i in range(len(words) - 1):
            w1, w2 = words[i], words[i+1]
            min_len = min(len(w1), len(w2))
            
            # Edge case. If prefix comes after longer word, invalid.
            if w1[:min_len] == w2[:min_len] and len(w1) > len(w2):
                return ""
            
            # Add edges
            for j in range(min_len):
                # In min_len, we can get a priority rule if ch is different.
                if w1[j] != w2[j]:
                    # Since w1[j] comes first before w2[j], create an edge w1[j] -> w2[j]
                    if w2[j] not in g[w1[j]]:
                        # 실제 edge 추가될 때만 indegree추가 해야함.
                        g[w1[j]].add(w2[j])
                        indegree[w2[j]] += 1
                    break # Don't need to see further, since no meaning after this.
        
    
        # 2) Traverse graph and get order (DFS/BFS / Disjoint Set Union)
        q = deque([c for c in indegree if indegree[c] == 0])
        res = []
        while q:
            node = q.popleft()
            res.append(node)
            for nei in g[node]:
                indegree[nei] -= 1
                if indegree[nei] == 0:
                    q.append(nei)
        
        if len(res) != len(g):
            # cycle detected. invalid.
            return ""
        
        return "".join(res)

