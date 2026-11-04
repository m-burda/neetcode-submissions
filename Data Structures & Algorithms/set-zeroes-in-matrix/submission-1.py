class Solution:
    def setZeroes(self, matrix: list[list[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        O(N * M * (N + M) time), O(1) space
        """
        ROWS = range(len(matrix))
        COLS = range(len(matrix[0]))
        def mark_cells(i, j):
            for r in ROWS:
                if matrix[r][j] != 0:
                    matrix[r][j] = "#"
            for c in COLS:
                if matrix[i][c] != 0:
                    matrix[i][c] = "#"

        for i in ROWS:
            for j in COLS:
                if matrix[i][j] == 0:
                    mark_cells(i, j)

        for i in ROWS:
            for j in COLS:
                if matrix[i][j] == "#":
                    matrix[i][j] = 0
        