class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # Topological Sort

        # 1) Build graph and indegree array
        g = defaultdict(list)
        indegree = [0] * numCourses

        for crs, pre in prerequisites:
            g[pre].append(crs)
            indegree[crs] += 1
        
        q = deque([i for i in range(numCourses) if indegree[i] ==0])
        res = []
        while q:
            pre = q.popleft()
            res.append(pre)

            for crs in g[pre]:
                indegree[crs] -= 1 # 현재 pre노드 없앴으니 이웃 노드 indegree -1
                if indegree[crs] == 0:
                    q.append(crs)
        if len(res) != numCourses:
            # raise ValueError("The graph has a cycle and cannot be topological sorted.")
            return False
        return True
        