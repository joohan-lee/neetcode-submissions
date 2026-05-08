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
        i=0

        # Find the position where merge begins
        while i < n and newInterval[0] > intervals[i][1]:
            res.append(intervals[i])
            i += 1
        
        # Merge
        while i < n and newInterval[1] >= intervals[i][0]:
            newInterval[0] = min(newInterval[0], intervals[i][0])
            newInterval[1] = max(newInterval[1], intervals[i][1])
            i += 1
        res.append(newInterval)

        # Rest
        while i < n:
            res.append(intervals[i])
            i += 1
        
        return res



        

                    