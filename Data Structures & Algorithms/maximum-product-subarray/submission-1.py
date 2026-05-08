class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        """
        prefix/suffix solution
        핵심 주장: 최대 곱 subarray는 반드시 한쪽 끝에 붙어있다 (0이 없을 때)
        반례를 만들어보려고 해봐. nums[1..3]이 최대라고 가정하면:
        nums = [?, nums[1], nums[2], nums[3], ?]
                ↑ 왼쪽에 뭔가 있음              ↑ 오른쪽에 뭔가 있음
        왼쪽의 nums[0]이 양수면? → nums[0..3]으로 확장하면 곱이 더 커짐 → 왼쪽 끝에 붙게 됨
        왼쪽의 nums[0]이 음수면? → 확장하면 부호 뒤집힘 → 확장 안 하는 게 나음
        그런데 확장 안 하면? → 그러면 오른쪽으로 확장을 생각해봐. 같은 논리로 오른쪽 끝까지 확장하거나 말거나. 결국 케이스를 나누면:
        전체 배열에 음수가 짝수개 → 전부 곱하면 양수 → 양쪽 끝 다 붙음
        전체 배열에 음수가 홀수개 → 하나를 잘라야 함:
        - 맨 왼쪽 음수 기준으로 오른쪽만 취함 → suffix에서 잡힘
        - 맨 오른쪽 음수 기준으로 왼쪽만 취함 → prefix에서 잡힘
        """
        n = len(nums)
        prefix = [1] * (n+1)
        suffix = [1] * (n+1)
        
        for i in range(n):
            prefix[i+1] = prefix[i] * nums[i]
            if prefix[i+1] == 0:
                # 0이 되면 그 뒤로 볼 때 다 0이되어 깨지니까 1로 리셋
                prefix[i+1] = 1
        
        for i in range(n-1, -1, -1):
            suffix[i] = suffix[i+1] * nums[i]
            if suffix[i] == 0:
                # 0이 되면 그 뒤로 볼 때 다 0이되어 깨지니까 1로 리셋
                suffix[i] = 1
        
        res = nums[0]
        for i in range(n):
            if nums[i] == 0:
                # nums[i] == 0 → 리셋된 유령 값 무시하고, 0 자체를 후보로
                res = max(res, 0)
            else:
                res = max(res, max(prefix[i+1], suffix[i]))

        return res
