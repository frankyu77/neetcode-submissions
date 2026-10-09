'''
You are given a mxn 2D grid initialized with these three possible values:
    - -1 - A water cell that can not be traversed.
    - 0 - A treasure chest.
    - INF - A land cell that can be traversed. We use the integer 2^31 - 1 = 2147483647 to represent INF.

Fill each land cell with the distance to its nearest treasure chest. If a land cell cannot reach a treasure chest then the value should remain INF.
    - have to call bfs from each land cell
    - could also call bfs from the treasure adn go outwards. 
        - instead of calling bfs from each treasure, i can do multi source bfs and put all the treasures into once queue

Assume the grid can only be traversed up, down, left, or right.
- no diagonals
'''
from collections import deque

class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        INF = 2**31 - 1
        m = len(grid)
        n = len(grid[0])

        q = deque()
        
        for x in range(m):
            for y in range(n):
                if grid[x][y] == 0:
                    q.append((x, y))
        
        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]

        while q:
            x, y = q.popleft()
            for dx, dy in directions:
                nx, ny = x+dx, y+dy
                if nx >= 0 and nx < m and ny >= 0 and ny < n and grid[nx][ny] == INF:
                    grid[nx][ny] = grid[x][y] + 1
                    q.append((nx, ny))
        







