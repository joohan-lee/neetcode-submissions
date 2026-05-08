class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        '''
        0 1 2 3 4 5
        7,1,7,2,2,4


        '''
        n = len(heights)
        
        # 왼쪽 가장 가까운 낮은 막대 idx using monotonic increasing stack
        leftMost = [-1] * n # -1이 idx 0보다 작다고 가정.
        stack = []
        for i in range(n):
            while stack and heights[stack[-1]] >= heights[i]:
                stack.pop()
            if stack:
                leftMost[i] = stack[-1]
            stack.append(i)

        # 오른쪽 가장 가까운 낮은 막대 idx
        stack = []
        rightMost = [n] * n
        for i in range(n-1, -1, -1):
            while stack and heights[stack[-1]] >= heights[i]:
                stack.pop()
            if stack:
                rightMost[i] = stack[-1]
            stack.append(i)

        # 각 idx의 높이를 갖는 최대 면적 계산
        maxArea = 0
        for i in range(n):
            leftMost[i] += 1 # 왼쪽에서 가장 가까운 더 작은 막대 다음 것부터 이용 가능.
            rightMost[i] -= 1 # 오른쪽에서 가장 가까운 더 작은 막대 이전 것부터 이용 가능.
            maxArea = max(maxArea, (rightMost[i] - leftMost[i] + 1) * heights[i])
        
        return maxArea

        # 그 중 최대 면적 return