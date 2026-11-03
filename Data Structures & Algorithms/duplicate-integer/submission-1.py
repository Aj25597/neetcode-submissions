class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        sexc = set()
        for x in nums:
            if x in sexc:
                return True
            else:
                sexc.add(x)
        return False