class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ROWS, COLS = len(matrix), len(matrix[0])
        # Find the row
        l, r = 0, ROWS - 1
        row = -1
        while l <= r:
            mid = l + (r-l) // 2
            if matrix[mid][-1] < target:
                l = mid + 1
            elif matrix[mid][0] > target:
                r = mid - 1
            else:
                # Target exists in current row (mid row)
                row = mid
                break
        # print(f'{row=}')
        # Find the col
        l, r = 0, COLS - 1
        while l <= r:
            mid = l + (r-l) // 2
            if matrix[row][mid] == target:
                return True
            elif matrix[row][mid] > target:
                r = mid - 1
            else:
                l = mid + 1
        
        return False

