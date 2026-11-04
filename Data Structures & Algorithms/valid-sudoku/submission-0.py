class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        subboxes = [[set() for _ in range(3)] for _ in range(3)]

        def check_row(i, j):
            if board[i][j] in rows[i]:
                return False
            rows[i].add(board[i][j])
            return True

        def check_col(i, j):
            if board[i][j] in cols[j]:
                return False
            cols[j].add(board[i][j])
            return True

        def check_subbox(i, j):
            if board[i][j] in subboxes[i // 3][j // 3]:
                return False
            subboxes[i // 3][j // 3].add(board[i][j])
            return True


        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] != ".":
                    if not all([check_row(i, j), check_col(i, j), check_subbox(i, j)]):
                        return False
        
        return True
