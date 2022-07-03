class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        if len(prices) == 0:
            return 0
        
        max = prices[len(prices)-1]
        profit = 0
        
        for item in prices[::-1]:
            if max - item > profit:
                profit = max - item
            if item > max:
                max = item
        
        return profit
            