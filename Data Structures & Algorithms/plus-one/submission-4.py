from collections import deque
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        s = set(digits)
        cur = len(digits) - 1
        if 9 not in s:
            digits[cur] = digits[cur] + 1
            return digits

        if digits[cur] != 9:
            digits[cur] = digits[cur] + 1
            return digits

        while digits[cur] == 9:
            digits[cur] = 0
            cur = cur - 1

        if cur < 0:
            q = deque(digits)
            q.appendleft(1)
            digits.clear()
            for i in range(len(q)):
                digits.append(q.popleft())
        else:
            digits[cur] = digits[cur] + 1

        return digits