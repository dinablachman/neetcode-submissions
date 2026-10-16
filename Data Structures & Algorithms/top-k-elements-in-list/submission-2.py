class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        #todo optimize: initialize freq counts (values) by default to 0
        for num in nums:
            if num not in freq:
                freq[num] = 1
            else:
                freq[num] = freq[num] + 1
        
        # sort by value descending
        sorted_freq = dict(sorted(freq.items(), key=lambda item: item[1], reverse=True))
        top_k = list(sorted_freq.keys())
        return top_k[0:k]
        