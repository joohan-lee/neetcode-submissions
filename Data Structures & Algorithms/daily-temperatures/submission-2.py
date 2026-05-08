from typing import List

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        ans = [0] * n

        # stack에는 "인덱스"만 저장
        # temperatures[stack] 를 보면 스택이 유지되는 동안
        # 위로 갈수록 더 "따뜻한 후보"가 남게끔(pop을 통해) 정리됨
        stack = []

        # 오른쪽 -> 왼쪽 스캔
        for i in range(n - 1, -1, -1):
            # 현재 온도보다 "따뜻하지 않은"(<=) 것들은 다음 warmer day가 될 수 없으므로 제거
            while stack and temperatures[stack[-1]] <= temperatures[i]:
                stack.pop()

            # 스택이 남아있으면, 그 top이 "가장 가까운 다음 더 따뜻한 날"
            # 그 남아있는 값은 현재 온도보다는 따뜻한 더 미래의 어떤 날이었을 것.
            if stack:
                ans[i] = stack[-1] - i  # 거리(며칠 뒤)

            # 현재 인덱스를 후보로 push
            stack.append(i)

        return ans
