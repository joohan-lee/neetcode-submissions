class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # Monotonic decreasing stack
        stack = []
        res = [0] * len(temperatures) # store idx of next warmer (higher)

        for i in range(len(temperatures)):
            t = temperatures[i]
            if not stack or temperatures[stack[-1]] >= t:
                stack.append(i)
            else:
                while stack and temperatures[stack[-1]] < t:
                    curr = stack.pop()
                    res[curr] = i - curr
                stack.append(i)
        return res