class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()
        cur = self.toSum(n)
        while cur not in seen:
            if cur == 1:
                return True
            seen.add(cur)
            cur = self.toSum(cur)
        return False
        
    def toSum(self, n: int) -> int:
        toList = list(str(n))
        sumOfSq = 0
        for c in toList:
            digit = int(c)
            sumOfSq = sumOfSq + math.pow(digit, 2)
        return int(sumOfSq)



        