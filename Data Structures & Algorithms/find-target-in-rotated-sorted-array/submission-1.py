class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # right side of mid
        #   mid < target and 0th < mid
        #   mid > target and last > target
        #   => l = mid + 1
        # left side of mid
        #   mid > target and 0th < mid 
        #   mid < target and 0th < target
        #   => r = mid - 1
        
        l, r = 0, len(nums) - 1
        # [1] 이렇게 하나만 있을 때도 여전히 비교해야 하므로 <= operator
        while l <= r:
            mid = l + (r-l) // 2
            # print(f'{l=}, {r=}, {mid=}')
            if nums[mid] == target:
                return mid
            
            # mid가 left sorted portion에 속한 경우.
            # l == mid 일 수도 있으므로 equal sign
            if nums[l] <= nums[mid]:
                if target > nums[mid]:
                    l = mid + 1
                elif target < nums[l]: # target이 mid값보다는 작지만 l보다도 작으면 우측을 봐야함. 
                    l = mid + 1
                else: # target이 nums[mid] 보다 작고 l보다는 크면 좌측.
                    r = mid - 1
            else:
                if target < nums[mid]:
                    r = mid - 1
                elif target > nums[r]:
                    r = mid - 1
                else:
                    l = mid + 1
        return -1