class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        def twoSum(arr, target):
            # Return two values
            l, r = 0, len(arr) - 1
            res = []
            while l < r:
                sm = arr[l] + arr[r]
                if sm == target:
                    res.append([arr[l], arr[r]])
                    l += 1
                    r -= 1
                elif sm < target:
                    l += 1
                else:
                    r -= 1
            return res
        
        nums.sort()
        res = set()
        for i in range(len(nums)):
            val = nums[i]
            if nums[i] > 0:
                break
            two_sums = twoSum(nums[i+1:], -val)
            for a, b in two_sums:
                res.add((val, a, b))
        
        return [list(t) for t in res]