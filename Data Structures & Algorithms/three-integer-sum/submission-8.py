class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        solutions = []
        nums = sorted(nums) # sort in ascending order
        numsCopy = nums
        current = numsCopy.pop(0) # starts with second element

        # while can still form triplets
        while len(numsCopy) > 1: 
            target = 0 - current
            start = 0
            stop = len(numsCopy) - 1

            while (start < stop):
                if (numsCopy[start] + numsCopy[stop] == target):
                    solution = [current, numsCopy[start], numsCopy[stop]]
                    if solution not in solutions: 
                        solutions.append(solution)
                    start = start + 1
                elif(numsCopy[start] + numsCopy[stop] < target):
                    start = start + 1
                else:
                    stop = stop - 1
            
            # move to next num + sublist
            current = numsCopy.pop(0) 

        return solutions
