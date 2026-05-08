class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum = nums[0]
        curr_sum = nums[0]
        for i in range(1,len(nums)):
            n = nums[i]
            if curr_sum + n < n:
                curr_sum = n
            else:
                curr_sum = curr_sum + n
            max_sum = max(max_sum, curr_sum)
        
        return max_sum

