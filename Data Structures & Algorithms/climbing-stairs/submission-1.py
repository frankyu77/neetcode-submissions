'''
find different ways to reach the top of stairs using only 1 or 2 steps


You are given an integer n representing the number of steps to reach the top of a staircase. 
- n is small

You can climb with either 1 or 2 steps at a time.
- order matters
    - 122 or 221
    - these are different
- can take steps multiple times
- can choose to take 1 step or not
- can choose to take 2 step or not

Return the number of distinct ways to climb to the top of the staircase.
- stop when the current number of steps is equal to the top


Input: n = 3

Decision: find number of ways to n using only 1 or 2

starting with the first step what are my options?
take 1 step:
    - n-1 till top
take 2 steps:
    - n-2 till top
'''
from functools import cache



class Solution:
    def climbStairs(self, n: int) -> int:
        @cache
        def numWays_takingSteps_toMake(top: int) -> int:
            if top == 0:
                return 1

            take_1, take_2 = 0, 0

            if (top - 1) >= 0:
                take_1 = numWays_takingSteps_toMake(top - 1)
            if (top - 2) >= 0:
                take_2 = numWays_takingSteps_toMake(top - 2)

            return take_1 + take_2
        return numWays_takingSteps_toMake(n)








