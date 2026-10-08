'''
There is an m x n grid where you are allowed to move either down or to the right at any point in time.

Given the two integers m and n, return the number of possible unique paths that can be taken from the top-left corner of the grid (grid[0][0]) to the bottom-right corner (grid[m - 1][n - 1]).
'''
from functools import cache
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        @cache
        def numWays_from(i: int, j: int) -> int:
            if i >= m or j >= n:
                return 0
            
            if i == m-1 and j == n-1:
                return 1
            
            right = numWays_from(i+1, j)
            down = numWays_from(i, j+1)

            return right + down
        return numWays_from(0, 0)