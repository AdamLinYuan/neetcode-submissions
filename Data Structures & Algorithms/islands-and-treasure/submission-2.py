class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        ROW, COL = len(grid), len(grid[0])
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        visit = set()
        q = deque()

        def addGrid(r,c):
            if (r < 0 or c < 0 or r == ROW or c == COL or grid[r][c] == -1 or (r,c) in visit):
                return

            visit.add((r,c))
            q.append([r,c])

        for r in range(ROW):
            for c in range(COL):
                if grid[r][c] == 0:
                    visit.add((r,c))
                    q.append([r,c])

        steps = 0
        while q:
            for i in range(len(q)):
                r, c = q.popleft()
                grid[r][c] = steps
                for dr, dc in directions:
                    addGrid(r+dr, c+dc)

            steps += 1
        
