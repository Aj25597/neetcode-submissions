class Solution:
    
    def internal_search(self,nums,target,left,right) -> int:
        if left > right:
            return -1
        if nums[left] == target:
            return left
        if nums[right] == target:
            return right      
        middle = int((left + right) / 2)
        #print(f"{middle} {nums[middle]}")
        if nums[middle] == target:
            return middle
        else:
            if nums[middle] < target:
                return self.internal_search(nums,target,middle + 1,right)
            else:
                return self.internal_search(nums,target,left,middle - 1)

    def search(self, nums: List[int], target: int) -> int:
        return self.internal_search(nums,target,0,len(nums)-1)

        