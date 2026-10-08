'''
Summary: rob the most money without robbing two houses in a row

You are given an integer array nums where nums[i] represents the amount of money the ith house has.
- nums.length = medium
- nums[i] = medium
- nums[i] is positive or 0

The houses are arranged in a straight line, i.e. the ith house is the neighbor of the (i-1)th and (i+1)th house.

You are planning to rob money from the houses, but you cannot rob two adjacent houses because the security system will automatically alert the police if two adjacent houses were both broken into.
- cannot rob two houses in a row
- so can only go from i to i+2 or i+3
- can either start at index 0 or 1

Return the maximum amount of money you can rob without alerting the police.

Input: nums = [2,9,8,3,6]
Start at i = 0:
    - choose to go to i+2 or i+3
    - udpate total with nums[i]

Start at i = 1:
    - choose to go to i+2 or i+3
    - update total ith nums[i]
'''
from functools import cache

class Solution:
    def rob(self, nums: List[int]) -> int:
        @cache
        def money_startingFrom(i: int) -> int:
            if i >= len(nums):
                return 0

            jump_2, jump_3 = 0, 0

            if i+2 < len(nums):
                jump_2 = money_startingFrom(i+2)
            if i+3 < len(nums):
                jump_3 = money_startingFrom(i+3)
            
            return nums[i] + max(jump_2, jump_3)
        return max(money_startingFrom(0), money_startingFrom(1))







