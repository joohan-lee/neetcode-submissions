class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # way1. brute-force
        # way2. 포지션 순으로 정렬해두고, 도착하는데 걸리는 시간을
        # monotonic decreasing stack에 담으면 스택에 남아있는 elem 수가 car fleet 수.
        
        pairs = [(p, s) for p, s in zip(position, speed)]
        pairs.sort()

        stack = []
        for p, s in pairs:
            t = (target - p) / s # time from position to target
            # 더 큰거나 같은 값을 stack에서 빼고,
            while stack and stack[-1] <= t:
                stack.pop()
            # 현재 값을 스택에 넣기.            
            stack.append(t)
        
        return len(stack)