class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        N, M = len(board), len(board[0])
        def backtrack(i, r, c, curr):
            print(f'{i=}, {r=}, {c=}, {curr=}')
            
            if (r,c) in visited:
                return False
            if curr == word:
                print(f'{curr=}, {word=}')
                return True
            if (i > len(word) or r < 0 or r >= N or c < 0 or c >= M
                or word[i] != board[r][c]):
                return False
            
            visited.add((r,c))

            ret = (backtrack(i+1, r+1, c, curr + board[r][c])
            or backtrack(i+1, r, c+1, curr + board[r][c])
            or backtrack(i+1, r-1, c, curr + board[r][c])
            or backtrack(i+1, r, c-1, curr + board[r][c]))

            visited.remove((r,c))
            return ret

            
        
        for i in range(N):
            for j in range(M):
                if board[i][j] == word[0]:
                    visited = set()
                    if backtrack(0, i,j, ""):
                        return True
        
        return False