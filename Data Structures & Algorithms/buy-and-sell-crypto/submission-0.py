class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        lowest = prices[0]
        for p in prices:
            if lowest > p:
                lowest = p
            if max_profit < p - lowest:
                max_profit = p - lowest
        return max_profit
                
