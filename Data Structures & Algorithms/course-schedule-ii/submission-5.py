class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # Topological Sort

        # 1. Check indegree at each node.
        g = defaultdict(list) # {pre: [crs1, crs2, ...]}
        indegree = [0 for _ in range(numCourses)]
        for crs, pre in prerequisites:
            g[pre].append(crs)
            indegree[crs] += 1

        # 2. Add nodes with zero indegree to queue
        q = deque()
        for crs in range(len(indegree)):
            if indegree[crs] == 0:
                q.append(crs)

        # 3. Pop from queue and decrement indegree for adjacent nodes
        taken = []
        while q:
            pre = q.popleft()
            taken.append(pre)
            for crs in g[pre]:
                indegree[crs] -= 1
                if indegree[crs] == 0:
                    q.append(crs)

        # 4. Check if the number of nodes we visited and the number of courses are the same.
        return taken if len(taken) == numCourses else []