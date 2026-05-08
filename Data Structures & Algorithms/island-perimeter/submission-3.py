class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        N, M = len(grid), len(grid[0])
        visited = set()
        
        def bfs(i,j):
            q = deque([(i,j)])
            visited.add((i,j))
            edges = 0

            while q:
                r, c = q.popleft()
                for dr, dc in [(0,1),(0,-1), (1,0),(-1,0)]:
                    nr = r + dr
                    nc = c + dc
                    if not (0<=nr<N and 0<=nc<M) or grid[nr][nc] == 0:
                        edges += 1
                    elif (nr,nc) not in visited and grid[nr][nc] == 1:
                        visited.add((nr,nc))
                        q.append((nr,nc))
            return edges
        
        for r in range(N):
            for c in range(M):
                if grid[r][c] == 1:
                    return bfs(r,c)
        return 0