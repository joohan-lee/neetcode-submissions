class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        n = len(gas)
        start, end = n-1, 0
        tank = gas[start] - cost[start]
        while start > end:
            
            if tank < 0:
                # tank 연료가 부족하면 확장. (tank = sum(gas[start:end]) - sum(cost[start:end]))
                start -= 1
                tank += (gas[start] - cost[start])
            else:
                # tank 연료가 충분하면 end를 늘려 더 갈 수 있는지 보기.
                tank += (gas[end] - cost[end])
                end += 1 # 탱크는 항상 [start, end) 구간의 연료 상태를 반영하므로 end를 포함하지 않아 나중에 +1
        # clockwise로 도는게 정해져있으므로 start를 끝에서부터 시작해서 앞으로 더 확장하면서 찾는다.
        return start if tank >= 0 else -1

