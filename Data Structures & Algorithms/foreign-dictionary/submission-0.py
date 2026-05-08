class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        # 1) Build graph
        # Nodes
        # Use set() to avoid creating duplicated edges
        g = {c: set() for word in words for c in word}

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
                    g[w1[j]].add(w2[j])
                    break # Don't need to see further, since no meaning after this.
        
    
        # 2) Traverse graph and get order (DFS/BFS / Disjoint Set Union)
        order = []
        visit = set()
        path = set()
        def dfs(node):
            # Post order DFS
            if node in path:
                return False
            if node in visit:
                return True
            
            visit.add(node)
            path.add(node)
            for nei in g[node]:
                if not dfs(nei):
                    return False
            path.remove(node)
            order.append(node)
            return True
        
        for c in g.keys():
            if not dfs(c):
                return ""
        return "".join(order[::-1])