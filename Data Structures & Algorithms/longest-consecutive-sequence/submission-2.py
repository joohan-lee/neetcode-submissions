class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # Starting point가 될 수 있는 지점에서만 출발.
        numSet = set(nums)
        res = 0
        for i in range(len(nums)):
            num = nums[i]
            if (num - 1) not in numSet: # This means it can be a starting point for a sequence
                length = 1
                while (num + length) in numSet:
                    length += 1
                res = max(res, length)
        return res