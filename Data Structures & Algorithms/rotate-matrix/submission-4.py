from pprint import pprint
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Rotate By Four Cells
        """
        n = len(matrix)
        l, r = 0, n - 1

        # 홀수인 경우의 가운데를 위해 l==r인 경우 까지는 rotate 해줘야함.
        while l < r:
            for i in range(r-l): # [[1,2,3,4],...] 있다고 하면 1-3까지 3번 rotate필요.
                top, bottom = l, r # Square므로 같음. 0,3 -> 1,2

                # Rotate
                temp_topleft = matrix[top][l+i]

                # left-bottom -> top-left
                matrix[top][l+i] = matrix[bottom-i][l]
                # right-bottom -> left-bottom
                matrix[bottom-i][l] = matrix[bottom][r-i]
                # top-right -> right-bottom
                matrix[bottom][r-i] = matrix[top+i][r]
                # top-left -> top-right
                matrix[top+i][r] = temp_topleft

            l += 1
            r -= 1
