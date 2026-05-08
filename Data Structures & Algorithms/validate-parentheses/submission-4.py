class Solution:
    def isValid(self, s: str) -> bool:
        # {closed: open}
        pairs = {
            '}': '{',
            ']': '[',
            ')': '('
        }

        stack = []
        for ch in s:
            if ch not in pairs:
                stack.append(ch)
            else:
                if not stack or stack[-1] != pairs[ch]:
                    return False
                stack.pop()
        
        return True if not stack else False