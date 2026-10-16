class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for idx,val in enumerate(nums):
            for idxPlus in range(idx + 1,len(nums)):
                if val + nums[idxPlus] == target:
                    return [idx,idxPlus]
            

            
        