class MinStack:

    def __init__(self):
        self.stack = []
        self.min_stack = [] # This is to keep track of minimum values

    def push(self, val: int) -> None:
        """
        Sliding window 개념처럼 stack은 순차적으로 쌓아가기때문에 더 작은 것을 발견할 때만 push 가능.
        """
        self.stack.append(val)
        if not self.min_stack or self.min_stack[-1] >= val:
            self.min_stack.append(val)

    def pop(self) -> None:
        if self.min_stack and self.min_stack[-1] == self.stack[-1]:
            self.min_stack.pop()
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1] # if self.stack else None

    def getMin(self) -> int:
        return self.min_stack[-1] # if self.min_stack else None

        
