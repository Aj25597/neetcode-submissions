class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        lis = defaultdict(list)
        for s in strs:
            sortedS = ''.join(sorted(s))
            lis[sortedS].append(s)
        return list(lis.values())