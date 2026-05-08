class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # Build graph
        g = defaultdict(list)

        for crs, pre in prerequisites:
            g[crs].append(pre)
        taken = set()
        path = set()
        def dfs(i):
            if i in path:
                # cycle detected
                return False
            if i in taken:
                # If already taken, ealry return
                return True
            
            path.add(i)
            # pre 다 들을 수 있는지 확인.
            for pre in g[i]:
                if not dfs(pre):
                    return False
            # 다 들을 수 있으면 현재 경로에서 제외하고, taken에 넣기.
            path.remove(i)
            taken.add(i)
            return True

        for i in range(numCourses):
            if not dfs(i):
                return False
        return True