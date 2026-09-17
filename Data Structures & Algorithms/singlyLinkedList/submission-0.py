class LinkedList:
    
    def __init__(self):
        self.linkedList = []
    
    def get(self, index: int) -> int:
        if index >= len(self.linkedList):
            return -1
        return self.linkedList[index]

    def insertHead(self, val: int) -> None:
        newList = [None] * (len(self.linkedList) + 1)
        newList[0] = val
        for i in range(0, len(self.linkedList)):
            newList[i+1] = self.linkedList[i]
        self.linkedList = newList

    def insertTail(self, val: int) -> None:
        self.linkedList.append(val)

    def remove(self, index: int) -> bool:
        size = len(self.linkedList)
        if index >= size:
            return False
        i = index + 1
        before = self.linkedList[0:index]
        after = self.linkedList[i:size]
        self.linkedList = before + after
        return True
        
    def getValues(self) -> List[int]:
        return self.linkedList