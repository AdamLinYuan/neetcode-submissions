class Solution:
    def solve(self, board: List[List[str]]) -> None:
        ROWS, COLS = len(board), len(board[0])
        directions = [(1,0), (-1,0), (0,1), (0,-1)]
        q = deque()
        for r in range(ROWS):
            if board[r][0] == "O":
                q.append((r,0))
                board[r][0] = "!"

            if board[r][COLS-1] == "O":
                q.append((r,COLS-1))
                board[r][COLS-1] = "!"

        for c in range(COLS):
            if board[0][c] == "O":
                q.append((0,c))
                board[0][c] = "!"

            if board[ROWS-1][c] == "O":
                q.append((ROWS-1,c))
                board[ROWS-1][c] = "!"

        while q:
            r,c = q.popleft()
            for dr,dc in directions:
                nr, nc = r+dr, c+dc
                if (0 <= nr < ROWS and 0 <= nc < COLS):
                    if (board[nr][nc] == "O"):
                        q.append((nr,nc))
                        board[nr][nc] = "!"

        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == "O":
                    board[r][c] = "X"

        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == "!":
                    board[r][c] = "O"

        return None