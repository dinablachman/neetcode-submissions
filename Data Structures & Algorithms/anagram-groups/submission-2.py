class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = {}
        anagram_list = []

        # build groups of anagrams
        for s in strs:
            t = "".join(sorted(s))
            if t not in anagrams:
                anagrams[t] = [s]
            else:
                anagrams[t].append(s)
        
        # build anagram list from dict values
        for k, v in anagrams.items():
            anagram_list.append(v)

        return anagram_list

        