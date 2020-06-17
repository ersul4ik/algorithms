from typing import List


class BoardFlliper:
    def solve(self, board: List[List[str]]) -> None:
        if not board:
            return board
        row, col = len(board), len(board[0])
        directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
        visited = set()

        def dfs(x, y):
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if 0 <= nx < row and 0 <= ny < col and board[nx][ny] == 'O' and (nx, ny) not in visited:
                    visited.add((nx, ny))
                    board[nx][ny] = 'G'
                    dfs(nx, ny)

        for x in range(row):
            for y in range(col):
                if (x == 0 or x == row - 1 or y == 0 or y == col - 1) and board[x][y] == 'O' and (x, y) not in visited:
                    board[x][y] = 'G'
                    visited.add((x, y))
                    dfs(x, y)

        for x in range(row):
            for y in range(col):
                if board[x][y] == 'O':
                    board[x][y] = 'X'
                elif board[x][y] == 'G':
                    board[x][y] = 'O'

        return board


if __name__ == '__main__':
    board = [["X", "X", "X", "X"],
             ["X", "O", "O", "X"],
             ["X", "X", "O", "X"],
             ["X", "O", "X", "X"]]
    flipper = BoardFlliper()
    modified_board = flipper.solve(board)

    assert  modified_board == [
        ["X", "X", "X", "X"],
        ["X", "X", "X", "X"],
        ["X", "X", "X", "X"],
        ["X", "O", "X", "X"]
    ]