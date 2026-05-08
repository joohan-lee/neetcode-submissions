class Solution:
    def findMin(self, nums: List[int]) -> int:
        # mid >= 0th and mid < last
        n = len(nums)

        l, r = 0, len(nums) - 1
        while l < r:
            mid = l + (r-l) // 2
            # 만약 가운데 값이 r값보다 크면 우측에 rotate point 있음을 의미. 즉, 우측으로 탐색.
            if nums[mid] > nums[r]:
                l = mid + 1
            # 아니면, 좌측으로 탐색.
            #   가운데 값이 r보다는 작으나, l보다도 작을 때 최소값은 좌측에 있음.
            #   [l,r] 모두 다 잘 정렬되어 있어도 작은 값은 좌측으로 탐색해야 함.
            else:
                r = mid
        
        return nums[l]
        

