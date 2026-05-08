def _arr():
    return [float('inf'),float('-inf')]
class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        """
        min idx, max idx로 각 letter 인터벌을 만들고 머지.
        각 인터벌의 길이가 output.
        """
        idx_map = defaultdict(_arr) # {ch: (min, max)}
        for i, ch in enumerate(s):
            idx_map[ch][0] = min(idx_map[ch][0], i)
            idx_map[ch][1] = max(idx_map[ch][1], i)
        
        intervals = list(idx_map.values())
        # print(f'{type(intervals)=}')
        intervals.sort()
        # print(f'{intervals=}')

        curr_interval = intervals[0]
        res = []
        for i in range(1, len(intervals)):
            if curr_interval[1] > intervals[i][0]:
                curr_interval[0] = min(curr_interval[0], intervals[i][0])
                curr_interval[1] = max(curr_interval[1], intervals[i][1])
            else:
                res.append(curr_interval[1] - curr_interval[0] + 1)
                curr_interval = intervals[i]
        res.append(curr_interval[1] - curr_interval[0] + 1)

        return res