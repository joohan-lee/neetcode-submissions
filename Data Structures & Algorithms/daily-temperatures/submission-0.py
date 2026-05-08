class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []

        ans = [0] * len(temperatures)
        for i in range(len(temperatures)):
            t = temperatures[i]
            if not stack or stack[-1][0] >= t:
                stack.append((t, i))
            else:
                while stack and stack[-1][0] < t:
                    old_t, old_i = stack.pop()
                    ans[old_i] = i - old_i
                stack.append((t,i))
        
        return ans
            