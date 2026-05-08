class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []

        for i in range(len(intervals)):
                
            if intervals[i][0] <= newInterval[1] and intervals[i][1] >= newInterval[0]:
                # 1. merge 필요할 때.
                # 겹치는건 두 가지 만족되어야.
                #     4----------10
                #   2----5
                # 1----3
                #    2-----5
                newInterval[0] = min(intervals[i][0], newInterval[0])
                newInterval[1] = max(intervals[i][1], newInterval[1])
            elif intervals[i][1] < newInterval[0]:
                # 2. merge 필요 없을 때
                res.append(intervals[i])
            elif intervals[i][0] > newInterval[1]:
                # 2. newInterval 이후 merge 필요 없을 때, newInterval 넣어주기.
                res.append(newInterval)
                return res + intervals[i:]
                
        # 마지막까지 다 merge된 경우, newInterval을 res에 넣어주기.
        res.append(newInterval)
        return res
