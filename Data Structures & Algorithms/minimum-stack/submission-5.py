class MinStack:

    def __init__(self):
        # Append Encoded value (val - min) to stack
        self.minVal = float('inf')
        self.stack = []

    def push(self, val: int) -> None:
        if not self.stack:
            self.stack.append(0)
            self.min = val
        else:
            self.stack.append(val - self.min) # val - min_old
            if self.min > val:
                # If new min was found, update min
                self.min = val

    def pop(self) -> None:
        if not self.stack:
            return
        
        popped = self.stack.pop()

        if popped < 0:
            # this means minimum was updated here.
            # since we stored (val - min) into stack,
            # popped = min_new(=current min) - min_old 
            # min_old = min_new(=current min) - popped
            # 그리고 여기서 current min은 더 작아서 업데이트된 val과 같다.
            curr_min = self.min
            self.min = curr_min - popped

    def top(self) -> int:
        # k = (val - min)을 저장하고 있으므로,
        # val = k + min을 리턴해야함.
        top = self.stack[-1]
        if top > 0:
            return top + self.min
        else:
            return self.min

    def getMin(self) -> int:
        return self.min
