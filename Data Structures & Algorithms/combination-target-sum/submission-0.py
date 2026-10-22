class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        results = []
        self.comboHelper(nums, target, 0, [], results, 0)
        return results

    def comboHelper(self, nums: List[int], target: int, total: int, path: List[int], results: List[int], idx) -> List[int]:
        if total == target:
            results.append(path.copy())
        for i in range(idx, len(nums)):
            if total + nums[i] <= target:
                total = total + nums[i]
                path.append(nums[i])
                self.comboHelper(nums, target, total, path, results, i)
                total = total - nums[i]
                path.pop()
        return []
            
