class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        left_max = [0] * n # highest height from current to left end
        right_max = [0] * n # # highest height from current to right end

        # Get left max, right max
        curr_max = 0
        for i in range(1, n):
            curr_max = max(curr_max, height[i-1])
            left_max[i] = curr_max
        
        curr_max = 0
        for i in range(n-2, -1, -1):
            curr_max = max(curr_max, height[i+1])
            right_max[i] = curr_max
        # print(f'{left_max=}, {right_max=}')
        # Get area
        area = 0
        for i in range(n):
            area += max(min(left_max[i], right_max[i]) - height[i], 0)

        return area