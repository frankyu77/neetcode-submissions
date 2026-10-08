'''
You are given an integer array coins representing coins of different denominations and an integer amount representing a target amount of money.
- coins[i] cannot be negative or zero
- amount can be zero

Return the fewest number of coins that you need to make up the exact target amount.

If it is impossible to make up the amount, return -1.
- occurs when all of coins[i] > amount

You may assume that you have an unlimited number of each coin.
- can use same coin multiple times

Input: coins = coins, amount = amount
take coins[i]:
    - take coins[i+1], coins[i]
    - amount = amount - coins[i]
skip coins[i]:
    - take coin coins[i+1]
    - amount = amount
'''
from functools import cache
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        @cache
        def numWays_from_toAmount(i: int, x: int) -> int:
            if x == 0:
                return 0
            if i == len(coins):
                return float('inf')
            
            take = float('inf')

            if coins[i] <= x:
                take = 1 + numWays_from_toAmount(i, x - coins[i])

            skip = numWays_from_toAmount(i+1, x)

            return min(take, skip)
        rsf = numWays_from_toAmount(0, amount)
        return -1 if rsf == float('inf') else rsf
            