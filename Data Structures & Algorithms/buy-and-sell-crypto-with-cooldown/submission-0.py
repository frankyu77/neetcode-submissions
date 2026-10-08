'''
You are given an integer array prices where prices[i] is the price of NeetCoin on the ith day.

You may buy and sell one NeetCoin multiple times with the following restrictions:

    - After you sell your NeetCoin, you cannot buy another one on the next day (i.e., there is a cooldown period of one day).
        - after sell on day i, can you only buy on day i+2
        - price = sell day - buy day    
            - keep track of the buy day
            - can either sell on next day or not sell on next day

    - You may only own at most one NeetCoin at a time.
        - can only buy after selling
        - can only sell if im holding

You may complete as many transactions as you like.
'''
from functools import cache

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        @cache
        def profit_fromDay_holding(i: int, holding: bool) -> int:
            if i >= len(prices):
                return 0
            
            if holding:
                sell = prices[i] + profit_fromDay_holding(i+2, False)
                not_sell = profit_fromDay_holding(i+1, True)
                return max(sell, not_sell)
            else:
                buy = -prices[i] + profit_fromDay_holding(i+1, True)
                not_buy = profit_fromDay_holding(i+1, False)
                return max(buy, not_buy)

        return profit_fromDay_holding(0, False)
