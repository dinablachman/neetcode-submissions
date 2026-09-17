# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def insertionSort(self, pairs: List[Pair]) -> List[List[Pair]]:
        listOfPairs = []
        if len(pairs) < 1:
            return listOfPairs
        
        if len(pairs) == 1:
            listOfPairs.append(pairs)
            return listOfPairs

        for current in range(0, len(pairs)):
            for compared in range(current - 1, -1, -1):
                pointer = compared + 1
                currentKey = pairs[pointer].key
                comparedKey = pairs[compared].key
                if currentKey < comparedKey:
                    temp1 = pairs[pointer]
                    temp2 = pairs[compared]
                    pairs[pointer] = temp2
                    pairs[compared] = temp1

            copy = pairs.copy()
            listOfPairs.append(copy)

        return listOfPairs

        
class Pair:
    def __init__(self, key: int, value: str):
        self.key = key
        self.value = value