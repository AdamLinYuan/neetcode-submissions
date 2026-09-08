from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        q = deque()
        fresh = 0
        
        # 1. Initialization: Count fresh oranges & queue up rotten ones
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    fresh += 1
                elif grid[r][c] == 2:
                    q.append((r, c))
        
        # Helper function (Using 'nonlocal' to update fresh count safely)
        def bfs(r, c):
            nonlocal fresh
            # Check bounds and if the orange is actually fresh
            if r < 0 or r >= ROWS or c < 0 or c >= COLS or grid[r][c] != 1:
                return
            
            # Mark as rotten, decrement fresh count, and add to queue
            grid[r][c] = 2
            fresh -= 1
            q.append((r, c))

        minutes = 0
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        
        # 2. The Loop
        # Condition: Run ONLY if there are rotten oranges AND fresh ones left to infect.
        # This prevents the loop from running that one extra time (removing the need for -1)
        while q and fresh > 0:
            minutes += 1
            for _ in range(len(q)):
                r, c = q.popleft()
                for dr, dc in directions:
                    bfs(r + dr, c + dc)
                    
        # 3. Final Result
        return minutes if fresh == 0 else -1