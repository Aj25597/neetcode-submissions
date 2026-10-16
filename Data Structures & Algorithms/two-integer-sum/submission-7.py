class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        idxVal = {}
        for idx,val in enumerate(nums):
            complement = target - val
            if complement in idxVal:
                return [idxVal[complement],idx]
            else:
                idxVal[val] = idx
            

            
        