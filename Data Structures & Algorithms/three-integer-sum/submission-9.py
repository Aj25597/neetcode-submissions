class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        x = []
        
        for i in range(0,len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            l,r = i + 1, len(nums) - 1
            while l < r:
                tS = nums[i] + nums[l] + nums[r]
                if tS > 0:
                    r -= 1
                elif tS < 0:
                    l += 1
                else:
                    x.append([nums[i],nums[l],nums[r]])
                    l += 1
                    while nums[l] == nums[l - 1] and l < r:
                        l +=1
        return x 

                


