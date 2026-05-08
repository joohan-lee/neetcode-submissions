class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        n = len(gas)
        for start in range(n):
            cur_gas = 0
            i = start
            is_possible = True
            for k in range(n):
                cur_gas += gas[i]
                cur_gas -= cost[i]
                i = (i+1) % n
                is_possible = (cur_gas >= 0)
                if not is_possible:
                    break
                
            cur_gas += gas[i]
            if is_possible:
                return start

        return -1