class Solution:
    def canJump(self, nums: List[int]) -> bool:
        """
        이 문제에서 Greedy 시그널
        시그널이 문제에서
        한 방향 진행 | 왼쪽 → 오른쪽만 (되돌아갈 필요 없음)
        선택이 미래를 망치지 않음 | 더 멀리 갈 수 있으면 무조건 이득
        상태가 단순함 | "최대 도달 범위" 숫자 하나로 충분
        가능 여부만 물어봄 | 경로 추적 불필요 → 단순화 가능
        """
        # Greedy
        can_reach = nums[0]

        for i in range(1, len(nums)-1):
            # 현재 지점에서 local optimal을 찾아나가다보면 global optimal 찾을 수 있음.
            if can_reach >= i:
                can_reach = max(can_reach, i + nums[i])
        
        return can_reach >= (len(nums) -1)