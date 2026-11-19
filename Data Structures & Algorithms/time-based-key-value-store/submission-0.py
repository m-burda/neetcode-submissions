class TimeMap:

    def __init__(self):
        self.kv = collections.defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.kv[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        values = self.kv[key]
        l, r = 0, len(values) - 1

        res = ""

        while l <= r:
            m = (l + r) // 2

            ts, val = values[m]
            if ts > timestamp:
                r = m - 1
            else:
                res = val
                l = m + 1
        
        return res
