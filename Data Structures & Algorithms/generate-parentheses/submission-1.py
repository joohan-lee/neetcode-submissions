class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        def backtrack(i, curr, open, close):
            if i > 2*n or open < close:
                return
            
            if open == close == n:
                res.append("".join(curr))
                return
            
            if open < n:
                curr.append("(")
                backtrack(i+1, curr, open+1, close)
                curr.pop()
            if open > close:
                curr.append(")")
                backtrack(i+1, curr, open, close + 1)
                curr.pop()
        backtrack(0, [], 0, 0)
        return res