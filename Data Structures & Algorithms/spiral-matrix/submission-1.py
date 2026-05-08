class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        VISITED=-99999 # Invalid value
        m = len(matrix)
        n = len(matrix[0])

        directions = [(0,1), (1,0), (0,-1), (-1,0)] # right, down, left, up

        d = 0
        res = [matrix[0][0]]
        matrix[0][0] = VISITED
        r, c = 0, 0
        while len(res) < m * n:
            dr, dc = directions[d]
            nr, nc = r + dr, c + dc
            if 0 <= nr < m and 0 <= nc < n and matrix[nr][nc] != VISITED:
                # 갈 수 있으면 이동.
                res.append(matrix[nr][nc])
                matrix[nr][nc] = VISITED
                r, c = nr, nc
            else:
                # 못 가면 방향 전환.
                d = (d+1) % 4
        return res