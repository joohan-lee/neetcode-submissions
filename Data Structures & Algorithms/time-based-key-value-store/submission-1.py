class TimeMap:

    def __init__(self):
        self.time_map = {} # key: list of (value, time)

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.time_map:
            self.time_map[key] = [(value, timestamp)]
        self.time_map[key].append((value, timestamp))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.time_map:
            return ""
        
        search_arr = self.time_map[key]
        l, r = 0, len(search_arr) - 1

        while l <= r:
            mid = l + (r-l) // 2
            val, prev_time = search_arr[mid]
            if prev_time <= timestamp:
                l = mid + 1
            else:
                r = mid - 1
            
        return search_arr[r][0] if r >= 0 else ""
        
