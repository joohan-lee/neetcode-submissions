class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        # dfs 아이디어는 닛코드 풀이를 참고함.
        N, M = len(grid), len(grid[0])
        visited = set()

        def dfs(i, j):
            if not (0 <= i < N and 0 <= j < M) or grid[i][j] == 0:
                # island의 perimeter edge찾음.
                return 1
            if (i,j) in visited:
                return 0
            
            visited.add((i, j))

            edges = 0
            edges += dfs(i+1, j)
            edges += dfs(i, j+1)
            edges += dfs(i-1, j)
            edges += dfs(i, j-1)
            
            return edges
        
        res = 0
        for r in range(N):
            for c in range(M):
                if grid[r][c] == 1:
                    # land를 찾았을 때 dfs.
                    # 랜드로부터 dfs/bfs를 해서 밖으로 넘어갈 때 edge를 하나 찾음.
                    # 즉, bfs해보면서 perimeter를 언제 찾을 수 있나 고민해보면 됨.
                    res += dfs(r,c)
        return res