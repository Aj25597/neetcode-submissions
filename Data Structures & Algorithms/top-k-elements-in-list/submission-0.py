class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #Style dict as {count: [nums]}
        counts = {}
        for x in nums:
            if x in counts:
                counts[x] = counts[x] + 1
            else:
                counts[x] = 1
        #print(counts)
        sorteds = sorted(counts, key=lambda num: counts[num], reverse=True)
        return sorteds[:k]
        
            