'''
Every consecutive pair of integers have opposite signs.

For all integers with the same sign, the order in which they were present in nums is preserved.

The rearranged array begins with a positive integer.
'''

class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        solution = []
        n, p = 0, 0
        positive = True

        while len(solution) < len(nums):
            if positive:
                while nums[p] < 0:
                    p += 1
                solution.append(nums[p])
                p += 1
            else:
                while nums[n] > 0:
                    n += 1
                solution.append(nums[n])
                n += 1
            positive = not positive
        return solution