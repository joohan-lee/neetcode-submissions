class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        '''
        놓아야하는 queen은 결국 n개.
        Qxxx  Qxxx
        xQxx  xQxx
        xxQx  xxxQ
        xxxQ  xxQx

        (0,0)   (0,1)   (0,2)   (0,3)
        |
(1,0)(1,1)..(1,3)           ...
    ...
    |
(3,0)...(3,3)
        이렇게 총 4^4 가지 방법 중에 맨 밑 level에 도달하면 snapshot찍어 res에 추가.
        '''
        res=[]
        board = [["."] * n for _ in range(n)]
        cols = set()
        posDiag = set() # / 모양의 대각선. 같은 대각선이면 r+c가 같음.
        negDiag = set() # \ 모양의 대각선. 같은 대각선이면 r-c가 같음.

        def backtrack(r):
            # 만약, 맨 밑 row까지 닿는다면 res에 추가.
            if r == n:
                res.append(["".join(row) for row in board])
                return
            
            # 현재 level(혹은 row)에서 놓을 수 있는 경우의 수는 컬럼의 수인 n가지.
            for c in range(n):
                # 위 level에서 놓은 queen과 경로가 겹치면 queen놓지않음.
                if (c in cols) or ((r+c) in posDiag) or ((r-c) in negDiag):
                    continue
                
                board[r][c] = "Q"
                # 현재 path를 기록.
                cols.add(c)
                posDiag.add(r+c)
                negDiag.add(r-c)

                # 다음 row 탐색.
                backtrack(r+1)

                board[r][c] = "."
                # 윗 level 다음 column 탐색 전에 이미 탐색한 path 삭제.
                cols.remove(c)
                posDiag.remove(r+c)
                negDiag.remove(r-c)

                

                
        
        backtrack(0)

        return res
        
        