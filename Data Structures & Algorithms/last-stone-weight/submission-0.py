class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = stones
        heapq.heapify_max(stones)
        while len(heap) > 1:
            x = heapq.heappop_max(heap)
            y = heapq.heappop_max(heap)
            if x < y or y < x:
                newWeight = abs(y - x)
                heapq.heappush_max(heap, newWeight)
        return 0 if not heap else heap[0]

        