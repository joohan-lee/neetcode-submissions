class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        ROWS = len(board)
        COLS = len(board[0])
        directions = [(0,1), (0,-1), (1,0), (-1,0)]
        

        def backtrack(i, point, curr):
            r, c = point
            # 종료 조건: 모든 문자 매칭 완료
            if i == len(word):
                return True
            
             # 경계, 방문, 문자 불일치 체크
            if (r < 0 or c < 0 or r >= ROWS or c >= COLS or
                board[r][c] != word[i] or (r,c) in visited):
                return False
            
            # 현재 위치 방문 표시
            visited.add(point)
            # 4방향 탐색
            for dr, dc in directions:       
                if backtrack(i+1, (r + dr, c + dc), curr):
                    return True
            # 백트래킹: 방문 표시 제거
            visited.remove(point)
            return False

        for r in range(ROWS):
            for c in range(COLS):
                visited = set()
                if backtrack(0, (r,c), []):
                    return True
        return False