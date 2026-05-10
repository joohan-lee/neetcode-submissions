class Solution:
    def findMin(self, nums: List[int]) -> int:
        # [3,4,5,6,1,2]
        #     nums[mid] > nums[r] => l = mid + 1
        # [6,1,2,3,4,5]
        #   nums[l] > nums[mid] => r = mid
        # [1,2,3,4,5,6]
        #  nums[l] < nums[mid] < nums[r] => r = mid 
        # 
        l, r = 0, len(nums) - 1
        while l < r:
            mid = l + (r-l) // 2
            # print(f'!!{l=}, {r=}, {mid=}')
            if nums[mid] > nums[r]:
                l = mid + 1
            # elif nums[mid] <= nums[l]:
            else:
                r = mid # mid 자체가 최솟값일 수 있으므로 mid-1로 해서 후보 범위에서 제외하면 안됨. 
            # print(f'{l=}, {r=}, {mid=}')
        return nums[l]