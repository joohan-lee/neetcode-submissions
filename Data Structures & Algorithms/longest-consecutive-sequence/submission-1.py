class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        nums.sort()
        curr = 1
        res = 1
        for i in range(1,len(nums)):
            if nums[i-1] + 1 == nums[i]:
                curr += 1
            elif nums[i-1] == nums[i]:
                continue
            else:
                curr = 1
            res = max(res, curr)
        return res