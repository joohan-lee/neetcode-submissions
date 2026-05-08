class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # Way 1. Brute Force: O(n^2)
        # Way 2. Division: O(n)
        # Way 3. Prefix & Suffix
        n = len(nums)
        prefix = [1] * n
        suffix = [1] * n

        for i in range(1, n):
            prefix[i] = prefix[i-1] * nums[i-1]
            j = n-1-i
            suffix[j] = suffix[j+1] * nums[j+1]
        
        res = []
        for i in range(n):
            res.append(prefix[i] * suffix[i])
        
        return res