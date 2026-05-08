class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # Sort position along with original index
        sorted_position = sorted([(pos, idx) for idx, pos in enumerate(position)])

        # 실제 걸리는 시간 계산
        took_hours = []
        for pos, idx in sorted_position:
            dist = target - pos
            s = speed[idx]
            took_hours.append(dist/s)
        
        # Monotonic decreasing stack 수 = fleet 수
        # 앞에 있는 차가 더 빨리 도착하기로 되어있으면, fleet 됨.
        stack = []
        for i, h in enumerate(took_hours):
            if not stack or h < stack[-1]:
                stack.append(h)
            else:
                while stack and h >= stack[-1]:
                    stack.pop()
                stack.append(h)
        return len(stack)