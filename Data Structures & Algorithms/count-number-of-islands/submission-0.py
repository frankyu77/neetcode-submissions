class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows, cols = len(grid), len(grid[0])
        count = 0

        def bfs(r, c):
            stack = []
            stack.append((r, c))

            directions = [
                (1, 0),
                (0, 1),
                (-1, 0),
                (0, -1)
            ]

            while stack:
                curr = stack.pop()
                grid[curr[0]][curr[1]] = "0"

                for dr, dc in directions:
                    nr, nc = curr[0] + dr, curr[1] + dc
                    
                    if nr >= 0 and nr < rows and nc >= 0 and nc < cols and grid[nr][nc] == "1":
                        stack.append((nr, nc))


        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1":
                    count += 1
                    bfs(r, c)
        return count