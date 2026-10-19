class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxL = 0
        seen = set()
        L = 0
        for R in range(len(s)):
            while s[R] in seen:
                seen.remove(s[L])
                L = L + 1
            seen.add(s[R])
            maxL = max(maxL, R - L + 1)
        return maxL
        