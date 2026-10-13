'''
There are a number of piles arranged in a row, and each pile has a positive integer number of stones piles[i]. 

The objective of the game is to end with the most stones.

Alice and Bob take turns, with Alice starting first.
    - we want to alternate turns
    - perhaps we have to keep track of both alice and bob

On each players turn, that player can take all the stones in the first X remaining piles, where 1 <= X <= 2M. 
Then, we set M = max(M, X). Initially, M = 1.

The game continues until all the stones have been taken.


Assuming Alice and Bob play optimally, return the maximum number of stones Alice can get.
    - we only want to maximize alice
    - or in other words minimize bob

Input: piles = [3,1,2,5,7]

1 <= X <= 2


so alice has 1-2M choices (up to 2M choices)
    - she can either take one pile or two piles or all the way up to M piles
    - update M accordingly

we want to keep track of the current index we are on, and the number of piles you can take
    - at this current index, we can take up to 2M piles

but how do we keep track of the other player:
    - do we assume that they will alwyas try to maximize their decision 
    - or can they mnimize it to guarentee they can win

'''
from functools import cache
class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        n = len(piles)
        suffix = [0] * (n + 1)
        for i in range(n - 1, -1, -1):
            suffix[i] = suffix[i + 1] + piles[i]
        @cache
        def maxStones(i: int, M: int):
            if i + 2 * M >= n:
                return suffix[i]
            msf = 0
            for x in range(1, 2*M+1):
                msf = max(msf, suffix[i] - maxStones(i+x, max(x, M)))
            return msf
        return maxStones(0, 1)







        