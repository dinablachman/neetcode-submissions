from collections import deque
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        output = [0] * len(temperatures)
        stack = deque()
        for i in range(len(temperatures)):
            if not stack:
                stack.append((i, temperatures[i]))
            else:
                current_temp = temperatures[i]
                last_index, last_temp = stack[-1]
                if current_temp < last_temp:
                    stack.append((i, temperatures[i]))
                else:
                    while(stack and stack[-1][1] < current_temp):
                        popped_index, popped_temp = stack.pop()
                        output[popped_index] = i - popped_index
                    stack.append((i, temperatures[i]))
        return output

        