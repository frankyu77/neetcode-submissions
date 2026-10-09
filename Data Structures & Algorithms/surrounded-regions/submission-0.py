'''
Connect: A cell is connected to adjacent cells horizontally or vertically.
    - up, down, left, right, no diagonal

Region: To form a region connect every 'O' cell. Regions can have any shape; they do not need to be squares or rectangles.
    - sounds like BFS from 'O' cells

Surround: A region is surrounded if none of the 'O' cells in that region are on the edge of the board. Such regions are completely enclosed by 'X' cells.
    - call BFS on all the edge 'O' cells
    - any 'O' cell that is not reachable from edge, convert to 'X'

First pass:
    - find all the edge 'O'
    - call BFS on all the edge 'O'
    - mark all 'O's that are reachable by BFS
        - use hashset to store position of 'O's
        - mark all visited 'O' to '-O'
Second pass:
    - go through the board, and turn all 'O's that are not marked to 'X'
'''
from collections import deque
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        q = deque()
        visited = set()

        m = len(board)
        n = len(board[0])

        for x in range(m):
            if board[x][0] == "O":
                q.append((x, 0))
                visited.add((x, 0))
            if board[x][n-1] == "O":
                q.append((x, n-1))
                visited.add((x, n-1))
        for y in range(n):
            if board[0][y] == "O":
                q.append((0, y))
                visited.add((0, y))
            if board[m-1][y] == "O":
                q.append((m-1, y))
                visited.add((m-1, y))

        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        while q:
            x, y = q.popleft()
            for dx, dy in directions:
                nx, ny = x+dx, y+dy
                if 0 <= nx < m and 0 <= ny < n and board[nx][ny] == 'O' and (nx, ny) not in visited:
                    visited.add((nx, ny))
                    q.append((nx, ny))
        
        for x in range(m):
            for y in range(n):
                if board[x][y] == 'O' and (x, y) not in visited:
                    board[x][y] = 'X'
















