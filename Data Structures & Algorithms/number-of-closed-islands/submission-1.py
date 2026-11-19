class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        directions = [[1,0], [-1, 0], [0,1], [0,-1]]
        
        def dfs(r, c):
            stack = [(r, c)]
            while stack:
                r, c = stack.pop()
                if r < 0 or c < 0 or r == rows or c == cols or grid[r][c] != 0:
                    continue
                grid[r][c] = 1
                for dr, dc in directions:
                    stack.append((r + dr, c + dc))


        for r in range(rows):
            dfs(r,0)
            dfs(r,cols - 1)
        
        for c in range(cols):
            dfs(0,c)
            dfs(rows - 1, c)

        closed = 0

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    dfs(r,c)
                    closed += 1
        
        return closed
        
