'''
The n-queens puzzle is the problem of placing n queens on an n x n chessboard so that no two queens can attack each other.
    - A queen in a chessboard can attack horizontally, vertically, and diagonally.
    - diag \ --> (x, y) --> x-y is the same for all
    - diag / --> (x, y) --> x+y is the same for all

- counter i (how many queens are placed)
- for each position on the board:
    - place the queen there:
        - i = i+1
        - put 'Q' in that position
        - check that there are no other queen horizontally, vertically, and diagonally
    - dont place the queen there
        - i = i
        - move to next position



Given an integer n, return all distinct solutions to the n-queens puzzle.

Each solution contains a unique board layout where the queen pieces are placed. 'Q' indicates a queen and '.' indicates an empty space.
'''

class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        board = [['.'] * n for _ in range(n)]
        sol = []
        cols = set()
        diag = set() # / --> x+y
        anti = set() # \ --> abs(x-y)

        def dfs(r: int):
            if r == n:
                sol.append(["".join(row) for row in board])
                return
            
            for c in range(n):
                if c in cols or r+c in diag or r-c in anti:
                    continue
    
                board[r][c] = 'Q'
                cols.add(c)
                diag.add(r+c)
                anti.add(r-c)
                dfs(r+1)

                board[r][c] = '.'
                cols.remove(c)
                diag.remove(r+c)
                anti.remove(r-c)
        dfs(0)
        return sol
                














