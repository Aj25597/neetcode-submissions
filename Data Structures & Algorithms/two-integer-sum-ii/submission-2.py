class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        start = 0
        end = len(numbers) - 1
        while start < end:
            if numbers[start] + numbers[end] == target:
                return [start + 1,end + 1]
            elif numbers[start] + numbers[end] > target:
                #Indicates that one of the numbers is too big, but reduce end b/c sorted list
                end -= 1
            else:
                start +=1
        
        return [0,0]
            
        