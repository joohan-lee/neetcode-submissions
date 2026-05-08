class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # Build graph {crs -> [pre,...]}
        g = defaultdict(list)
        for crs, pre in prerequisites:
            g[crs].append(pre)
        
        taken = set()
        cur_path = set()
        def dfs(crs):
            if crs in cur_path:
                # cycle detected
                return False
            if taken in cur_path:
                return True
            
            cur_path.add(crs)
            for pre in g[crs]:
                if not dfs(pre):
                    return False
            cur_path.remove(crs)
            taken.add(crs)
            return True
        
        for crs in range(numCourses):
            if not dfs(crs):
                return False
        return True
        

