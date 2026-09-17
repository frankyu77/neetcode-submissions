class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left, right = 0, 1
        rsf = 0

        while right < len(prices):
            if prices[right] >= prices[left]:
                rsf = max(rsf, prices[right] - prices[left])
                right += 1
            else:
                left = right
        return rsf
            
            
