class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0 
        for x in range(0,len(prices)):
            xPlus = x + 1
            while xPlus < len(prices):
                if (prices[xPlus] - prices[x]) > max_profit:
                    max_profit = prices[xPlus] - prices[x]
                xPlus += 1
        return max_profit

