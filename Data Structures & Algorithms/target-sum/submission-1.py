'''
You are given an array of integers nums and an integer target.
- nums[i] is positive or 0
- target can be negative

For each number in the array, you can choose to either add or subtract it to a total sum.
For example, if nums = [1, 2], one possible sum would be "+1-2=-1".

If nums=[1,1], there are two different ways to sum the input numbers to get a sum of 0: "+1-1" and "-1+1".
- we can either negate the current value and add to sum
- or we can just add the current value to the sum

Return the number of different ways that you can build the expression such that the total sum equals target.


Input: nums = nums, target = target
- check that curr sum == target:
    - return 1

- add nums[i] to curr_sum
    - move to i+1

- add -nums[i] to curr_sum
    - move to i+1

recurrance
'''
from functools import cache
class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        @cache
        def numWays_from_toGet(i: int, x: int) -> int:
            if i >= len(nums):
                return 1 if x == 0 else 0
            
            normal = numWays_from_toGet(i+1, x-nums[i])
            negated = numWays_from_toGet(i+1, x+nums[i])

            return normal + negated
        return numWays_from_toGet(0, target)



