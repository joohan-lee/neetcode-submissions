class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1

        while l < r:
            mid = l + (r-l) // 2
            if nums[mid] > nums[r]: # point is in right
                l = mid + 1
            elif nums[mid] <= nums[l] or nums[l] < nums[r]: # point is in left
                r = mid
            # print(f'{l=}, {r=}, {mid=}')
            
        return nums[l]
        