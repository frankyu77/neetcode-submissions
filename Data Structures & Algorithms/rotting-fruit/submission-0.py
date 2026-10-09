'''
0 representing an empty cell
1 representing a fresh fruit
2 representing a rotten fruit
    - can there be multiple fruit

Every minute, if a fresh fruit is horizontally or vertically adjacent to a rotten fruit, then the fresh fruit also becomes rotten.
    - no diagonal
    - sounds like BFS

Return the minimum number of minutes that must elapse until there are zero fresh fruits remaining. If this state is impossible within the grid, return -1.
    - what does it mean by state is impossible
        - no rotten orange in an island
    - need a way to check if all fruits have been infected
        - maybe do one pass of the grid to get total number of fruits
        - then second pass would be multi-source BFS, decrementing the total fruits as we infect
        - if bfs over and there is total fruit is not 0 then -1
'''

from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        q = deque()
        time = 0

        total_fruit = 0
        for x in range(m):
            for y in range(n):
                if grid[x][y] == 1:
                    total_fruit += 1
                if grid[x][y] == 2:
                    q.append((x, y))
        
        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]

        while q and total_fruit > 0:
            for _ in range(len(q)):
                rx, ry = q.popleft()
                for dx, dy in directions:
                    nx, ny = rx+dx, ry+dy
                    if nx >= 0 and nx < m and ny >= 0 and ny < n and grid[nx][ny] == 1:
                        grid[nx][ny] = 2
                        total_fruit -= 1
                        q.append((nx, ny))
            time += 1
        
        return -1 if total_fruit > 0 else time








        
