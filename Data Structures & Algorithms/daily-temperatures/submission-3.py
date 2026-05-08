class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # stack에는 실제 temperature가 줄어드는 인덱스를 저장.
        # 앞에서 뒤로 순회하면서 더 큰 온도를 찾으면 스택의 인덱스와 현재 인덱스의 거리를 결과 배열에 저장.
        n = len(temperatures)
        stack = []
        res = [0] * n

        for i in range(n):
            while stack and temperatures[stack[-1]] < temperatures[i]:
                idx = stack.pop()
                res[idx] = i - idx
            stack.append(i)
        
        return res
            