from bisect import bisect_left, bisect_right
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if not nums:
            return [-1, -1]
            
        left = bisect_left(nums, target)
        right = bisect_right(nums, target)

        if left < 0 or left >= len(nums) or nums[left] != target:
            return [-1, -1]

        return [left, right-1]