'''
given a grid, find the largest island. an island is connected ONLY horizontally vertically.


You are given a matrix grid where grid[i] is either a 0 (representing water) or 1 (representing land).

An island is defined as a group of 1s connected horizontally or vertically.
- diagonals dont count

You may assume all four edges of the grid are surrounded by water.
- no land beyond grid

The area of an island is defined as the number of cells within the island.
- counting 1s in the island

Return the maximum area of an island in grid. If no island exists, return 0.



Input: grid = [
  [0,1,1,0,1],
  [1,0,1,0,1],
  [0,1,1,0,1],
  [0,1,0,0,1]
]

- max_rsf
- call bsf on first point in island
    - convert island to 0s after its been searched
    - once no more bfs, compare with max_rsf
'''


class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        max_rsf = 0

        def bfs(x, y):
            stack = []
            stack.append((x, y))
            grid[x][y] = 0
            directions = [
                (1, 0),
                (0, 1),
                (-1, 0),
                (0, -1)
            ]
            area = 0

            while stack:
                curr_x, curr_y = stack.pop()
                area += 1

                for dx, dy in directions:
                    nx, ny = curr_x + dx, curr_y + dy

                    if nx >= 0 and nx < len(grid) and ny >= 0 and ny < len(grid[0]):
                        if grid[nx][ny] == 1:
                            grid[nx][ny] = 0
                            stack.append((nx, ny))
            
            return area


        for x in range(len(grid)):
            for y in range(len(grid[0])):
                if grid[x][y] == 1:
                    curr_area = bfs(x, y)
                    max_rsf = max(max_rsf, curr_area)
        
        return max_rsf











