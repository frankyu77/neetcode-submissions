'''
given cost, i can start at cost[0] or cost[1] and i want to reach the top (len(cost)) by taking only 1 or 2 steps while minimizing my cost


You are given an array of integers cost where cost[i] is the cost of taking a step from the ith floor of a staircase.
- cost is medium
- cost[i] is medium
- cost[i] is the cost of the floor

After paying the cost, you can step to either the (i + 1)th floor or the (i + 2)th floor.
- can only take 1 or 2 steps
    - so go to the i+1th index or the i+2th index
    - reach the end once (i+1) or (i+2) is >= len(cost)

You may choose to start at the index 0 or the index 1 floor.
- can start at index 0 or 1
- but min cost doesnt necessarily mean that its best pick
    - so dont know which index to start at
    - have to check both

Return the minimum cost to reach the top of the staircase, i.e. just past the last index in cost.
- stop when you reach >= len(cost)


Input: cost = [1,2,1,2,1,1,1]

top = len(cost)

Decision 1: start at index 0 or index 1

Decision 2: take 1 step or 2 step from current index i
- take 1 step
    - i >= top
    - action: take 1 step or 2 step
- take 2 step
    - i >= top
    - action: take 1 step or 2 step

cost = cost[i] + min(cost_1, cost_2)
'''
from functools import cache

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)

        @cache
        def cost_startingAt(i: int) -> int:
            if i >= n:
                return 0
            
            take_1, take_2 = 0, 0

            if i+1 < n:
                take_1 = cost_startingAt(i+1)
            if i+2 < n:
                take_2 = cost_startingAt(i+2)
            
            return cost[i] + min(take_1, take_2)
        
        return min(cost_startingAt(0), cost_startingAt(1))











