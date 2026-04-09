class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = 0 
    
        ans = 0

        for leng in range(1, len(prices)):
            if prices[leng] < prices[l]:
                l = leng
            else:
                profit = prices[leng] - prices[l]
                ans = max(ans, profit)
        return ans