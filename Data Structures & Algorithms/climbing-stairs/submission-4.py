class Solution:
    def climbStairsHelper(self,n,memo):
        if n in memo:
            return memo[n]
        
        result = self.climbStairsHelper(n-1,memo) + self.climbStairsHelper(n-2,memo)

        memo[n] = result
        return result
        

    def climbStairs(self, n: int) -> int:
        memo = {
            0: 0,
            1: 1,
            2: 2,
            3: 3
        }
        return self.climbStairsHelper(n,memo)