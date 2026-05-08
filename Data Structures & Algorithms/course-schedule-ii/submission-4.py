class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        """
        0  ->  1
        |      |
        \/     \/
        2  ->  3

        Visit all nodes with dfs without cycle, we can finish all courses.
        If cycle exists or independent node exists, cannot finish.
        """
        # Build a graph
        g = defaultdict(list) # {crs: [pre1, pre2, ...]}
        for crs, pre in prerequisites:
            g[crs].append(pre)

        # Iterate all courses as a starting point
        taken = set()
        res = []
        def dfs(crs, cur_path):
            if crs in cur_path:
                return False
            if crs in taken:
                return True
            
            cur_path.add(crs)

            for pre in g[crs]:
                if pre in taken:
                    continue
                if not dfs(pre, cur_path):
                    
                    return False
            
            
            taken.add(crs)
            res.append(crs)
            return True
            
        for crs in range(numCourses):
            dfs(crs, set())
        
        return res if len(taken) == numCourses else []
        