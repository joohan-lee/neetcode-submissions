class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [0] * 9 # 각 row당 9개의 비트를 써서 각 row에서 9개의 숫자 중 무엇이 나왔었는지 확인.
        cols = [0] * 9
        boxes = [0] * 9

        for r in range(9):
            for c in range(9):
                if board[r][c] == ".":
                    continue
                
                val = int(board[r][c]) - 1 # 1-9 => 0-8
                box_idx = (r//3)*3 + c//3

                # 체크: val번째 비트가 켜져있나?
                if (1 << val) & rows[r]:
                    # val = 3일 때, 이미 3 나온적 있으면 아래 처럼 0이 아니게 됨.
                    # (000001000) & (000001000)
                    return False
                if (1 << val) & cols[c]:
                    return False
                
                if (1 << val) & boxes[box_idx]:
                    return False

                rows[r] = rows[r] | (1 << val)
                cols[c] = cols[c] | (1 << val)
                boxes[box_idx] = boxes[box_idx] | (1 << val)
            
        return True

"""
[비트연산 패턴]

# 체크: k번째 비트가 켜져있나?
if mask & (1 << k):

# 켜기: k번째 비트 ON
mask |= (1 << k)

# 끄기: k번째 비트 OFF  
mask &= ~(1 << k)

# 토글: k번째 비트 반전
mask ^= (1 << k)
"""