class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = {}

        for s in strs:
            t = "".join(sorted(s))
            if t not in anagrams:
                anagrams[t] = [s]
            else:
                anagrams[t].append(s)
        
        return list(anagrams.values())

        