'''
You are given a rectangular island heights where heights[r][c] represents the height above sea level of the cell at coordinate (r, c).

The islands borders the Pacific Ocean from the top and left sides, and borders the Atlantic Ocean from the bottom and right sides.
    - pacific:
        - top of heights[0][], left of heights[][0]
    - atlantic:
        - bottom of height[m][], right of height[][n]

Water can flow in four directions (up, down, left, or right) from a cell to a neighboring cell with height equal or lower. Water can also flow into the ocean from cells adjacent to the ocean.
    - water cannot flow diagonally
    - can only flow to neighbour if neighbour is <= current height
        - flow if grid[nx][ny] >= grid[x][y]

Find all cells where water can flow from that cell to both the Pacific and Atlantic oceans. Return it as a 2D list where each element is a list [r, c] representing the row and column of the cell. You may return the answer in any order.
    - for each cell bordering pacific, call BFS on it
        - opposite check, neighbour is >= to curr
        - store all cells in a set
    - for each cell bordering atlantic do same thing
        - store all cells in a set
    - cells that are in both sets mean that they can flow to both oceans, that is the answer
'''
from collections import deque
class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        m = len(heights)
        n = len(heights[0])

        p_q = deque()
        a_q = deque()
        p_set = set()
        a_set = set()

        for x in range(m):
            p_q.append((x, 0))
            p_set.add((x, 0))
            a_q.append((x, n-1))
            a_set.add((x, n-1))

        for y in range(n):
            p_q.append((0, y))
            p_set.add((0, y))
            a_q.append((m-1, y))
            a_set.add((m-1, y))
    
        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]

        p_visited = set(p_set)
        while p_q:
            x, y = p_q.popleft()
            for dx, dy in directions:
                nx, ny = dx+x, dy+y
                if nx >= 0 and nx < m and ny >= 0 and ny < n and heights[nx][ny] >= heights[x][y] and (nx, ny) not in p_visited:
                    p_set.add((nx, ny))
                    p_q.append((nx, ny))
                    p_visited.add((nx, ny))
        
        a_visited = set(a_set)
        while a_q:
            x, y = a_q.popleft()
            for dx, dy in directions:
                nx, ny = dx+x, dy+y
                if nx >= 0 and nx < m and ny >= 0 and ny < n and heights[nx][ny] >= heights[x][y] and (nx, ny) not in a_visited:
                    a_set.add((nx, ny))
                    a_q.append((nx, ny))
                    a_visited.add((nx, ny))

        solution = []
        for px, py in p_set:
            if (px, py) in a_set:
                solution.append([px, py])
        return solution














        