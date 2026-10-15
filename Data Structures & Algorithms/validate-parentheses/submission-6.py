class Solution:
    def isValid(self, s: str) -> bool:
        # success condition: stack is empty
        pairs = {
            # key: open bracket; value: closed bracket
            "(": ")",
            "{": "}",
            "[": "]"
        }
        stack = []
        for char in s:
            # if open bracket, add to stack
            if char in pairs:
                stack.append(char)
            elif stack:
                top = stack[-1] # check top of stack
                if pairs[top] == char: # if closes brackets
                    stack.pop() # remove set of brackets
                else:
                    return False
            else:
                return False
        
        return False if stack else True

