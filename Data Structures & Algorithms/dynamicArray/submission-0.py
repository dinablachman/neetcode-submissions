class DynamicArray:
    
    def __init__(self, capacity: int):
        self.array = [None] * capacity
        self.capacity = capacity
        self.size = 0

    def get(self, i: int) -> int:
        return self.array[i]

    def set(self, i: int, n: int) -> None:
        prev = self.array[i]
        if prev is None and n is not None:
            self.size = self.size + 1
        self.array[i] = n

    def pushback(self, n: int) -> None:
        if self.size == self.capacity:
            self.resize()
        self.array[self.size] = n
        self.size = self.size + 1

    def popback(self) -> int:
        index = self.getSize() - 1
        popped = self.array[index]
        self.array[index] = None
        self.size = self.size - 1
        return popped

    def resize(self) -> None:
        newArray = [None] * 2 * self.capacity
        for i in range (0, self.size):
            newArray[i] = self.array[i]
        self.array = newArray
        self.capacity = self.capacity * 2

    def getSize(self) -> int:
        return self.size
    
    def getCapacity(self) -> int:
        return self.capacity
