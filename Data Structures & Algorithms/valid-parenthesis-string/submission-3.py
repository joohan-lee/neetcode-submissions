class Solution:
    def checkValidString(self, s: str) -> bool:
        """
        "((**"
        "))**"
        "**))"
        "(*)"
        """
        stack = []
        star = []
        for i, ch in enumerate(s):
            if ch == "(":
                stack.append(i)
            elif ch == ")":
                if stack:
                    stack.pop()
                elif star:
                    star.pop()
                else:
                    return False
            elif ch == "*":
                star.append(i)
        
        # print(f'{star=}, {stack=}')
        while stack and star:
            # star가 남아있어도 "(" (left open parenthesis) 보다 앞에 있음 무용지물. (* 순서야함.
            if stack.pop() > star.pop():
                return False
        return not stack
