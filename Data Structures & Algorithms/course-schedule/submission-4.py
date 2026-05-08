class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # build graph {crs: [pre]}
        g = defaultdict(list)
        q = deque()
        indegree = [0] * numCourses
        for crs, pre in prerequisites:
            g[crs].append(pre)
            indegree[pre] += 1
        
        # Add indegree==0 to q
        for i in range(numCourses):
            if indegree[i] == 0:
                q.append(i)
        
        ans = []
        while q:
            cur = q.popleft()
            ans.append(cur)
            for nei in g[cur]:
                indegree[nei] -= 1
                if indegree[nei] == 0:
                    q.append(nei)
        return len(ans) == numCourses
    
