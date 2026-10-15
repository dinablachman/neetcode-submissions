import re
from collections import deque
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        result = 0
        if (len(tokens) == 1):
            return int(tokens[0])

        for i in range(len(tokens)):
            s = tokens[i]
            if s == '+' or s == '-' or s == '*' or s == '/':
                if not stack:
                    return result
                first = int(stack[-2])
                second = int(stack[-1])
                if s == '+':
                    result = first + second
                elif s == '-':
                    result = first - second
                elif s == '*':
                    result = first * second
                elif s == '/':
                    result = int(first / second)
                stack.pop()
                stack.pop()
                stack.append(result)
            else:
                stack.append(s)
            
        return result
        