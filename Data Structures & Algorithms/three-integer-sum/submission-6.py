class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()

        res = []
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            
            pairs = self._twoSum(nums[i+1:], -nums[i])
            for a, b in pairs:
                res.append([nums[i], a, b])
        return res
    
    def _twoSum(self, nums, target):
        """nums are already sorted"""
        l, r = 0, len(nums) - 1
        pairs = set()
        while l < r:
            curr_sum = nums[l] + nums[r]
            if curr_sum == target:
                pairs.add((nums[l], nums[r]))
                l += 1
                r -= 1
            elif curr_sum > target:
                r -= 1
            else:
                l += 1
        return pairs

            