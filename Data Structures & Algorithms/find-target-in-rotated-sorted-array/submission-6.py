class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        while l <= r:
            mid = l + (r-l) // 2

            if nums[mid] == target:
                return mid
            """
            [3,4,5,6,1,2] => 오른쪽으로 갈 경우의 수 2개
            [5,6,1,2,3,4] => 왼쪽으로 갈 경우의 수 2개
            일단 pivot이 있을 수 있는 가능한 두 경우의 수로 나누고,
            그 안에서 각 2개의 경우의 수 나누기.

            """
            # If pivot is in right,
            if nums[mid] > nums[r]:
                # target이 mid보다 크거나, target이 우측에 있음이 확실하면=>우측 탐사
                if target > nums[mid] or target < nums[l]:
                    l = mid + 1
                # 아니면 좌측 탐사
                else:
                    r = mid - 1
            else: # If pivot is in left or at mid,
                # target이 mid보다 작거나 target이 왼쪽에 있음이 확실하면=> 현재 및 좌측탐사
                if target < nums[mid] or target > nums[r]:
                    r = mid - 1
                # 아니면 우측 탐사
                else:
                    l = mid + 1
        
        return -1
