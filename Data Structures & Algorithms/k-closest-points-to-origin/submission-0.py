import math
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        closest = []
        clean = []
        for point in points:
            dist = math.dist(point, [0,0])
            heapq.heappush_max(closest, (dist, point))
        while len(closest) > k:
            heapq.heappop_max(closest)
        for d, p in closest:
            clean.append(p)
        return clean
