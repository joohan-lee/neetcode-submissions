class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # way2. 포지션 순으로 정렬해두고, 도착하는데 걸리는 시간을
        # monotonic decreasing stack에 담으면 스택에 남아있는 elem 수가 car fleet 수.
        
        pairs = [(p, s) for p, s in zip(position, speed)]
        pairs.sort()

        stack = []
        for p, s in pairs:
            t = (target - p) / s # time from position to target
            # 스택에 현재 값보다 더 작거나 같은 값이 있으면 빼고, (감소 유지위해)
            while stack and stack[-1] <= t:
                stack.pop()
            # 현재 값을 항상 스택에 넣기.            
            stack.append(t)
        
        return len(stack)