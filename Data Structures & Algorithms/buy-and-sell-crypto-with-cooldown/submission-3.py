'''
You are given an integer array prices where prices[i] is the price of NeetCoin on the ith day.
- can there be negative prices[i]? --> no
- can prices[i] be 0? --> yes
- is length of prices always greater than 0? --> yes
- can you have negative profit? --> yes

You may buy and sell one NeetCoin multiple times with the following restrictions:
- After you sell your NeetCoin, you cannot buy another one on the next day (i.e., there is a cooldown period of one day).
    - when sell on day i:
        - can only buy from day i+2
- You may only own at most one NeetCoin at a time.
    - need something to tell me if im holding a coin or not
        - boolean

Return the maximum profit you can achieve.


- if holding coin on day i:
    - sell coin
        - go to i+2 day to make decision
    - dont sell coin
        - go to i+1 day to make decision
- if not holding coin on day i:
    - buy coin
        - go to i+1 day to make decision
        - i am now holding a coin
    - dont buy coin
        - go to i+1 to make decision

Input: prices = [1,3,4,0,4]
'''
# from functools import cache
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # @cache
        # def maxProfit_fromDay(i: int, holding: bool) -> int:
        #     if i >= len(prices):
        #         return 0

        #     max_profit = 0
        #     if holding:
        #         sell = prices[i] + maxProfit_fromDay(i+2, False)
        #         dont_sell = maxProfit_fromDay(i+1, True)
        #         max_profit = max(sell, dont_sell)
        #     else:
        #         buy = -prices[i] + maxProfit_fromDay(i+1, True)
        #         dont_buy = maxProfit_fromDay(i+1, False)
        #         max_profit = max(buy, dont_buy)
        #     return max_profit
        # return maxProfit_fromDay(0, False)

        dp = [[0, 0] for _ in range(len(prices)+2)]
        #. [False, True]

        for i in range(len(prices) - 1, -1, -1):
            sell = prices[i] + dp[i+2][0]
            dont_sell = dp[i+1][1]
            dp[i][1] = max(sell, dont_sell)

            buy = -prices[i] + dp[i+1][1]
            dont_buy = dp[i+1][0]
            dp[i][0] = max(buy, dont_buy)
        return dp[0][0]
        
            
            











