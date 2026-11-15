class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        q = collections.deque()
        rows, cols = len(grid), len(grid[0])
        fresh = 0
        directions = [[0,1],[0,-1],[1,0],[-1,0]]

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    q.append((r,c))
                if grid[r][c] == 1:
                    fresh += 1
        
        minutes = 0
        while q and fresh > 0:
            for _ in range(len(q)):
                row, col = q.popleft()
                for dr, dc in directions:
                    r, c = row + dr, col + dc
                    if (0 <= r < rows) and (0 <= c < cols) and (grid[r][c] == 1):
                        grid[r][c] = 2
                        fresh -= 1
                        q.append((r,c))
            minutes += 1
        
        return -1 if fresh > 0 else minutes