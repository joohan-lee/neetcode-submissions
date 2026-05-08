class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        # 왼쪽 가장 높은 것
        left_bounds = [0] * n 
        # 오른쪽 가장 높은 것
        right_bounds = [0] * n

        curr_max = 0
        for i in range(n):
            left_bounds[i] = curr_max = max(curr_max, height[i])
        
        curr_max = 0
        for i in range(n-1, -1, -1):
            right_bounds[i] = curr_max = max(curr_max, height[i])
        
        area = 0
        for i in range(n):
            h = min(left_bounds[i], right_bounds[i])
            area += (h - height[i])
        return area
        