class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # [3,4,5,6,1,2] - left sorted - nums[l] <= nums[mid]
        #   target < nums[mid] and target >=nums[l] -> left. else left
        # [5,6,1,2,3,4] - right sorted - nums[mid] < nums[r]
        #   target > nums[mid] and target <= nums[r] -> right. else left
        # [1,2,3,4,5,6] - both sorted
        l, r = 0, len(nums) - 1
        while l <= r:
            mid = l + (r-l) // 2
            # print(f'!!{l=}, {r=}, {mid=}')
            if target == nums[mid]:
                return mid
            elif nums[l] <= nums[mid]: # left sorted
                if target < nums[mid] and target >= nums[l]:
                    r = mid - 1
                else:
                    l = mid + 1
            elif nums[mid] < nums[r]:
                if target > nums[mid] and target <= nums[r]:
                    l = mid + 1
                else:
                    r = mid - 1
            # print(f'{l=}, {r=}, {mid=}')
        
        return -1

