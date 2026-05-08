class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m = len(matrix)
        n = len(matrix[0])

        res = []
        # 각 방향 경계선
        top, bottom = 0, m - 1
        left, right = 0, n - 1

        while left <= right and top <= bottom:
            # 1. To right
            for c in range(left, right + 1):
                res.append(matrix[top][c])
            top += 1 # 맨 윗줄 넣었으니 top 경계선 아래로 이동.

            # 2. To bottom
            for r in range(top, bottom+1):
                res.append(matrix[r][right])
            right -= 1 # 우측 경계선 넣었으니 좌측으로 이동.

            # 3. To left
            if top <= bottom: # 행이 존재하면 넣기.
                for c in range(right, left-1, -1):
                    res.append(matrix[bottom][c])
                bottom -= 1 # 아래 경계선 넣었으니 위로 이동.

            # 4. To top
            if left <= right: # 왼쪽 열이 존재하면 넣기.
                for r in range(bottom, top-1, -1):
                    res.append(matrix[r][left])
                left += 1 # 좌측 경계선 넣었으니 우측으로 줄이기.
        
        return res
            
