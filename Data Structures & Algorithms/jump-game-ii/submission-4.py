class Solution:
    def jump(self, nums: List[int]) -> int:
        cur_end = 0      # 현재 점프 범위의 끝 (이 범위를 넘으면 점프 필요)
        cur_far = 0      # 현재까지 도달할 수 있는 가장 먼 위치
        jumps = 0        # 점프 횟수

        # 마지막 인덱스는 도착지점이므로, 거기선 점프할 필요 없음
        for i in range(len(nums) - 1):
            # 현재 위치에서 도달 가능한 최장 거리 갱신
            cur_far = max(cur_far, i + nums[i])

            # 현재 범위의 끝에 도달한 경우:
            # 더 멀리가려면 무조건적으로 점프를 해야하는 지점임.
            # 더 멀리 가기 위해 점프 횟수 증가, 다음 점프 범위를 cur_far로 확장
            if i == cur_end:
                jumps += 1
                cur_end = cur_far  # 점프한 이후 새 범위 설정

        return jumps
