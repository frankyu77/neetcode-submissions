'''
Given an integer array nums, return the length of the longest strictly increasing subsequence.

A subsequence is a sequence that can be derived from the given sequence by deleting some or no elements without changing the relative order of the remaining characters.

starting at index i:
- can choose to jump to any number from [i:] that is stricly greater than nums[i]
'''

from functools import cache
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        @cache
        def getIncreasing_from(i: int) -> int:
            if i == len(nums):
                return 1
            
            msf = 1
            for n in range(i+1, len(nums)):
                if nums[n] > nums[i]:
                    curr_max = 1 + getIncreasing_from(n)
                    msf = max(curr_max, msf)
            return msf
        return max(getIncreasing_from(i) for i in range(len(nums)))
            
