class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # Way 1. Brute Force: O(n^2)
        # Way 2. Division: O(n)
        # Way 3. Prefix & Suffix: Time-O(n), Space-O(n)
        # Way 4. Prefix & Suffix: Time-O(n), Space-O(1)
        # n = len(nums)
        # prefix = [1] * (n+1)
        # suffix = [1] * (n+1)

        # for i in range(n):
        #     prefix[i+1] = prefix[i] * nums[i]
        #     j = n-1-i
        #     suffix[j] = suffix[j+1] * nums[j]    
        
        # res = []
        # for i in range(n):
        #     res.append(prefix[i] * suffix[i+1])
        # return res

        n = len(nums)
        prefix = 1
        res = []
        for i in range(n):
            prefix *= nums[i-1] if i-1>=0 else 1
            res.append(prefix)
        suffix = 1
        for i in range(n-1, -1, -1):
            suffix *= nums[i+1] if i + 1 < n else 1
            res[i] = suffix*res[i]

        return res