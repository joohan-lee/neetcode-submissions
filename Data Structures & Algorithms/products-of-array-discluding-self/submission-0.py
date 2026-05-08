class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)

        left = [1 for _ in range(n)]
        right = [1 for _ in range(n)]
        
        cur_l = 1
        cur_r = 1
        for i in range(n):
            cur_l *= nums[i]
            cur_r *= nums[n-1-i]
            left[i] = cur_l
            right[n-1-i] = cur_r
        
        res = []
        for i in range(n):
            temp = 1
            temp *= left[i-1] if i-1 >= 0 else 1
            temp *= right[i+1] if i + 1 < n else 1
            res.append(temp)
        return res

        