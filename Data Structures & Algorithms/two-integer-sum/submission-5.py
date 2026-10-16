class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            x = nums[i]
            y = target - x
            if y in nums and i == nums.index(y):
                continue
            if y in nums:
                if i < nums.index(y):
                    return [i,nums.index(y)]
                else:
                    return [nums.index(y),i]
            
            
            

        