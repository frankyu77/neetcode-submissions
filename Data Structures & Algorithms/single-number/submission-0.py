class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        sol = nums[0]
        for n in nums[1:]:
            sol = sol ^ n
        return sol