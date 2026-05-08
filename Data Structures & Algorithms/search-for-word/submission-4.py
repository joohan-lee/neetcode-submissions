class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        '''
        1. iterate through all elements
        2. when first character is same, start dfs
        3. if found, return True, if not, continue to iterate.
        - 지금까지 path를 기록해야 왔던 방향으로는 안 갈 수 있음.
        '''
        def _is_valid_point(point):
            r, c = point
            return 0 <= r < len(board) and 0 <= c < len(board[0])

        def dfs(i,point, curr):
            if ''.join(curr) == word:
                return True
            if not _is_valid_point(point) or i >= len(word):
                return False
            r, c = point
            if word[i] != board[r][c] or (r,c) in path:
                return False
            
            path.add((r,c))
            curr.append(board[r][c])
            if (dfs(i+1, (r+1, c), curr) or
                dfs(i+1, (r, c+1), curr) or
                dfs(i+1, (r-1, c), curr) or
                dfs(i+1, (r, c-1), curr)):
                return True
            path.remove((r,c))
            curr.pop()

        path = set()
        n = len(board)
        m = len(board[0])
        for i in range(n):
            for j in range(m):
                if board[i][j] == word[0]:
                    path = set()
                    if dfs(0, (i,j), []):
                        return True
        return False
