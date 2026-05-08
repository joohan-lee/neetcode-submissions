class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_idx = {}
        for i, n in enumerate(nums):
            complement = target - n
            if complement in num_idx:
                return [num_idx[complement], i]
            num_idx[n] = i