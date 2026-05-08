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
        if key not in self.mp:
            return ""

        res = ""
        for v, t in self.mp[key]:
            if t <= timestamp:
                res = v
        return res
        
