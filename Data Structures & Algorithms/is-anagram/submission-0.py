class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        x = list(s)
        y = list(t)
        x.sort()
        y.sort()
        return x == y
                    