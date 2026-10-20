class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # brute force solution
        a = 0
        b = 0
        total = []
        while a < len(nums1) and b < len(nums2):
            if nums1[a] < nums2[b]:
                total.append(nums1[a])
                a = a + 1
            elif nums1[a] > nums2[b]:
                total.append(nums2[b])
                b = b + 1
            else:
                total.append(nums1[a])
                total.append(nums2[b])
                a = a + 1
                b = b + 1
        if a < len(nums1):
            while a < len(nums1):
                total.append(nums1[a])
                a = a + 1
        if b < len(nums2):
            while b < len(nums2):
                total.append(nums2[b])
                b = b + 1
        print(total)
        if len(total) % 2 == 0:
            R = (len(total) // 2) - 1
            L = R + 1
            mid = (total[R] + total[L]) / 2
            return mid
        half = len(total) // 2
        return total[half]