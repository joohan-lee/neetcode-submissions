class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        '''
        [(0,1), (1,2), (1,3), (2,1)]
        2->1->0
           ^
           |
           3
        [(0,1), (1,2), (1,3), (2,0)]
        1->0
        2->1->0
           3
        0->2->1
              3
        '''

        preMap = {i:[] for i in range(numCourses)}
        for crs, pre in prerequisites:
            preMap[crs].append(pre)

        # visitSet = all courses along the current DFS path
        visitSet = set() # Keep track of visited nodes(path)
        def dfs(crs):
            # If crs was already in current DFS path
            if crs in visitSet:
                return False
            if len(preMap[crs]) == 0: # if the leaf node, able to take
                return True

            visitSet.add(crs) # 방문처리
            # 후 neighbors
            for pre in preMap[crs]:
                if not dfs(pre):
                    return False
            visitSet.remove(crs) # 이미 방문한 노드는 방문 요소에서 제거.
            preMap[crs] = [] # 이미 방문한 노든는 엣지 제거.

            return True

        
        for c in preMap:
            if not dfs(c):
                return False
        return True