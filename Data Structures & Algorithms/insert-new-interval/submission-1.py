class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        '''
        IDEA: 하나의 interval을 merge하면서 업데이트!
        1. 항상 newInterval처럼 merge할 하나의 interval을 만들어두고,
        merge가 가능한만큼 최대한 newInterval에 merge.
        2. 그리고, 그 뒤에 더 이상 merge가 안되면 res에 추가.
        '''
        
        n = len(intervals)
        res = []

        for i in range(n):
            # 새로 넣을 연장중인 newInterval의 끝이 더 이상 뒤와 겹치지 않으면, 나머지 넣고 return
            if newInterval[1] < intervals[i][0]:
                res.append(newInterval)
                return res + intervals[i:]
            # 새로 넣을 interval이 앞 interval과 겹치지 않을 때.
            elif newInterval[0] > intervals[i][1]:
                res.append(intervals[i])
            # 겹치는 부분이 있으면 newInterval에 겹치는 부분 없을 때까지 merge.
            else:
                newInterval[0] = min(newInterval[0], intervals[i][0])
                newInterval[1] = max(newInterval[1], intervals[i][1])
        
        # 마지막까지 다 merge된 경우, newInterval을 res에 넣어주기.
        res.append(newInterval)
        return res