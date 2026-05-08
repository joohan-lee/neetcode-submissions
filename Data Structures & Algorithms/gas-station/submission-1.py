class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        '''
        [1,2,3,4,5]
        [3,4,5,1,2]
        [-2,-2,-2,3,3]

        [4,2,3,1,5]
        [1,4,5,3,2]
        [3,-2,-2,-2,3]
        '''
        if sum(gas) < sum(cost):
            return -1
        
        total = 0
        start = 0
        for i in range(len(gas)):
            total += (gas[i] - cost[i])

            # total이 마지막으로 음수였던 곳 다음이 무조건 전체 gas가 양수가 되도록하는 시작점이다.
            if total < 0:
                total = 0
                start = i + 1
        return start