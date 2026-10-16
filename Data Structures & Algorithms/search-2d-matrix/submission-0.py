class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # search 1st & last elements of each row
        r = []
        for row in matrix:
            first = row[0]
            last = row[-1]
            if target == first or target == last:
                return True
            elif target > first and target < last:
                r = row
        if not r:
            return False
        
        left = 0
        right = len(r) - 1
        if len(r) == 1:
            return True if r[0] == target else False

        while (left < right):
            if target == r[left] or target == r[right]:
                return True
            mid = (left + right) // 2
            if target == r[mid]:
                return True
            elif target > r[mid]:
                left = mid + 1
            elif target < r[mid]:
                right = mid - 1
        return False        
            
        