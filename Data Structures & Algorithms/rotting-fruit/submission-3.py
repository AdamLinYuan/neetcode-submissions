class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        visit = set()
        q = deque()
        noFruit = True

        def bfs(r,c):
            if (r < 0 or c < 0 or r == ROWS or c == COLS or grid[r][c] == 0 or (r,c) in visit):
                return 

            grid[r][c] = 2
            visit.add((r,c))
            q.append([r,c])


        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 2:
                    visit.add((r,c))
                    q.append([r,c])
                if grid[r][c] == 1:
                    noFruit = False

        if not q and noFruit: 
            return 0
        
        minutes = -1
        while q:
            for _ in range(len(q)):
                r,c = q.popleft()
                for dr, dc in directions:
                    bfs(r+dr,c+dc)
            minutes += 1

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    return -1
        return minutes
