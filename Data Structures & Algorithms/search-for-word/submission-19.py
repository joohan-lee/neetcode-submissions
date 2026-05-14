class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        # Clarification:
        # - can have both upper & lower? if so, case-sensitive comparison?
        # - can board empty?
        # - can word be empty?
        ROWS, COLS = len(board), len(board[0])
        def backtrack(i,j,cur_idx):
            # Termination condition: all chars matched
            if cur_idx == len(word):
                return True
            # Check border, visited, char match
            if not (0 <= i < ROWS
                and 0 <= j < COLS
                and word[cur_idx] == board[i][j]
                and (i,j) not in visited):
                return False
            # Mark as visit
            visited.add((i,j))
            # travers 4-way
            for dr, dc in [(0,1), (0,-1), (1,0),(-1,0)]:
                if backtrack(i+dr, j+dc, cur_idx + 1):
                    return True
            # backtrack: remove visited
            visited.remove((i,j))
            return False
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                visited = set()
                if backtrack(i,j,0):
                    return True
        return False
        