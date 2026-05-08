class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # Kadane (DP)
        """
        정의
        maxDP[i] = nums[i]에서 끝나는 subarray의 최대 곱
        minDP[i] = nums[i]에서 끝나는 subarray의 최소 곱
        Base Case
        maxDP[0] = nums[0]
        minDP[0] = nums[0]
        재귀식
        maxDP[i] = max(nums[i], maxDP[i-1] * nums[i], minDP[i-1] * nums[i])
        minDP[i] = min(nums[i], maxDP[i-1] * nums[i], minDP[i-1] * nums[i])
        최종 답
        answer = max(maxDP[0], maxDP[1], ..., maxDP[n-1])
        """
        # keep track of the maximum product up to that number (we will call max_so_far) and minimum product up to that number (we will call min_so_far).
        # 음수 때문에 지금까지 최소값이 최대가 될수도, 지금까지 최대가 최소가 될수도 있다.
        n = len(nums)
        res = curr_min = curr_max = nums[0]
        for i in range(1, n):
            tmp_min = curr_min
            # 현재 nums[i]가 이전을 다 버리고 가장 작거나 클수도 있으니 함께 넣어 비교 필요.
            curr_min = min(nums[i], curr_min * nums[i], curr_max * nums[i])
            curr_max = max(nums[i], curr_max * nums[i], tmp_min * nums[i])
            res = max(res, curr_max)
            
        return res
