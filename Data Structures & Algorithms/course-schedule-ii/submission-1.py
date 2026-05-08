class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj = {i: [] for i in range(numCourses)}

        q = deque()
        indegree = [0] * numCourses

        for dst, src in prerequisites:
            indegree[dst] += 1
            adj[src].append(dst)
        
        for crs in range(numCourses):
            if indegree[crs] ==0:
                q.append(crs)
        
        # print(f'{q=}')
        res = []
        while q:
            crs = q.popleft()
            res.append(crs)
            for nei in adj[crs]:
                indegree[nei] -= 1
                if indegree[nei] == 0:
                    q.append(nei)
        return res if len(res) == numCourses else []



