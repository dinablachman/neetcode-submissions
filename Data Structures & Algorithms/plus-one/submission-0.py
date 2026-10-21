from collections import deque
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        q = deque(digits)
        cur = len(digits) - 1
        if digits[cur] != 9:
            digits[cur] = digits[cur] + 1
            return digits
        while q[cur] == 9:
            q[cur] = 0
            cur = cur - 1
        if cur < 0:
            q.appendleft(1)
        else:
            q[cur] = q[cur] + 1
        added = []
        for i in range(len(q)):
            added.append(q.popleft())
        return added