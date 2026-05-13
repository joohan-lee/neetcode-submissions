class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        """
            2
          /  |  \
         2   5   6 ...
        /|
       2 5
        """
        res = []
        def dfs(i, curr, total):
            # Base case
            # if sum == target -> append it to the result
            if total == target:
                res.append(curr.copy())
                return
            # if sum > target -> early return
            if total > target:
                return

            # Sum up
            # Traverse by iterating nums
            # to avoid duplicate, start from i
            for idx in range(i, len(nums)):
                curr.append(nums[idx])
                dfs(idx, curr, total + nums[idx])
                curr.pop()
        dfs(0, [], 0)
        return res