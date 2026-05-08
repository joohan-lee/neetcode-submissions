class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0])
        print(f'{intervals=}')
        interval = intervals[0]

        res = []
        for i in range(1, len(intervals)):
            if interval[1] < intervals[i][0]:
                res.append(interval)
                interval = intervals[i]
            else:
                interval[0] = min(interval[0], intervals[i][0])
                interval[1] = max(interval[1], intervals[i][1])
        res.append(interval)
        return res