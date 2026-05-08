class MinStack:

    def __init__(self):
        # Stack
        self.stack = []
        # Monotonic decreasing stack to keep minimum
        self.minStack = []

    def push(self, val: int) -> None:

        if not self.minStack or self.minStack[-1] > val:
            self.minStack.append(val)
        else:
            self.minStack.append(self.minStack[-1])
        
        # Append to the stack
        self.stack.append(val)

    def pop(self) -> None:
        self.minStack.pop()
        return self.stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minStack[-1]
