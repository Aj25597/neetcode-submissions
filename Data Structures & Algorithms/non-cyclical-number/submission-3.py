class Solution:
    def isHappy(self, n: int) -> bool:
        visited = set()
        while n != 1:
            count = 0
            #Get digits
            for digit in str(n):
                count = count + (int(digit) * int(digit))
            if count == 1:
                    return True 
            if count in visited:
                return False
            visited.add(count)
            n = count
            
        return True
            
        
