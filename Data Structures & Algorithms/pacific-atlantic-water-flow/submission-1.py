class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        pacific = set()
        atlantic = set()
        ROWS, COLS = len(heights), len(heights[0])
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        for r in range(ROWS):
            pacific.add((r,0))
            atlantic.add((r,COLS-1))

        for c in range(COLS):
            pacific.add((0,c))
            atlantic.add((ROWS-1,c))

        def bfs(source):
            q = deque(source)
            while q:
                r, c = q.popleft()
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if (0 <= nr < ROWS and 0 <= nc < COLS) and ((nr,nc) not in source) and (heights[nr][nc] >= heights[r][c]):
                        source.add((nr,nc))
                        q.append((nr,nc))

        bfs(pacific)
        bfs(atlantic)

        res = []

        for r in range(ROWS):
            for c in range(COLS):
                if (r,c) in pacific and (r,c) in atlantic:
                    res.append([r,c])

        return res



        
                
