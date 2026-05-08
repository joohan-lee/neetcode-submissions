class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        m = len(matrix)
        n = len(matrix[0])
        zero_rows = set()
        zero_cols = set()

        # Check rows
        for r in range(m):
            is_row_zero = False
            for c in range(n):
                if matrix[r][c] == 0:
                    is_row_zero = True
                    break
            if is_row_zero:
                for c in range(n):
                    if matrix[r][c] != 0:
                        matrix[r][c] = float('inf')
        
        # Check cols
        for c in range(n):
            is_col_zero = False
            for r in range(m):
                if matrix[r][c] == 0:
                    is_col_zero = True
                    break
            if is_col_zero:
                for r in range(m):
                    if matrix[r][c] != 0:
                        matrix[r][c] = float('inf')
        
        # Return all inf to zero
        for r in range(m):
            for c in range(n):
                if matrix[r][c] == float('inf'):
                    matrix[r][c] = 0
        
