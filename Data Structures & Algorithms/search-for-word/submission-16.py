class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROWS, COLS = len(board), len(board[0])
        visited = set()
        def dfs(point, i):
            r, c = point
            if i == len(word):
                return True
            if not (0 <= r < ROWS) or not (0 <= c < COLS) or (board[r][c] != word[i]) or (r,c) in visited:
                return False
            
            visited.add((r,c))

            res= (
                dfs((r+1, c), i+1) or
                dfs((r-1,c), i+1) or
                dfs((r,c+1), i+1) or
                dfs((r,c-1), i+1)
            )

            visited.remove((r,c))
            return res

        for r in range(ROWS):
            for c in range(COLS):
                if dfs((r,c), 0):
                    return True
        return False