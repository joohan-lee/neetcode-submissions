class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = defaultdict(set)
        cols = defaultdict(set)
        boxes = defaultdict(set)

        for r in range(9):
            for c in range(9):
                elem = board[r][c]
                if elem == ".":
                    continue
                box_idx = (r//3) * 3 + c //3
                
                if elem in rows[r] or elem in cols[c] or elem in boxes[box_idx]:
                    return False

                rows[r].add(elem)
                cols[c].add(elem)
                boxes[box_idx].add(elem)
            
        return True