class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if not nums:
            return [-1, -1]
        
        lower_bound = self.findLowerBound(nums, target)
        upper_bound = self.findUpperBound(nums, target)

        print(f'{lower_bound=}')
        print(f'{upper_bound=}')

        # if nums[lower_bound] == target -> return [lower, upper]
        # otherwise, return [-1, -1]
        if lower_bound >= len(nums) or nums[lower_bound] != target:
            return [-1, -1]
        return [lower_bound, upper_bound-1] 
    
    def findLowerBound(self, nums, target):
        l, r = 0, len(nums)

        while l < r:
            mid = l + (r-l) // 2

            if nums[mid] < target:
                l = mid + 1
            else:
                r = mid
        
        return l
    
    def findUpperBound(self, nums, target):
        l, r = 0, len(nums)

        while l < r:
            mid = l + (r-l) // 2

            if nums[mid] <= target:
                l = mid + 1
            else:
                r = mid
        
        return l