class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # BFS
        directions = [(0,1),(0,-1),(1,0),(-1,0)]
        def bfs(i,j):
            q = deque([(i,j)])
            while q:
                r, c = q.popleft()

                for dr, dc in directions:
                    nr = r + dr
                    nc = c + dc
                    if 0<=nr<len(grid) and 0<=nc<len(grid[0]) and grid[nr][nc] == '1':
                        q.append((nr,nc))
                        grid[nr][nc]='0'

        
        
        res = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    bfs(i,j)
                    res += 1
        return res