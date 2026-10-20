class TimeMap:

    def __init__(self):
        self.kvs = {}
        self.times = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.kvs:
            self.kvs[key] = {timestamp: value}
            self.times[key] = [timestamp]
        elif timestamp not in (self.kvs[key]).keys():
            (self.kvs[key])[timestamp] = value
            (self.times[key]).append(timestamp)

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.kvs:
            return ""
        timestamps = self.times[key]
        idx = self.indexLessThanT(timestamps, timestamp)
        if idx == -1:
            return ""
        return (self.kvs[key]).get(idx)

    def indexLessThanT(self, tsp: List[int], t: int) -> int:
        L = 0
        R = len(tsp) - 1
        if tsp[L] > t:
            return -1
        while (L <= R):
            M = (L + R) // 2
            if t > tsp[M]:
                L = M + 1
            elif t < tsp[M]:
                R = M - 1
            else:
                return tsp[M]
        return tsp[R]