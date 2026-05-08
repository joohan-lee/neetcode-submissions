class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        # Way 1. Brute-Force: check all pairs (left, right) * min(heights[l:r])
        # Way 2. 
        # S = h * w 인데, 각 i에서 heights[i] 막대를 최소 높이로 하는 최대 직사각형은
        # i보다 왼쪽에서 처음으로 더 작은 막대 (L), 오른쪽에서 처음으로 더 작은 막대 (R)사이에서만 확장 가능.
        # 두 개의 단조 증가 스택에 인덱스를 저장하면서 왼쪽에서 더 작은 값이 나오는 인덱스, 오른쪽에서 더 작은 값이 나오는 인덱스를 구하고
        # 각각을 L, R 값으로 쓰고 현재 높이와 곱해서 면적의 최대를 찾는다.
        n = len(heights)
        stack = [] # monotonic increasing stack 
        left_idx = [-1] * n # (to store index where smaller value found to the left)
        right_idx = [n] * n # (to store index where smaller value found to the right)
        maxArea = 0

        for i in range(n):
            # 현재 값보다 더 큰 것은 팝
            while stack and heights[stack[-1]] > heights[i]:
                popped = stack.pop()
                right_idx[popped] = i

            stack.append(i)

        for i in range(n-1,-1,-1):
            # 현재 값보다 더 큰 것은 팝
            while stack and heights[stack[-1]] > heights[i]:
                popped = stack.pop()
                left_idx[popped] = i

            stack.append(i)
        
        # Get max area
        for i in range(n):
            R = right_idx[i]
            L = left_idx[i]
            maxArea = max(maxArea, heights[i] * (R-L-1))

        return maxArea