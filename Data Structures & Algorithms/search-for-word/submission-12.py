class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROWS, COLS = len(board), len(board[0])

        def dfs(r, c, i, path):
            if i == len(word):
                return True
            if 0 > r or r >= ROWS or 0 > c or c >= COLS or (r,c) in path:
                return False
            if word[i] != board[r][c]:
                return False
            
            path.add((r,c))
            exist= (dfs(r + 1, c, i+1, path) or
                dfs(r-1, c, i+1, path) or
                dfs(r, c+1, i+1, path) or
                dfs(r, c-1, i+1, path)
            )
            path.remove((r,c))
            return exist


        for r in range(ROWS):
            for c in range(COLS):
                if dfs(r, c, 0, set()):
                    return True
        
        return False