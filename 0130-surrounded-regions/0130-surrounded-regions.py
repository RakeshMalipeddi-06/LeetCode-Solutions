from collections import deque

class Solution(object):
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        if not board or not board[0]:
            return

        row, col = len(board), len(board[0])
        q = deque()

        for i in range(row):
            for j in range(col):
                if board[i][j] == "O" and (i == 0 or i == row - 1 or j == 0 or j == col - 1):
                    board[i][j] = "#"
                    q.append((i, j))

        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        while q:
            r, c = q.popleft()
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < row and 0 <= nc < col and board[nr][nc] == "O":
                    board[nr][nc] = "#"
                    q.append((nr, nc))

        for i in range(row):
            for j in range(col):
                if board[i][j] == "O":
                    board[i][j] = "X"
                elif board[i][j] == "#":
                    board[i][j] = "O"
        