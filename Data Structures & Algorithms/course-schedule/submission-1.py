class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        preMap = {i: [] for i in range(numCourses)}
        q = deque()
        indegree = [0] * (numCourses)

        for src, dst in prerequisites:
            indegree[dst] += 1
            preMap[src].append(dst)
        
        for crs in range(numCourses):
            if indegree[crs] == 0:
                q.append(crs)
        
        ans = []
        while q:
            cur = q.popleft()
            ans.append(cur)
            for nei in preMap[cur]:
                indegree[nei] -= 1 # 인접 노드 in-degree 1 감소
                if indegree[nei] == 0:
                    q.append(nei)
        
        return len(ans) == numCourses

        
