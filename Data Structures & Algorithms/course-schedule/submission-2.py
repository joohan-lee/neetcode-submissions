class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        g = {i: [] for i in range(numCourses)} # {crs: [pre1, pre2, ...]}

        # Build a graph
        for crs, pre in prerequisites:
            g[crs].append(pre)

        taken = set()
        cur_path = set()
        def dfs(crs):
            if crs in cur_path:
                # Cycle detected.
                return False
            if crs in taken:
                return True
            
            cur_path.add(crs)

            for pre in g[crs]:
                if dfs(pre) == False:
                    return False
            
            cur_path.remove(crs)
            taken.add(crs)
            return True
        
        for crs in range(numCourses):
            if not dfs(crs):
                return False
        
        return True