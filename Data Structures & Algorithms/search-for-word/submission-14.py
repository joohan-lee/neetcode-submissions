class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROWS = len(board)
        COLS = len(board[0])

        visited=set()
        def backtrack(i, r, c):
            # len(word) 모두 찾으면 true
            if i == len(word):
                return True
            
            # 경계, 방문, 문자 불일치 체크하여 early return (탐색 불필요)
            if (r < 0 or c < 0 or r >= ROWS or c >= COLS or
                board[r][c] != word[i] or (r,c) in visited):
                return False
            
            # 4방향 탐색
            visited.add((r,c))
            for dr, dc in [(0,1), (0,-1), (1,0), (-1,0)]:
                if backtrack(i+1, r+dr, c+dc):
                    return True
            # if all four directions was invalid, remove
            visited.remove((r,c))
            return False
            


        for r in range(ROWS):
            for c in range(COLS):
                if backtrack(0, r, c):
                    return True
        return False