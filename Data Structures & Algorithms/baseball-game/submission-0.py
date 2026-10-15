class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []
        result = 0
        for op in operations:
            print(stack)
            if op == '+':
                a = int(stack[-1])
                b = int(stack[-2])
                res = a + b
                stack.append(res)
            elif op == 'D':
                a = int(stack[-1])
                res = 2 * a
                stack.append(res)
            elif op == 'C':
                stack.pop()
            else:
                stack.append(op)
        
        for s in stack:
            result = result + int(s)
        
        return result
