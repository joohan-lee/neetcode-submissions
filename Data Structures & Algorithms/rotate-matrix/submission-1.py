from pprint import pprint
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        (0,0) -> (0,1) y++
        (0,1) -> (1,1) x++
        (1,0) -> (0,0) x--
        (1,1) -> (1,0) y--

        ====
        (0,0) -> (0,2) x+=0 y+=2
        (0,1) -> (1,2) x+=1 y+=1
        (0,2) -> (2,2) x+=2 y+=0
        (1,0) -> (0,1) x-=1 y+=1
        (1,1) -> (1,1) 
        (1,2) -> (2,1) x+=1 y-=1
        (2,0) -> (0,0) x-=2 
        (2,1) -> (1,0) x-=1 y-=1
        (2,2) -> (2,0) x-=0 y-=2

        규칙: (i, j) --rotation--> (j, (n-1)-i)
        """
        n = len(matrix)
        rotated = [[0] * n for _ in range(n)]
        # pprint(rotated)
        for i in range(n):
            for j in range(n):
                rotated[j][(n-1)-i] = matrix[i][j]
        
        for i in range(n):
            for j in range(n):
                matrix[i][j] = rotated[i][j]
        
        