class Solution:
    def search(self, nums: List[int], target: int) -> int:
        start = 0
        stop = len(nums)-1
        while (start < stop):
            mid = int(start + (stop - start) / 2)
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                stop = mid
            elif nums[mid] < target:
                start = mid + 1
        if (start == stop):
            return start if nums[start] == target else -1
        return -1

