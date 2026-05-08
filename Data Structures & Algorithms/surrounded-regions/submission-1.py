class Solution:
    def solve(self, board: List[List[str]]) -> None:
        '''
        O -> X
        '''
        ROWS, COLS = len(board), len(board[0])

        
        q = deque()
        visited = set()

        for r in range(ROWS):
            if board[r][0] == "O":
                q.append((r,0))
                board[r][0] = "U"
            if board[r][COLS-1]=="O":
                q.append((r,COLS-1))
                board[r][COLS-1] = "U"
        for c in range(1,COLS-1):
            if board[0][c] == "O":
                q.append((0,c))
                board[0][c] = "U"
            if board[ROWS-1][c] == "O":
                q.append((ROWS-1,c))
                board[ROWS-1][c] = "U"
        
        
        def _is_valid(r,c):
            return 0<=r<ROWS and 0<=c<COLS and board[r][c] == "O"
        while q:
            r, c = q.popleft()
            for dr, dc in [(0,1), (0,-1), (1,0), (-1,0)]:
                nr, nc = r + dr, c + dc
                if _is_valid(nr,nc):
                    q.append((nr,nc))
                    board[nr][nc] = "U" # Unsurrounded
        
        
        for i in range(ROWS):
            for j in range(COLS):
                if board[i][j] == "U":
                    board[i][j] = "O"
                elif board[i][j] == "O":
                    board[i][j] = "X"
