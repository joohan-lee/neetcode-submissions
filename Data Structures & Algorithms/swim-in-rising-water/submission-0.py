class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        M, N = len(grid), len(grid[0])
        cost = [[float('inf')] * M for _ in range(N)] # max cost on the path so far
        cost[0][0] = grid[0][0]

        min_heap = [(grid[0][0], (0,0))] # (거리, 노드)

        while min_heap:
            # 1. 가장 가까운 노드 꺼내기
            curr_cost, curr_node = heapq.heappop(min_heap)
            r, c = curr_node

            # 2. 이미 처리된 노드 스킵
            if curr_cost > cost[r][c]:
                continue
            
            # 3. 인접 노드 탐색 및 거리 갱신
            for dr, dc in [(0,1), (0,-1), (1,0), (-1,0)]:
                nr = r + dr
                nc = c + dc
                if 0 <= nr < M and 0 <= nc < N and max(curr_cost, grid[nr][nc]) < cost[nr][nc]:
                    cost[nr][nc] = max(curr_cost, grid[nr][nc])
                    heapq.heappush(min_heap, (max(curr_cost, grid[nr][nc]), (nr, nc)))
        
        return cost[M-1][N-1]