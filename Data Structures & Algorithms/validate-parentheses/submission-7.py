from collections import deque
class Solution:
    def isValid(self, s: str) -> bool:
        pairings = {')': '(', '}': '{', ']': '['}
        stack = deque()

        for c in s:
            if c not in pairings.keys():
                stack.append(c)
            else:          
                if not stack or stack[-1] != pairings[c]:
                    return False
                stack.pop()

        return len(stack) == 0
