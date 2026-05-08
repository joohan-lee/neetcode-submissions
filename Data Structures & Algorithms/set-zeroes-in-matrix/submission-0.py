class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        M = len(matrix)
        N = len(matrix[0])
        zero_rows = set()
        zero_cols = set()

        for r in range(M):
            for c in range(N):
                if matrix[r][c] == 0:
                    zero_rows.add(r)
                    zero_cols.add(c)
        
        for r in range(M):
            for c in range(N):
                if r in zero_rows or c in zero_cols:
                    matrix[r][c] = 0
        
        