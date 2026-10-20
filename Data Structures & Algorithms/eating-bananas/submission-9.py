class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        maxPile = (sorted(piles))[-1]
        L = 1
        R = maxPile
        bestSeen = R
        while (L <= R):
            M = (L + R) // 2
            result = 0
            for p in piles:
                result = result + -(-p // M)
                if result > h:
                    L = M + 1
                    break
            if result > h:
                L = M + 1
            elif result < h:
                bestSeen = min(bestSeen, M)
                R = M -1
            else:
                bestSeen = min(bestSeen, M)
                R = M - 1
        return bestSeen
            





        