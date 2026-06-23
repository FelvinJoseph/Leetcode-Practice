class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left = 0  # Buy pointer
        right = 1 # Sell pointer
        max_profit = 0
        
        while right < len(prices):
            # Check if it a profitable transaction?
            if prices[left] < prices[right]:
                profit = prices[right] - prices[left]
                max_profit = max(max_profit, profit)
            else:
                # We found a lower buying point, shift the left pointer
                left = right
            
            
            right += 1
            
        return max_profit
