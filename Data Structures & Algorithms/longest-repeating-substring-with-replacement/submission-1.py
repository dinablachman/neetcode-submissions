class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        maxL = 0
        maxfreq = 0
        L = 0
        freq = {}
        for R in range(len(s)):
            freq[s[R]] = freq.get(s[R], 0) + 1
            maxfreq = max(freq.values())
            while((R - L + 1) - maxfreq > k):
                freq[s[L]] = freq.get(s[L], 0) - 1
                maxfreq = max(freq.values())
                L = L + 1
            maxL = max(maxL, R-L+1)
        return maxL