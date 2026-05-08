class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_area = 0
        l, r = 0, len(heights) - 1
        while l < r:
            h_l, h_r = heights[l], heights[r]
            if h_l < h_r:
                l += 1
            else:
                r -= 1
            
            max_area = max(max_area, (r - l + 1) * min(h_l, h_r))
        return max_area