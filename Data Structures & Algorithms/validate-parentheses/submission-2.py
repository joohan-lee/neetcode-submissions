class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        bracket_map = {
            "]" : "[",
            "}" : "{",
            ")" : "("
        }

        for ch in s:
            if ch == "[" or ch == "{" or ch == "(":
                stack.append(ch)
                continue
            
            if stack:
                b = stack.pop()
                if b != bracket_map[ch]:
                    return False
            else:
                return False
        
        return True if not stack else False