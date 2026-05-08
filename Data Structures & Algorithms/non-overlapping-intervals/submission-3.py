class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: x[0])

        cur_interval = intervals[0]
        remove_cnt = 0
        for i in range(1, len(intervals)):
            # if overlap, remove longer one.
            if cur_interval[1] > intervals[i][0]:
                remove_cnt += 1
                cur_interval[1] = min(cur_interval[1], intervals[i][1])
            else:
                cur_interval = intervals[i]
        
        return remove_cnt