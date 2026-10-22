class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        if not nums:
            return [[]]
        subsets = []
        for num in nums:
            if not subsets:
                subsets.append([])
                subsets.append([num])
            else:
                for i in range(len(subsets)):
                    subsets.append(subsets[i] + [num])
        return subsets
            





        