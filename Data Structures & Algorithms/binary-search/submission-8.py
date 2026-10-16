class Solution:
    def search(self, nums: List[int], target: int) -> int:
        start = 0
        stop = len(nums)-1
        if len(nums) == 1:
            return 0 if nums[0] == target else -1

        while (start < stop):
            if nums[start] == target:
                return start
            elif nums[stop] == target:
                return stop
            mid = (stop + start) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                stop = mid
            elif nums[mid] < target:
                start = mid + 1
        return -1

