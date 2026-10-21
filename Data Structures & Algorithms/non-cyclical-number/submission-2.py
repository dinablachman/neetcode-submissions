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
        output = 0
        while n > 0:
            last = n % 10
            output = output + pow(last, 2)
            n //= 10
        return output       