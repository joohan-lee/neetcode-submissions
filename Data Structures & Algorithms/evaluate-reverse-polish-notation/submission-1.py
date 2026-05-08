class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        # 숫자는 push, operands만나면 두개 꺼내서 계산 후 push
        operations = {
            "+": lambda x,y: x + y, 
            "-": lambda x,y: x - y,
            "*": lambda x,y: x * y, 
            "/": lambda x,y: int(x / y)
        }
        stack = []

        for t in tokens:
            if t not in operations:
                stack.append(int(t))
            else:
                n1 = stack.pop()
                n2 = stack.pop()
                res = operations[t](n2, n1)
                stack.append(res)
        
        return stack[-1]
        


