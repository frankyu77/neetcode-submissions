'''
You are given an integer array coins representing coins of different denominations (e.g. 1 dollar, 5 dollars, etc) 
- can coins be negative? --> no
- will the coins array always be none empty? --> yes

and an integer amount representing a target amount of money.

Return the number of distinct combinations that total up to amount.
- must be exact
- what makes it distinct?
    - order doesnt matter
    - 112 vs 211 --> same thing

If its impossible to make up the amount, return 0.
- if all coins[i] > amount
    - return 0
- if none of the coins add up to amount:
    - return 0

You may assume that you have an unlimited number of each coin and that each value in coins is unique.
- no repeat coins
- can choose same coin multiple times


Input: amount = amount, coins = coins
- choose i:
    - amount -= coins[i]
    - stay at i, or go to i+1
- not choose i:
    - amount = amount
    - go to i+2
'''
from functools import cache
class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        @cache
        def numWays_toAmount_from(amount:int, i: int) -> int:
            if i >= len(coins):
                return 0
            if amount == 0:
                return 1
            if amount < 0:
                return 0

            choose = numWays_toAmount_from(amount-coins[i], i)
            not_choose = numWays_toAmount_from(amount, i+1)
            
            return choose + not_choose
        return numWays_toAmount_from(amount, 0)








