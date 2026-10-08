'''
You are given an integer array nums where nums[i] represents the amount of money the ith house has. 
- no negative money

The houses are arranged in a circle, i.e. the first house and the last house are neighbors.
- if start at index 0, cannot rob last house
- if start at index 1, can rob last house

You are planning to rob money from the houses, but you cannot rob two adjacent houses because the security system will automatically alert the police if two adjacent houses were both broken into.
- cannot rob neighbours, so can only go i+2 or i+3


Return the maximum amount of money you can rob without alerting the police.


Input: nums = [2,9,8,3,6]
start index 0
    - cannot end at index len(nums) - 1
    - can go to i+2 or i+3

start index 1
    - can end at index len(nums) - 1
    - can go to i+2 or i+3
'''
from functools import cache
class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        @cache
        def moneyRobbed_from_startingAt(i: int, firstHouse: bool) -> int:
            if i >= len(nums):
                return 0
            if i == len(nums) - 1 and firstHouse:
                return 0
            
            jump2 = moneyRobbed_from_startingAt(i+2, firstHouse)
            jump3 = moneyRobbed_from_startingAt(i+3, firstHouse)
            
            return nums[i] + max(jump2, jump3)
        
        return max(moneyRobbed_from_startingAt(0, True),
                moneyRobbed_from_startingAt(1, False),
                moneyRobbed_from_startingAt(2, False))






        