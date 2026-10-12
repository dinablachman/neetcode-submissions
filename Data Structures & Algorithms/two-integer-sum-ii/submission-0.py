class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        start = 1
        stop = len(numbers)
        # every time we access an array element, decrease the index by 1

        while (start < stop):
            currentSum = numbers[start-1] + numbers[stop-1]
            if (currentSum == target):
                return [start, stop]
            if (currentSum > target):
                stop = stop - 1
            if (currentSum < target):
                start = start + 1
        
        return []
        