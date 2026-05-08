class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        directions = [(0,1), (0,-1), (1,0), (-1,0)]
        def _is_valid(r, c):
            return 0<=r<len(grid) and 0<=c < len(grid[0]) and grid[r][c] == 1
        def bfs(i,j):
            q = deque([(i,j)])
            area = 0
            visited = set()
            while q:
                r,c = q.popleft()
                area += 1
                visited.add((r,c))
                for dr, dc in directions:
                    nr = r + dr
                    nc = c + dc
                    if _is_valid(nr,nc) and (nr,nc) not in visited:
                        q.append((nr,nc))
                        visited.add((nr,nc))
            
            return area


        N = len(grid)
        M = len(grid[0])
        max_size = 0
        for r in range(N):
            for c in range(M):
                if grid[r][c] == 1:
                    max_size = max(max_size, bfs(r,c))
        return max_size