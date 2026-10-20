class TimeMap:

    def __init__(self):
        self.kvs = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.kvs:
            self.kvs[key] = ([timestamp], [value])
        else:
            ((self.kvs[key])[0]).append(timestamp)
            ((self.kvs[key])[1]).append(value)

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.kvs:
            return ""
        timestamps = (self.kvs[key])[0]
        idx = self.indexLessThanT(timestamps, timestamp)
        return "" if idx == -1 else ((self.kvs[key])[1])[idx]

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
                return M
        return R
        
