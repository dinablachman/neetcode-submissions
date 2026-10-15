class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0

        nums = sorted(list(set(nums)))
        i = 1
        counter = 0
        best = 0
        while i < len(nums):
            diff = nums[i] - nums[i-1]
            if diff == 1:
                counter = counter + 1
                if counter > best:
                    best = counter
            else:
                counter = 0
            i = i + 1

        return best + 1