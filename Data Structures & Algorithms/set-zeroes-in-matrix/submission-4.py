class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        m = len(matrix)
        n = len(matrix[0])

        # O(1)으로 하기 또 다른 방법은 zero_rows, zero_cols를 따로 두지 않고,
        # 각 첫행, 첫 열을 해당 배열로 대신 사용하는 것.
        # 다만, (0,0) 포인트는 중복되므로 첫 row가 zero out될 것인지는 따로 변수를 이용.

        firstRowZero = False
        for r in range(m):
            for c in range(n):
                if matrix[r][c] == 0:
                    matrix[0][c] = 0 # 이러면 c열은 모두 zero out
                    if r > 0:
                        matrix[r][0] = 0 # 이러면 r행은 모두 zero out
                    else:
                        firstRowZero = True
        
        print(matrix)
        # column 기준 zero out - 단, 기준 값으로 쓰고 있는 첫 열은 아직 하면 안됨.
        # row 기준 zero out - 단, 기준 값으로 쓰고 있는 첫 행은 아직 하면 안됨.
        for r in range(1, m):
            for c in range(1, n):
                if matrix[0][c] == 0 or matrix[r][0] == 0:
                    matrix[r][c] = 0
        
        # 이제 첫 열을 업데이트
        if matrix[0][0] == 0:
            for r in range(m):
                matrix[r][0] = 0
        # 첫 행 업데이트
        if firstRowZero:
            for c in range(n):
                matrix[0][c] = 0
                