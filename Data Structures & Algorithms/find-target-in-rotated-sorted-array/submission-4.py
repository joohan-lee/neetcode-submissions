class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        # Binary search. If found, return index
        l, r = 0, len(nums) - 1
        while l <= r:
            mid = l + (r-l) // 2

            if nums[mid] == target:
                return mid
            
            if nums[mid] < target:
                # pivot is in left side.
                if nums[mid] < nums[l] and nums[l] <= target:
                    r = mid - 1
                # pivot이 오른쪽에 있으면 무조건 right로 가면됨. 혹은, pivot이 좌측이어도 target이 nums[l]보다 크지 않으면 우측으로.
                # (이는 우측 절반이 정렬되있음이 보장될 때와 mid보다 큰 값이 그럼에도 좌측에 있을때)
                else:
                    l = mid + 1
            elif nums[mid] > target:
                # if pivot is in right side
                if nums[r] < nums[mid] and nums[r] >= target:
                    l = mid + 1
                # pivot이 왼쪽에 있으면 무조건 left로 가면됨. 혹은, pivot이 우측이어도 target이 nums[r]보다 크면 왼쪽으로.
                else:
                    r = mid - 1
                
        return -1