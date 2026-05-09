class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        pairs = {
            "]":"[",
            "}":"{",
            ")":"("
        }

        for ch in s:
            if ch not in pairs:
                # If open bracket, push
                stack.append(ch)
            else:
                # If close bracket, check and pop
                if not stack or stack[-1] != pairs[ch]:
                    return False
                stack.pop()
        return not stack