class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # Way 1. Brute Force: O(n^2)
        # Way 2. Division: O(n)
        # Way 3. Prefix & Suffix: Time-O(n), Space-O(n)
        # Way 4. Prefix & Suffix: Time-O(n), Space-O(1)
        n = len(nums)
        res = [1] * n
        
        prefix = 1
        for i in range(1, n):
            res[i] = res[i-1] * nums[i-1]
        # print(f"{res=}")
        suffix = 1
        for j in range(n-2, -1, -1):
            suffix = suffix * nums[j+1]
            res[j] = res[j] * suffix
        
        return res