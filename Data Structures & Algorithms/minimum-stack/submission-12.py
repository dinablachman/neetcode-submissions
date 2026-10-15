class MinStack:

    def __init__(self):
        self.min_seen = []
        self.min_stack = []

    def push(self, val: int) -> None:
        if len(self.min_seen) == 0:
            self.min_seen.append(val)
        elif val <= self.min_seen[-1]:
            self.min_seen.append(val)
        self.min_stack.append(val)

    def pop(self) -> None:
        top = self.min_stack.pop()
        if len(self.min_seen) > 0 and top == self.min_seen[-1]:
            self.min_seen.pop()
        return top

    def top(self) -> int:
        top = self.min_stack[-1]
        return top

    def getMin(self) -> int:
        if len(self.min_seen) == 0:
            return 0
        else:
            return self.min_seen[-1]