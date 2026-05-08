class TimeMap:

    def __init__(self):
        # {key: [(value, timestamp), ...] }
        self.mp = {} 

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.mp:
            self.mp[key] = [(value, timestamp)]
        else:
            self.mp[key].append((value, timestamp))

    def get(self, key: str, timestamp: int) -> str:
        # 항상 timestamp 순으로 set됨이 정해져있으므로 timestamp는 sorted상태. => binary search 가능.
        if key not in self.mp:
            return ""

        res = ""
        l, r = 0, len(self.mp[key]) - 1
        
        while l <= r:
            mid = l + (r-l) // 2
            value, curr_time = self.mp[key][mid]
            if curr_time > timestamp:
                r = mid - 1
            else:
                l = mid + 1
        return self.mp[key][r][0] if r >=0 else ""
