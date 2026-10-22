class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.heap = nums
        heapq.heapify_max(self.heap)
        self.k = k

    def add(self, val: int) -> int:
        if len(self.heap) == 0:
            self.heap.append(val)
        else:
            heapq.heappush_max(self.heap, val)
        kth = 0
        removed = []
        # pop kth largest
        for i in range(self.k):
            kth = heapq.heappop_max(self.heap)
            removed.append(kth)
        # restore popped values
        for r in removed:
            heapq.heappush_max(self.heap, r)
        return kth
