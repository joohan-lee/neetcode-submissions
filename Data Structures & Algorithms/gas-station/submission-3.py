class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        n = len(gas)
        diff = [g - c for g, c in zip(gas, cost)]
        total = sum(diff)

        if total < 0:
            return -1  # 전체 연료가 부족하므로 불가능

        # 누적합 구하기
        prefix = [0] * n
        prefix[0] = diff[0]
        for i in range(1, n):
            prefix[i] = prefix[i - 1] + diff[i]

        # 최소 누적합 찾기
        min_index = 0
        min_value = prefix[0]
        for i in range(1, n):
            if prefix[i] < min_value:
                min_value = prefix[i]
                min_index = i

        # 출발점은 그 다음 index (min_index + 1) % n
        return (min_index + 1) % n

