class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        maxPile = max(piles)
        L = 1
        R = maxPile
        bestSeen = R
        while (L < R):
            M = (L + R) // 2
            result = 0
            for p in piles:
                result = result + -(-p // M)
            if result <= h:
                R = M
            else:
                L = M + 1
        return L
            





        